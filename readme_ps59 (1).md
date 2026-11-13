# PS No. 59: Maze Escape Game

- **Student Name:** Nushrat Ansari erp - Ru-26-02306
- **Course:** Bachelor of Computer Application (BCA) - 1st Semester (Section 1B)
- **Subject:** Programming Fundamentals Using Python (`RU-100-05-00058`)
- **College:** Rungta International Skills University

---

## About The Project

This is my 1st semester BCA Python project (**PS No. 59: Maze Escape Game**). It is a console-based maze game where the player starts at position `(0, 0)` in a 5x5 maze stored as a 2D list and navigates to the exit `E` at `(4, 4)` using `W`, `A`, `S`, and `D` keys. The program blocks moves into walls (`#`) or outside the maze boundaries without counting them as moves, and uses the **Breadth-First Search (BFS)** algorithm to calculate the shortest path from start to exit.

---

## Features

- **2D List Maze Representation:** Stores the 5x5 grid as a Python list of lists and prints the updated board after every move.
- **W/A/S/D Movement & Validation:** Moves Up (`W`), Left (`A`), Down (`S`), and Right (`D`). Checks for invalid keys, boundary limits, and wall collisions (`#`).
- **Accurate Move Counter:** Counts only valid steps and displays the winning message when the player reaches the exit `E`.
- **Shortest Path Finder (BFS):** Implements Breadth-First Search using a queue to find and display the minimum number of steps (`10 steps`) from `(0, 0)` to `(4, 4)`.
- **Built-in Test Case Runner:** Includes an option in the menu to test all 4 university evaluation test cases automatically.

---

## Maze Layout (5x5)

```text
Row 0:  P  .  .  #  #
Row 1:  #  #  .  #  #
Row 2:  #  .  .  .  #
Row 3:  #  .  #  #  #
Row 4:  #  .  .  .  E
```
- `P` = Player / Start `(0, 0)`
- `E` = Exit `(4, 4)`
- `.` = Open Path
- `#` = Wall (Blocked)

---

## Files in this Repository

1. **`maze_escape_game.py`** — Complete Python 3 source code (uses standard Python, no external packages required).
2. **`Project_Report_PS59.pdf`** — Project documentation report with algorithm, BFS visual diagram, and test cases.
3. **`README.md`** — Project overview and instructions.

---

## How to Run

1. Open terminal or Command Prompt in the project folder.
2. Run the Python script directly:
   ```bash
   python maze_escape_game.py
   ```

---

## Test Cases Output

### Test Case 1: Normal Input
- **Input:** `Move: D`
- **Output:**
  ```text
  Player moved to (row 0, col 1) | Moves: 1
  ```

### Test Case 2: Boundary / Minimum Input
- **Input:** `Player at (0, 0)`, `Move: W (up, outside the maze)`
- **Output:**
  ```text
  Cannot move outside the maze. Player stays at (0, 0) | Moves: 0
  ```

### Test Case 3: Invalid Input
- **Input:** `Moves: D, D, D, X`
- **Output:**
  ```text
  Wall ahead. Move blocked. Player stays at (0, 2)
  Invalid key 'X'. Use W, A, S or D only.
  Moves counted: 2
  ```

### Test Case 4: Different Valid Scenario
- **Input:**
  - `(a) Moves: D, D, S, S, A, S, S, D, D, D`
  - `(b) Menu option 2 (Shortest path)`
- **Output:**
  ```text
  (a) You escaped the maze! Total moves: 10
  (b) Shortest path length: 10 steps
  ```
