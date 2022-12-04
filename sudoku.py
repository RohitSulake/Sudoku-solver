#input sudoku-0 if box is empty
grid=[]
for i in range(1,10):
    l=[]
    print("Row",i)
    for j in range(0,9):
        n=int(input("Enter number : "))
        l.append(n)
    grid.append(l)

print(grid)

#function to find and return location of empty boxes
def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c

    return None, None

#function to check if guess is valid
def is_valid(grid, guess, row, col):
    row_vals = grid[row]
    if guess in row_vals:
        return False

    col_vals = [grid[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == guess:
                return False

    return True

#function to make guesses and fill boxes if guess is valid
def solve_suduko(grid):
    row, col = find_empty(grid)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(grid, guess, row ,col):
            grid[row][col] = guess

            if solve_suduko(grid):
                return True

        grid[row][col] = 0

    return False

print(solve_suduko(grid))
print(grid)

def printing(arr):
    for i in range(0,9):
        for j in range(0,9):
            print(arr[i][j], end = " ")
        print()
printing(grid)