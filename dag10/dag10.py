
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
    print(" "+"".join("___" for _ in matrix[0]))

    for row in matrix:
        print("|" + "".join(f" {elem} " for elem in row) + "|")

    print(" "+"".join("¯¯¯" for _ in matrix[0]))


fine_print(matrix)
print(f'Start at {start if start else "No start"}')