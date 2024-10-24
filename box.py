from collections import deque

def is_valid_move(x, y, M, N, grid):
    """Check if the move is valid within grid bounds and lands on a 0 (empty cell)."""
    return 0 <= x < M and 0 <= y < N and grid[x][y] == 0

def get_next_positions(curr_x, curr_y, move_x, move_y):
    """Get all possible next positions using the move rule in all four directions."""
    # Forward move
    forward = (curr_x + move_x, curr_y + move_y)
    
    # Right move (90° clockwise rotation of move vector)
    right = (curr_x + move_y, curr_y - move_x)
    
    # Left move (90° counterclockwise rotation of move vector)
    left = (curr_x - move_y, curr_y + move_x)
    
    # Backward move (180° rotation)
    back = (curr_x - move_x, curr_y - move_y)
    
    return [forward, right, left, back]

def find_min_moves(M, N, grid, start_x, start_y, dest_x, dest_y, move_x, move_y):
    """Find minimum moves required to reach destination using BFS, and track the path."""
    queue = deque([(start_x, start_y, 0, [])])  # Include a list to track the path
    visited = set([(start_x, start_y)])
    
    while queue:
        curr_x, curr_y, moves, path = queue.popleft()
        
        # If we've reached the destination
        if curr_x == dest_x and curr_y == dest_y:
            return moves, path + [(dest_x, dest_y)]  # Return the final path
        
        next_positions = get_next_positions(curr_x, curr_y, move_x, move_y)
        
        for next_x, next_y in next_positions:
            if (next_x, next_y) not in visited and is_valid_move(next_x, next_y, M, N, grid):
                queue.append((next_x, next_y, moves + 1, path + [(curr_x, curr_y)]))
                visited.add((next_x, next_y))
    
    return -1, []  # If no path is found

def solve():
    # Read input
    input_data = list(map(int, input().strip().split()))
    
    M = input_data[0]
    N = input_data[1]
    
    # Construct the grid
    grid = []
    index = 2
    for _ in range(M):
        row = input_data[index:index + N]
        grid.append(row)
        index += N
    
    # Read start and destination coordinates and move rules
    start_x, start_y = input_data[index], input_data[index + 1]
    dest_x, dest_y = input_data[index + 2], input_data[index + 3]
    move_x, move_y = input_data[index + 4], input_data[index + 5]
    
    # Find minimum moves and path
    result, path = find_min_moves(M, N, grid, start_x, start_y, dest_x, dest_y, move_x, move_y)
    print("Minimum Moves:", result)
    print("Path Taken:", path)

if __name__ == "__main__":
    solve()
