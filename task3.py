# Sudoku Solver using Backtracking

def print_grid(grid):
    """Function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty_location(grid):
    """Find an empty cell in the Sudoku grid (marked as 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_safe(grid, row, col, num):
    """Check if placing 'num' is valid in the given row, column, and 3x3 box."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # No empty location → puzzle solved

    row, col = empty_loc

    for num in range(1, 10):  # Try digits 1–9
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Undo assignment (backtrack)
            grid[row][col] = 0

    return False  # Triggers backtracking

# Example unsolved Sudoku grid (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("🧩 Unsolved Sudoku:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\n✅ Solved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("❌ No solution exists.")
