def read_grid(file_path):
    grid = []

    with open(file_path, 'r') as file:
        for line in file:

            row = [x for x in line.split() if x != '*']
            if row:
                grid.append(row)

    return grid


def print_grid_by_columns(grid):

    num_columns = len(grid[0])


    result = []
    for col in range(num_columns):
        column = [grid[row][col] for row in range(len(grid))]
        result.append(column)
    return result


def print_grid_by_diagonals(grid):
    m = len(grid)
    n = len(grid[0])


    diagonals_1 = []
    for d in range(m + n - 1):
        diag = []
        for i in range(max(0, d - n + 1), min(d + 1, m)):
            j = d - i
            if 0 <= j < n:
                diag.append(grid[i][j])
        diagonals_1.append(diag)


    diagonals_2 = []
    for d in range(m + n - 1):
        diag = []
        for i in range(max(0, d - n + 1), min(d + 1, m)):
            j = n - 1 - (d - i)
            if 0 <= j < n:
                diag.append(grid[i][j])
        diagonals_2.append(diag)

    return diagonals_1, diagonals_2



file_path = '/mnt/data/wood.txt'


grid = read_grid(file_path)
print("Grid:")
for row in grid:
    print(row)


print("\nColumns:")
columns = print_grid_by_columns(grid)
for col in columns:
    print(col)


print("\nDiagonals (first direction):")
diagonals_1, diagonals_2 = print_grid_by_diagonals(grid)
for diag in diagonals_1:
    print(diag)

print("\nDiagonals (second direction):")
for diag in diagonals_2:
    print(diag)
