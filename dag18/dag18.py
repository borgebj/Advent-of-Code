import random

# parsing
with open("input", "r") as f:
    instructions = [line.split() for line in f.readlines()]


def ray_cast(mat):
    rows, cols = len(mat), len(mat[0])
    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

    indices = [(row + i * direction[0], col + i * direction[1]) for i in range(max(rows, cols))]
    indices = [(i, j) for i, j in indices if 0 <= i < rows and 0 <= j < cols]

    count = sum(mat[i][j] == '#' for i, j in indices)  # counts crossings of loop-lines

    # returns point inside the loop
    if count == 1 and mat[row][col] != "#":
        return row, col
    return ray_cast(mat)


def create_matrix(instructions):
    edges = 0

    # base matrix and (x,y)
    mat = [["."]]
    row, col = 0, 0

    for direction, steps, rgb in instructions:
        steps = int(steps)

        # moves 'direction' in 'steps' steps
        for _ in range(steps):
            edges += 1
            match direction:
                case "U": row -= 1
                case "D": row += 1
                case "L": col -= 1
                case "R": col += 1

            max_rows = max(row, len(mat) - 1)
            max_cols = max(col, len(mat[0]) - 1)

            # create new matrix based on new size
            new_mat = [["."] * (max_cols + 1) for _ in range(max_rows + 1)]

            # copy previous matrix to new
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    new_mat[r][c] = mat[r][c]

            # put in new path-value
            new_mat[row][col] = "#"
            mat = new_mat

    print(edges)
    return mat


matrix = create_matrix(instructions)
c = ray_cast(matrix)
print(c)

[print(x, end=" ") if i < len(row) - 1 else print(x) for row in matrix for i, x in enumerate(row)]
