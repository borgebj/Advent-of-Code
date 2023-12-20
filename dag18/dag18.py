import copy
import random

from annet.algoritmer.Matrix import Matrix

p1_dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
p2_dirs = {"0": p1_dirs["R"], "1": p1_dirs["D"], "2": p1_dirs["L"], "3": p1_dirs["U"]}


# parsing
def parse():
    with open("input", "r") as f:
        return [line.split() for line in f.readlines()]


# creates generator for part 1
def part1():
    for direction, steps, _ in parse():
        yield p1_dirs[direction], int(steps)

# creates generator for part 2
def part2():
    for _, _, hex in parse():
        hex = hex[hex.find("(") + 1:hex.find(")")]
        yield p2_dirs[hex[-1]], int(hex[1:-1], 16)


# Uses shoelace algorithm for area of polgyons
def shoelace(vertices):
    total = 0
    for i in range(len(vertices) - 1):
        row, col = vertices[i][0], vertices[i][1]  # current row, col
        nrow, ncol = vertices[i + 1][0], vertices[i + 1][1]  # next row, col
        total += (row * ncol) - (col * nrow)  # difference of cross

    return int(abs(total) * 0.5)


# finds all vertices and calculates
def calculate(generator):
    vertices = [(0, 0)]
    perimeter = 0

    for (dx, dy), steps in generator:
        row = vertices[-1][0] + dx * steps
        col = vertices[-1][1] + dy * steps
        vertices.append((row, col))
        perimeter += steps

    count = shoelace(vertices)
    return count + perimeter // 2 + 1


print(f'Part 1 area: {calculate(part1()):_}')
print(f'Part 2 area: {calculate(part2()):_}')


# ----------------------- [ OLD ] --------------------------------------
# includes:
# - ray-casting
# - flood-fil
# - matrix-creation


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

    print(*mat, sep="\n")
    return Matrix(mat)

# matrix = create_matrix(parse())
# filled_matrix = ray_cast(matrix)
#
# border = sum([line.count("#") for line in matrix.board])
# fill = sum([line.count("#") for line in filled_matrix.board])
#
# print(f'Border count: {border}')
# print(f'Filled count: {fill}')
#
# matrix.print_to_html("border.html")
# filled_matrix.print_to_html("filled.html")