matrix = []
start = None

with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.read().splitlines()):
        row = []
        for j, char in enumerate(line):
            if char.lower() == "s": start = (i, j)
            row.append(char)
        matrix.append(row)

# initialize distance-matrix
distances = [[0 for _ in _] for _ in matrix]  # list for mapping of distances


# fine-prints a 2D array into a nice HTML with color
def fine_print_to_html(matrix, output_file):
    with open(output_file, mode="w") as f:
        f.write("<html><head><style>")
        f.write("body { background-color: #1E1E1E; color: #FFFFFF; padding: 20px; margin: 0; font-family: monospace; }")
        f.write(".green { color: #00FF00; }")
        f.write(".red { color: #FF0000; }")  # Change to red or another color of your choice
        f.write("</style></head><body><pre>")

        rows, cols = len(matrix), len(matrix[0])
        max_width = max(len(str(matrix[i][j])) for i in range(rows) for j in range(cols)) + 1

        f.write("    " + " ".join(f"{i:>{max_width}}" for i in range(cols)) + "<br>")
        f.write("   " + "-" * (max_width * cols + 4) + "---" * max_width + "<br>")

        for i, row in enumerate(matrix):
            f.write(f"{i:>{max_width}} |")
            for j, elem in enumerate(row):
                if (elem != 0 and elem != "O") and elem != "." or (i, j) == start:
                    f.write(f"<span class='green'>{elem:>{max_width}}</span> ")
                elif elem == 0:
                    f.write(f"<span class='red'>{elem:>{max_width}}</span> ")
                else:
                    f.write(f"{elem:>{max_width}} ")
            f.write("<br>")
        f.write("</pre></body></html>")


def inside_bounds(row, col, max_rows, max_cols):
    return 0 <= row < max_rows and 0 <= col < max_cols


def get_adjacent(row, col):
    directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    row_len, col_len = len(matrix), len(matrix[0])

    adjacant = []

    for direction, (dr, dc) in directions.items():
        if inside_bounds(row + dr, col + dc, row_len, col_len):
            adjacant.append((direction, matrix[row + dr][col + dc], (row + dr, col + dc)))

    return adjacant


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


# traverse iteratively - works better than the recursive
def traverse_dfs(matrix, start, distances):
    stack = [(start, "X", 0)]  # Start node, direction, and distance   | DFS = stack BFS = queue
    while stack:
        (row, col), from_dir, i = stack.pop()  # DFS = stack.pop BFS = queue.pop(0)

        # gets all legal paths
        adjacent = get_adjacent(row, col)
        legal_paths = get_legal_paths(matrix[row][col], adjacent)

        # goes through all legal paths
        for direction, dest_sym, (dr, dc) in legal_paths:
            # don't go back to previous
            if direction != from_dir and dest_sym != "S":
                # stops at start / halfway on second loop
                if distances[dr][dc] == 0 or distances[dr][dc] > i + 1:
                    distances[dr][dc] = i + 1
                    stack.append(((dr, dc), opposite_direction(direction), i + 1))


def flood_fill(matrix, row, col, fill_value):
    stack = [(row, col)]

    while stack:
        current_row, current_col = stack.pop()

        if 0 <= current_row < len(matrix) and 0 <= current_col < len(matrix[0]) and not matrix[current_row][
            current_col]:
            matrix[current_row][current_col] = fill_value

            stack.append((current_row - 1, current_col))  # North
            stack.append((current_row + 1, current_col))  # South
            stack.append((current_row, current_col - 1))  # West
            stack.append((current_row, current_col + 1))  # East
            stack.append((current_row - 1, current_col - 1))  # Northwest
            stack.append((current_row - 1, current_col + 1))  # Northeast
            stack.append((current_row + 1, current_col - 1))  # Southwest
            stack.append((current_row + 1, current_col + 1))  # Southeast


def fill_corners(matrix, fill_value):
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1

    # flood-fills every corner
    flood_fill(matrix, 0, 0, fill_value)  # top left
    flood_fill(matrix, 0, max_col - 1, fill_value)  # top right
    flood_fill(matrix, max_row - 1, 0, fill_value)  # bottom left
    flood_fill(matrix, max_row - 1, max_col - 1, fill_value)  # bottom right


def expand(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with expanded dimensions
    new_matrix = [[0] * (cols + 4) for _ in range(rows + 4)]

    # Copy values from the original matrix to the new matrix
    for i in range(rows):
        for j in range(cols):
            new_matrix[i + 1][j + 1] = matrix[i][j]

    return new_matrix


# ---------------------------------------------------------------------------------------------------------------------
# start of task-processing
# ---------------------------------------------------------------------------------------------------------------------

# traversal start
traverse_dfs(matrix, start, distances)

# expands and fills distances
distances = expand(distances)
fill_corners(distances, "O")

# part 1  -  finds highest value in 2D array
result = max(map(lambda row: max((value for value in row if isinstance(value, int)), default=0), distances))
print(f'Furthest distance: {result}')

# part 2  -  counts all zeroes in distances
zero_values = len([x for row in distances for x in row if x == 0])  # counts all zeroes that are left (within the loop)
print(f'Tiles within the loop: {zero_values}')

# prints labyrinth to HTML
fine_print_to_html(distances, "distances.html")




















# old recursive traversal - recursion too deep for task :(

# # good in theory, but the recursion just goes too deep ...
# def traverse_rec(from_sym, distances, from_dir, i):
#     # retrieves info on current node
#     row, col = from_sym
#     from_node = matrix[row][col]
#
#     # base case
#     if from_node.lower() == "s" and distances[row][col] != 0:
#         return
#
#     # gets all legal paths
#     adjacent = get_adjacent(row, col)
#     legal_paths = get_legal_paths(from_node, adjacent)
#
#     # goes through all legal paths
#     for direction, dest_sym, (dr, dc) in legal_paths:
#         if direction != from_dir and dest_sym != "S":
#             if distances[dr][dc] == 0 or distances[dr][dc] > i + 1:
#                 distances[dr][dc] = i + 1
#                 traverse_rec((dr, dc), distances, opposite_direction(direction), i + 1)
