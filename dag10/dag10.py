matrix = []
start = None

with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.read().splitlines()):
        row = []
        for j, char in enumerate(line):
            if char.lower() == "s": start = (i, j)
            row.append(char)
        matrix.append(row)


def inside_bounds(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


def get_adjacent(mat, row, col):
    directions = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E":(0, 1),
                  "NW":(-1, -1), "NE":(-1, 1), "SW":(1, -1), "SE":(1, 1)}

    return [(direction, (row+dr, col+dc)) for direction, (dr, dc) in directions.items()
            if inside_bounds(row+dr, col+dc, len(mat), len(mat[0]))]


def fine_print(matrix: list[list[str]]):
    rows, cols = len(matrix), len(matrix[0])

    # Print column indexes on the top
    print("   " + " ".join(f"{i:2}" for i in range(cols)))

    # Print matrix content with row indexes
    for i, row in enumerate(matrix):
        print(f"{i:2} ", end="")
        for elem in row:
            print(f" {elem} ", end="")
        print()
    print()


def is_legal_move(current_node, dest_node, direction):
    legal_connections = {
        '.': ['.'],
        '|': {'N': ["|", "7", "F"], 'S': ["|", "L", "J"], 'W': [], 'E': []},
        '-': {'N': [], 'S': [], 'W': ["-", "L", "F"], 'E': ["-", "7", "J"]},
        'L': {'N': ["|", "7", "F"], 'S': [], 'W': [], 'E': ["-", "J", "7"]},
        'J': {'N': ["|", "7", "F"], 'S': [], 'W': ["-", "F", "L"], 'E': []},
        '7': {'N': [], 'S': ["|", "J", "L"], 'W': ["-", "L", "F"], 'E': []},
        'F': {'N': [], 'S': ["|", "L", "J"], 'W': [], 'E': ["-", "J", "7"]},
        'S': {'N': ["|", "F", "7"], 'S': ["|", "L", "J"], 'W': ["-", "L", "F"], 'E': ["-", "7", "J"]},
    }
    return dest_node in legal_connections[current_node][direction]



def traverse(matrix):
    row, col = start

    while True:
        current_node = matrix[row][col]
        adjacent = get_adjacent(matrix, row, col)

        legal_paths = []
        for direction, (dr, dc) in adjacent[:-4]:
            dest_node = matrix[dr][dc]
            allowed = is_legal_move(current_node, dest_node, direction)

            if allowed: legal_paths.append(dest_node)

        print("On node:", current_node)
        print("Legal Paths:", legal_paths)
        print()

        if current_node.lower() == "s":
            print("End")
            break


fine_print(matrix)
traverse(matrix)

