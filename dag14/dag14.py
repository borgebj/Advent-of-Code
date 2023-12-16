import time
from tqdm import tqdm

# parsing
with open("input.txt", "r") as f:
    data = [[x for x in line.strip()] for line in f]


# print a nice matrix in terminal
def print_matrix(matrix):
    print()
    [print(f'{len(data) - i:2}: {" ".join(row)}') for i, row in enumerate(matrix)]
    print()


def inside_bounds(row, col, max_rows, max_cols):
    return 0 <= row < max_rows and 0 <= col < max_cols


# tilts the matrix to specific direction
def tilt(data, direction):
    max_rows = len(data)
    max_cols = len(data[0])
    moved = True

    # swaps direction so element is moved. e.g: O . . -> . O . -> . . O
    def swap_direction(i, j, new_i, new_j):
        if inside_bounds(new_i, new_j, max_rows, max_cols) and data[new_i][new_j] == ".":
            data[new_i][new_j], data[i][j] = data[i][j], data[new_i][new_j]
            return True
        return False

    # tilt based on direction
    while moved:
        moved = False

        for i in range(max_rows):
            for j in range(max_cols):
                if data[i][j] == "O":
                    if direction == "N" and swap_direction(i, j, i - 1, j):
                        moved = True
                    elif direction == "W" and swap_direction(i, j, i, j - 1):
                        moved = True
                    elif direction == "S" and swap_direction(i, j, i + 1, j):
                        moved = True
                    elif direction == "E" and swap_direction(i, j, i, j + 1):
                        moved = True

    return data


# IDE:
# etter mange sykler vil det komme et mønster med de samme 4 tallene over og over igjen
# fang disse og stop når mønstre gjentar seg

# tilts in cycles (part 2)
def tilt_cycle(data, cycles):
    directions = ["N", "W", "S", "E"]
    end_direction = directions[(cycles - 1) % 4]

    print("end up on:", end_direction)

    # for _ in range(cycles):
    for _ in tqdm(range(cycles), desc="Tilting", unit="cycle", disable=True):
        direction = directions[_ % 4]

        data = tilt(data, direction)
        weights = sum([(row.count("O") * (len(row) - i)) for i, row in enumerate(data)])

        if _ % 4 == 0: time.sleep(1)

        print(f'{_ + 1}: {weights} {direction}')
        if direction == "E": print()


    return data


cycles = int(input("Cycles: "))

# time-measure
start = time.time()
data = tilt_cycle(data, cycles)
time_taken = time.time() - start

# counts the sum of number of O's on each row times the row number reversed
weights = sum([(row.count("O") * (len(row) - i)) for i, row in enumerate(data)])

# prints part 1 or part 2 based on cycles
print(f'Weights {"part 1" if cycles == 1 else "part 2"} = {weights}, took {time_taken}s')
