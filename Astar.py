import heapq

grid = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '#'],
    ['.', '#', '.', 'G']
]

start = (0,0)
goal = (3,3)

rows = len(grid)
cols = len(grid[0])

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar():
    open_list = []
    heapq.heappush(open_list,(0,start))

    came_from = {}
    g = {start:0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path=[]
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        neighbors=[(0,1),(1,0),(-1,0),(0,-1)]

        for dx,dy in neighbors:
            nx=current[0]+dx
            ny=current[1]+dy

            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] != '#':
                new_cost=g[current]+1
                if (nx,ny) not in g or new_cost<g[(nx,ny)]:
                    g[(nx,ny)] = new_cost
                    f = new_cost + heuristic((nx,ny),goal)
                    heapq.heappush(open_list,(f,(nx,ny)))
                    came_from[(nx,ny)] = current

print("Shortest Path:", astar())