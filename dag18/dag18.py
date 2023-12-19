import copy
import random

from annet.algoritmer.Matrix import Matrix

# parsing
with open("input", "r") as f:
    instructions = [line.split() for line in f.readlines()]


# casts a ray from a random point to the edge to identify if point is inside or outside loop
def ray_cast(mat):
    rows, cols = mat.max_rows, mat.max_cols
    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

    indices = [(row + i * direction[0], col + i * direction[1]) for i in range(max(rows, cols))]
    indices = [(i, j) for i, j in indices if 0 <= i < rows and 0 <= j < cols]

    count = sum(mat.board[i][j] == '#' for i, j in indices)  # counts crossings of loop-lines

    # returns point inside the loop
    if count == 1 and mat.board[row][col] != "#":
        return flood_fill(mat, row, col, "#")
    return ray_cast(mat)


# flood fills using DFS
def flood_fill(mat, i, j, fill):
    stack = [(i, j)]
    new_mat = copy.deepcopy(mat)

    while stack:
        row, col = stack.pop()

        if new_mat.inside_bounds(row, col) and new_mat.board[row][col] != "#":
            new_mat.board[row][col] = fill

            stack.append((row - 1, col))  # North
            stack.append((row + 1, col))  # South
            stack.append((row, col - 1))  # West
            stack.append((row, col + 1))  # East

    return new_mat


def create_matrix(instructions):
    true_dir = {"0": "R", "1": "D", "2": "L", "3": "U"}
    edges = 0

    # base matrix and (x,y)
    mat = [["."]]
    row, col = 0, 0

    for direction, steps, rgb in instructions:
        steps = int(steps)

        # part 2: creates the true instructions
        rgb = rgb[rgb.find("(")+1:rgb.find(")")]
        direction = true_dir[rgb[-1]]
        steps = int(rgb[1:-1], 16)

        # moves 'direction' in 'steps' steps
        for _ in range(steps):
            edges += 1
            match direction:
                case "U":
                    row -= 1
                case "D":
                    row += 1
                case "L":
                    col -= 1
                case "R":
                    col += 1

            # Ensure row and col are non-negative
            if row < 0:
                # Insert an empty row at the beginning
                mat.insert(0, ["."] * len(mat[0]))
                row = 0
            if col < 0:
                # Insert an empty column at the beginning of each row
                [r.insert(0, ".") for r in mat]
                col = 0

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

    return Matrix(mat)


matrix = create_matrix(instructions)
filled_matrix = ray_cast(matrix)

border = sum([line.count("#") for line in matrix.board])
fill = sum([line.count("#") for line in filled_matrix.board])

print(f'Border count: {border}')
print(f'Filled count: {fill}')

matrix.print_to_html("border.html")
filled_matrix.print_to_html("filled.html")
