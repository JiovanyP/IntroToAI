import heapq

graph = {
    'A': [('B',2),('C',4)],
    'B': [('A',2),('D',3),('E',1)],
    'C': [('A',4),('E',2)],
    'D': [('B',3),('E',3)],
    'E': [('B',1),('C',2),('D',3)]
}

heuristic = {
    'A':5,
    'B':3,
    'C':4,
    'D':0,
    'E':2
}

def astar(start,goal):
    open_list=[]
    heapq.heappush(open_list,(0,start))

    g={start:0}
    came={}

    while open_list:
        current=heapq.heappop(open_list)[1]

        if current==goal:
            path=[]
            while current in came:
                path.append(current)
                current=came[current]
            path.append(start)
            return path[::-1]

        for neighbor,cost in graph[current]:
            new_cost=g[current]+cost

            if neighbor not in g or new_cost<g[neighbor]:
                g[neighbor]=new_cost
                f=new_cost+heuristic[neighbor]
                heapq.heappush(open_list,(f,neighbor))
                came[neighbor]=current

print("Shortest Path:", astar('A','D'))