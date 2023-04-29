from queue import PriorityQueue

# The state of the problem is represented as a tuple (m, c, b),
# where m is the number of missionaries on the left bank, c is
# the number of cannibals on the left bank, and b is 1 if the
# boat is on the left bank, or 0 if it is on the right bank.

def is_valid_state(state):
    m, c, b = state
    if m < 0 or m > 3 or c < 0 or c > 3 or (b != 0 and b != 1):
        return False
    if m > 0 and m < c:
        return False
    if m < 3 and m < c:
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 0)

def get_successors(state):
    m, c, b = state
    successors = []
    if b == 1:
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    new_m = m - i
                    new_c = c - j
                    new_b = 0
                    if is_valid_state((new_m, new_c, new_b)):
                        successors.append(((new_m, new_c, new_b), i + j))
    else:
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    new_m = m + i
                    new_c = c + j
                    new_b = 1
                    if is_valid_state((new_m, new_c, new_b)):
                        successors.append(((new_m, new_c, new_b), i + j))
    return successors

def uniform_cost_search(start_state):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((0, [start_state]))
    while not frontier.empty():
        (cost, path) = frontier.get()
        state = path[-1]
        if is_goal_state(state):
            return path
        if state not in explored:
            explored.add(state)
            for (succ, succ_cost) in get_successors(state):
                if succ not in explored:
                    new_path = path + [succ]
                    new_cost = cost + succ_cost
                    frontier.put((new_cost, new_path))
    return None

# Example usage:
start_state = (3, 3, 1)
path = uniform_cost_search(start_state)
if path is None:
    print("No solution found")
else:
    for state in path:
        print(state)