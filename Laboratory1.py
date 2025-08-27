def dfa1(string):
    """Automaton 1: Accepts language 010(1)*"""
    state = "a"  # start state

    for ch in string:
        if state == "a":
            if ch == "0":
                state = "b"
            elif ch == "1":
                state = "a"
            else:
                return False
        elif state == "b":
            if ch == "1":
                state = "c"
            else:
                return False
        elif state == "c":
            if ch == "0":
                state = "d"
            else:
                return False
        elif state == "d":
            if ch == "1":
                state = "d"
            else:
                return False

    return state == "d"  # accept state
# Accepted examples: 010, 0101, 01011
# Rejected examples: 0, 1, 00


def dfa2(string):
    """Automaton 2: Square cycle, accepts if final state is q0 or q3"""
    state = "q0"  # start state

    for ch in string:
        if state == "q0":
            if ch == "a":
                state = "q1"
            elif ch == "b":
                state = "q2"
            else:
                return False
        elif state == "q1":
            if ch == "a":
                state = "q3"
            elif ch == "b":
                state = "q0"
            else:
                return False
        elif state == "q2":
            if ch == "a":
                state = "q0"
            elif ch == "b":
                state = "q3"
            else:
                return False
        elif state == "q3":
            if ch == "a":
                state = "q2"
            elif ch == "b":
                state = "q1"
            else:
                return False

    return state in ["q0", "q3"]  # accept if final state is q0 or q3
# Accepted examples: "bb", "abab", "aabb"
# Rejected examples: "a", "b", "aaa"


while True:
    print("\nChoose DFA to test:")
    print("1. DFA1 (language: 010(1)*)")
    print("2. DFA2 (square cycle, accepts if final state is q0 or q3)")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        user_input = input("Enter a string of 0s and 1s: ").strip()
        result = "ACCEPTED" if dfa1(user_input) else "REJECTED"
        print(f"Result: {result}")

    elif choice == "2":
        user_input = input("Enter a string of a's and b's: ").strip()
        result = "ACCEPTED" if dfa2(user_input) else "REJECTED"
        print(f"Result: {result}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
