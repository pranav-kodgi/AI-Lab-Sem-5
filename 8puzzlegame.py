# 8-Puzzle Solver using DFS and IDS for the specified Initial and Goal states

# Initial and Goal states defined from the image (0 represents the blank tile)
START_STATE = (5, 4, 0,
               6, 1, 8,
               7, 3, 2)

GOAL_STATE = (0, 1, 2,
              3, 4, 5,
              6, 7, 8)

# Valid movements: (row_offset, col_offset, action_name)
MOVES = [
    (-1, 0, 'Up'),
    (1, 0, 'Down'),
    (0, -1, 'Left'),
    (0, 1, 'Right')
]

def get_neighbors(state):
    """Generates valid successor states from the current state."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    for dr, dc, action in MOVES:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            # Swap empty space with the neighboring tile
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append((tuple(state_list), action))
            
    return neighbors

def print_board(state):
    """Formats and prints the 3x3 board."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else ' ' for x in state[i:i+3]]
        print(f"| {' | '.join(row)} |")
    print("-" * 13)


# ==========================================
# 1. Depth-First Search (DFS)
# ==========================================
def dfs(start_state, max_depth=30):
    """Solves 8-puzzle using Depth-First Search with a depth limit."""
    stack = [(start_state, [], 0)]  # (current_state, path, current_depth)
    visited = {start_state: 0}

    nodes_expanded = 0

    while stack:
        state, path, depth = stack.pop()
        nodes_expanded += 1

        if state == GOAL_STATE:
            return path, nodes_expanded

        if depth < max_depth:
            for neighbor, action in get_neighbors(state):
                if neighbor not in visited or visited[neighbor] > depth + 1:
                    visited[neighbor] = depth + 1
                    stack.append((neighbor, path + [action], depth + 1))

    return None, nodes_expanded


# ==========================================
# 2. Iterative Deepening Search (IDS)
# ==========================================
def depth_limited_search(state, depth, path, visited):
    """Recursive Depth-Limited Search helper for IDS."""
    if state == GOAL_STATE:
        return path, 1

    if depth <= 0:
        return None, 1

    nodes_expanded = 1
    for neighbor, action in get_neighbors(state):
        if neighbor not in visited:
            visited.add(neighbor)
            result, expanded = depth_limited_search(neighbor, depth - 1, path + [action], visited)
            nodes_expanded += expanded
            visited.remove(neighbor)
            
            if result is not None:
                return result, nodes_expanded

    return None, nodes_expanded


def ids(start_state, max_depth=50):
    """Solves 8-puzzle using Iterative Deepening Search."""
    total_nodes_expanded = 0

    for depth in range(max_depth):
        visited = {start_state}
        solution, nodes = depth_limited_search(start_state, depth, [], visited)
        total_nodes_expanded += nodes

        if solution is not None:
            return solution, total_nodes_expanded

    return None, total_nodes_expanded


# ==========================================
# Main Execution
# ==========================================
if __name__ == "__main__":
    print("--- Initial State ---")
    print_board(START_STATE)

    print("--- Target Goal State ---")
    print_board(GOAL_STATE)

    # --- DFS Execution ---
    dfs_path, dfs_nodes = dfs(START_STATE, max_depth=30)
    print("\n=== Depth-First Search (DFS) ===")
    if dfs_path:
        print(f"Solution found in {len(dfs_path)} steps!")
        print(f"Path: {dfs_path}")
        print(f"Nodes expanded: {dfs_nodes}")
    else:
        print("No solution found within DFS max depth limit.")

    # --- IDS Execution ---
    ids_path, ids_nodes = ids(START_STATE, max_depth=50)
    print("\n=== Iterative Deepening Search (IDS) ===")
    if ids_path:
        print(f"Optimal Solution found in {len(ids_path)} steps!")
        print(f"Path: {ids_path}")
        print(f"Nodes expanded: {ids_nodes}")
    else:
        print("No solution found within IDS depth limit.")
