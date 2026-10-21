N = 8

# Create an empty 8 x 8 chessboard
board = [[0 for _ in range(N)] for _ in range(N)]


# Check whether a Queen can be placed at board[row][col]
def is_safe(row, col):
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve_queens(row):
    # All queens have been placed
    if row == N:
        return True

    # Try every column in the current row
    for col in range(N):
        if is_safe(row, col):
            # Place Queen
            board[row][col] = 1

            # Recursively place the remaining Queens
            if solve_queens(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Place the first Queen at a fixed position
first_row = 0
first_col = 0
board[first_row][first_col] = 1

print("Initial 8-Queens Matrix:")
for row in board:
    print(row)

# Start backtracking from the second row
if solve_queens(1):
    print("\nFinal 8-Queens Matrix:")
    for row in board:
        print(row)
else:
    print("\nNo solution exists for the given first Queen position.")

print("\nComplexity Analysis:")
print("Worst-case Time Complexity : O(N)")
print("Space Complexity : O(N^2)")
