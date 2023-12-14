matrix = []
start = None

with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.read().splitlines()):
        row = []
        for j, char in enumerate(line):
            if char.lower() == "s": start = (i, j)
            row.append(char)
        matrix.append(row)


def fine_print(matrix):
    print()
    rows, cols = len(matrix), len(matrix[0])

    # colored-text
    RESET = '\033[0m'
    GREEN = '\033[92m'

    # Calculate the maximum width of elements in the matrix
    max_width = max(len(str(matrix[i][j])) for i in range(rows) for j in range(cols)) + 1

    # Print column indices on the top
    print("    " + " ".join(f"{i:>{max_width}}" for i in range(cols)))

    # Print a horizontal line
    print("   " + "-" * (max_width * cols + 4) + "-" * max_width)

    # Print matrix content with row indices
    for i, row in enumerate(matrix):
        print(f"{i:>{max_width}} |", end="")
        for j, elem in enumerate(row):
            if elem != 0 and elem != "." or (i, j) == start:
                print(f"{GREEN}{elem:>{max_width}}{RESET} ", end="")
            else:
                print(f"{elem:>{max_width}} ", end="")
        print()
    print()


def inside_bounds(row, col, max_rows, max_cols):
    return 0 <= row < max_rows and 0 <= col < max_cols


def get_adjacent(row, col):
    directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    row_len, col_len = len(matrix), len(matrix[0])

    return [(direction, matrix[row+dr][col+dc], (row + dr, col + dc))
            for direction, (dr, dc) in directions.items()
            if inside_bounds(row + dr, col + dc, row_len, col_len)]


def opposite_direction(direction):
    opposite = {"N": "S", "S": "N", "E": "W", "W": "E", "X": "?"}
    return opposite[direction]


def is_legal_move(current_node, dest_node, direction):
    legal_connections = {
        '.': ['.'],
        '|': {'N': ['|', '7', 'F'], 'S': ['|', 'L', 'J'], 'W': [], 'E': []},
        '-': {'N': [], 'S': [], 'W': ['-', 'L', 'F'], 'E': ['-', '7', 'J']},
        'L': {'N': ['|', '7', 'F'], 'S': [], 'W': [], 'E': ['-', 'J', '7']},
        'J': {'N': ['|', '7', 'F'], 'S': [], 'W': ['-', 'F', 'L'], 'E': []},
        '7': {'N': [], 'S': ['|', 'J', 'L'], 'W': ['-', 'L', 'F'], 'E': []},
        'F': {'N': [], 'S': ['|', 'L', 'J'], 'W': [], 'E': ['-', 'J', '7']},
        'S': {'N': ['|', 'F', '7'], 'S': ['|', 'L', 'J'], 'W': ['-', 'L', 'F'], 'E': ['-', '7', 'J']},
    }
    return dest_node in legal_connections[current_node][direction] or dest_node == "S"


def get_legal_paths(current_node, adjacent):
    legal_paths = []

    for direction, sym, (dr, dc) in adjacent:
        dest_node = matrix[dr][dc]
        if is_legal_move(current_node, dest_node, direction):
            legal_paths.append((direction, sym, (dr, dc)))

    return legal_paths


def traverse(from_sym, distances, from_dir, i):
    i += 1

    # retrieves info on current node
    row, col = from_sym
    current_node = matrix[row][col]

    # base case
    if current_node.lower() == "s" and distances[row][col] != 0:
        print("\nEnd\n")
        return

    # gets all legal paths
    adjacent = get_adjacent(row, col)
    legal_paths = get_legal_paths(current_node, adjacent)

    print("\n\non         ", from_dir, current_node, (row, col))

    # goes through all legal paths
    for direction, dest_sym, (dr, dc) in legal_paths:
        if direction != from_dir and dest_sym != "S":
            print("Going ->   ", direction, dest_sym, (dr, dc))
            distances[dr][dc] = i
            traverse((dr, dc), distances, opposite_direction(direction), i)
            break # ensures only one direction AT THE START (should do nothing further on)


distances = [[0 for _ in _] for _ in matrix]  # list for mapping of distances

fine_print(matrix)

traverse(start, distances, "X", 0)

fine_print(distances)
