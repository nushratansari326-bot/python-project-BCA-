# PS No. 59: Maze Escape Game
# Student Name: Nushrat Ansari
# Class: BCA 1st Semester (Section 1B)
# Subject: Programming Fundamentals Using Python (RU-100-05-00058)
# University: Rungta International Skills University

# -------------------------------------------------------------
# 1. Function to create a fresh 5x5 maze as a 2D list
# -------------------------------------------------------------
def create_maze():
    """
    Returns the 5x5 maze as a 2D list (list of lists).
    'P' = Start (0, 0), 'E' = Exit (4, 4), '#' = Wall, '.' = Path
    """
    maze = [
        ["P", ".", ".", "#", "#"],
        ["#", "#", ".", "#", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", "#", "#", "#"],
        ["#", ".", ".", ".", "E"]
    ]
    return maze


# -------------------------------------------------------------
# 2. Function to display the maze on the console
# -------------------------------------------------------------
def print_maze(maze, player_row, player_col):
    """
    Prints the 5x5 maze with the player's current position 'P'.
    """
    print("\n--- Current Maze (5x5) ---")
    for r in range(5):
        row_str = ""
        for c in range(5):
            if r == player_row and c == player_col:
                row_str = row_str + "P "
            elif maze[r][c] == "P":
                # Original start cell becomes '.' when player moves away
                row_str = row_str + ". "
            else:
                row_str = row_str + maze[r][c] + " "
        print("  " + row_str.strip())
    print("--------------------------")


# -------------------------------------------------------------
# 3. Function to process a single W/A/S/D move
# -------------------------------------------------------------
def make_move(maze, player_row, player_col, moves_count, key, verbose=True):
    """
    Moves the player using W (up), A (left), S (down), D (right).
    Blocks moves outside the maze or into walls ('#').
    Only valid moves increase moves_count.
    """
    key = key.strip().upper()

    # Validate key input
    if key not in ["W", "A", "S", "D"]:
        if verbose:
            print(f"Invalid key '{key}'. Use W, A, S or D only.")
        return player_row, player_col, moves_count, False

    # Calculate new row and column based on direction
    new_row = player_row
    new_col = player_col

    if key == "W":
        new_row = player_row - 1
    elif key == "S":
        new_row = player_row + 1
    elif key == "A":
        new_col = player_col - 1
    elif key == "D":
        new_col = player_col + 1

    # Check if move is outside the 5x5 boundary (0 to 4)
    if new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 5:
        if verbose:
            print(
                f"Cannot move outside the maze. Player stays at ({player_row}, {player_col}) | Moves: {moves_count}"
            )
        return player_row, player_col, moves_count, False

    # Check if there is a wall '#' ahead
    if maze[new_row][new_col] == "#":
        if verbose:
            print(
                f"Wall ahead. Move blocked. Player stays at ({player_row}, {player_col})"
            )
        return player_row, player_col, moves_count, False

    # Valid move! Update position and count
    player_row = new_row
    player_col = new_col
    moves_count = moves_count + 1

    # Check if player reached Exit 'E'
    if maze[player_row][player_col] == "E":
        if verbose:
            print(f"You escaped the maze! Total moves: {moves_count}")
        return player_row, player_col, moves_count, True

    if verbose:
        print(
            f"Player moved to (row {player_row}, col {player_col}) | Moves: {moves_count}"
        )
    return player_row, player_col, moves_count, False


# -------------------------------------------------------------
# 4. Function to find shortest path using BFS algorithm
# -------------------------------------------------------------
def find_shortest_path_bfs(maze):
    """
    Uses Breadth-First Search (BFS) with a simple list queue
    to find the shortest path from start (0, 0) to exit (4, 4).
    Returns the shortest number of steps and the list of coordinates.
    """
    start = (0, 0)
    exit_cell = (4, 4)

    # Queue stores tuples of: (row, col, steps, path_list)
    queue = [(start[0], start[1], 0, [start])]
    visited = [start]

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(queue) > 0:
        # Pop the first element from queue (FIFO for BFS)
        curr_r, curr_c, steps, path = queue.pop(0)

        # Check if we reached the exit
        if (curr_r, curr_c) == exit_cell:
            return steps, path

        # Check all 4 neighbors
        for dr, dc in directions:
            next_r = curr_r + dr
            next_c = curr_c + dc

            # Check boundaries, wall, and whether already visited
            if 0 <= next_r < 5 and 0 <= next_c < 5:
                if maze[next_r][next_c] != "#" and (next_r, next_c) not in visited:
                    visited.append((next_r, next_c))
                    new_path = path + [(next_r, next_c)]
                    queue.append((next_r, next_c, steps + 1, new_path))

    return -1, []


# -------------------------------------------------------------
# 5. Interactive Play Function (Menu Option 1)
# -------------------------------------------------------------
def play_game():
    """
    Lets the player play the maze game interactively from the console.
    """
    maze = create_maze()
    player_row = 0
    player_col = 0
    moves_count = 0

    print("\nWelcome to the Maze Escape Game!")
    print("Controls: W = Up, A = Left, S = Down, D = Right, Q = Quit to Menu")
    print_maze(maze, player_row, player_col)

    while True:
        user_input = input("Enter move (W/A/S/D) or Q to quit: ").strip()
        if user_input.upper() == "Q":
            print("Returning to main menu...")
            break

        player_row, player_col, moves_count, won = make_move(
            maze, player_row, player_col, moves_count, user_input, verbose=True
        )
        print_maze(maze, player_row, player_col)

        if won:
            break


# -------------------------------------------------------------
# 6. Built-in Test Cases Runner (Verifies all 4 Syllabus Cases)
# -------------------------------------------------------------
def run_all_test_cases():
    """
    Runs all 4 official test cases from the problem sheet.
    """
    print("\n==============================================================")
    print("         RUNNING 4 OFFICIAL TEST CASES (PS NO. 59)            ")
    print("==============================================================")

    # Test Case 1: Normal Input
    print("\n--- Test Case 1: Normal Input ---")
    print("Input: Move: D")
    maze1 = create_maze()
    r, c, m = 0, 0, 0
    r, c, m, _ = make_move(maze1, r, c, m, "D", verbose=True)

    # Test Case 2: Boundary / Minimum Input
    print("\n--- Test Case 2: Boundary / Minimum Input ---")
    print("Input: Player at (0, 0), Move: W (up, outside the maze)")
    maze2 = create_maze()
    r, c, m = 0, 0, 0
    r, c, m, _ = make_move(maze2, r, c, m, "W", verbose=True)

    # Test Case 3: Invalid Input
    print("\n--- Test Case 3: Invalid Input ---")
    print("Input: Moves: D, D, D, X")
    maze3 = create_maze()
    r, c, m = 0, 0, 0
    # First two valid moves (D, D)
    r, c, m, _ = make_move(maze3, r, c, m, "D", verbose=False)
    r, c, m, _ = make_move(maze3, r, c, m, "D", verbose=False)
    # 3rd move D hits wall at (0, 3)
    r, c, m, _ = make_move(maze3, r, c, m, "D", verbose=True)
    # 4th move X is invalid key
    r, c, m, _ = make_move(maze3, r, c, m, "X", verbose=True)
    print(f"Moves counted: {m}")

    # Test Case 4: Different Valid Scenario
    print("\n--- Test Case 4: Different Valid Scenario ---")
    print("Input: (a) Moves: D, D, S, S, A, S, S, D, D, D")
    print("       (b) Menu option 2 (Shortest path)")
    maze4 = create_maze()
    r, c, m = 0, 0, 0
    moves_seq = ["D", "D", "S", "S", "A", "S", "S", "D", "D", "D"]
    for step_idx in range(len(moves_seq)):
        move_key = moves_seq[step_idx]
        # Print final winning message on the last move
        is_last = (step_idx == len(moves_seq) - 1)
        if is_last:
            print("(a) ", end="")
        r, c, m, won = make_move(maze4, r, c, m, move_key, verbose=is_last)

    steps, path = find_shortest_path_bfs(maze4)
    print(f"(b) Shortest path length: {steps} steps")
    print("==============================================================\n")


# -------------------------------------------------------------
# Main Program Loop
# -------------------------------------------------------------
def main():
    while True:
        print("\n===========================================")
        print("       MAZE ESCAPE GAME (PS NO. 59)        ")
        print("===========================================")
        print("1. Play Maze Game (W/A/S/D)")
        print("2. Find Shortest Path (BFS Algorithm)")
        print("3. View Maze Layout")
        print("4. Run All 4 Evaluation Test Cases")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            maze = create_maze()
            steps, path = find_shortest_path_bfs(maze)
            print(f"\nShortest path length: {steps} steps")
            path_str = " -> ".join([f"({r},{c})" for r, c in path])
            print(f"BFS Shortest Path: {path_str}")
        elif choice == "3":
            maze = create_maze()
            print_maze(maze, 0, 0)
        elif choice == "4":
            run_all_test_cases()
        elif choice == "5":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()