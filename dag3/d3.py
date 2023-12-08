with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


def create_matrix(dat: list[str]) -> list[list[str]]:
    return [[s for s in line] for line in dat]


def inside_bounds(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


def get_adjacent(mat, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    return [mat[row + dr][col + dc] for dr, dc in directions
            if inside_bounds(row + dr, col + dc, len(mat), len(mat[0]))]


def find_symbol(mat):
    return {(i, j): get_adjacent(mat, i, j)
            for i, row in enumerate(mat)
            for j, symbol in enumerate(row)
            if not symbol.isdigit() and symbol != "."}


def get_full_number(mat, i, j):
    left = mat[i][:j]  # gets left of val
    right = mat[i][j + 1:]  # gets right of val

    left_digits = ''.join(left).split('.')[-1] if left and left[-1].isdigit() else ''  # only digits left
    right_digits = ''.join(right).split(".")[0] if right and right[0].isdigit() else ''  # only digits right

    return left_digits, mat[i][j], right_digits  # the whole number and skips


def find_part_numbers(mat):
    all_nums = []
    cols = len(mat[0])

    for i, line in enumerate(mat):
        j = 0
        while j < cols:
            adj = get_adjacent(mat, i, j)
            valid = any(not s.isdigit() and s != "." and s != "\n" for s in adj)

            if not mat[i][j].isdigit() and mat[i][j] != ".":
                adj = get_adjacent(mat, i, j)
                print("Symbol:", i, j, mat[i][j], "adj:", adj)

            if valid and mat[i][j].isdigit():
                left, mid, right = get_full_number(mat, i, j)
                full_number = int(left+mid+right)
                all_nums.append(full_number)

                j += len(right) + 1  # Move to the next element after the modified segment
            else:
                j += 1

    return sum(all_nums)


def part_sums(nums):
    print(f'Sum of all part numbers are {sum(nums)}')


matrix = create_matrix(data)
nums = find_part_numbers(matrix)
print(f'Sum of all part numbers: {nums}')
