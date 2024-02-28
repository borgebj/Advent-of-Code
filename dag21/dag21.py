from collections import deque

from annet.algoritmer.Matrix import Matrix

matrix = []
start = None

with open("input", mode="r") as f:
    for i, line in enumerate(f.read().splitlines()):
        row = []
        for j, char in enumerate(line):
            if char.lower() == "s": start = (i, j)
            row.append(char)
        matrix.append(row)
    matrix = Matrix(matrix)

# Iterative Bredth-First-Search
from collections import deque


def bfs(graph, start, steps):
    queue = deque([(start, 0)])  # Each element in the queue is now a tuple (coordinates, layer)

    while queue:
        (row, col), layer = queue.popleft()

        print(f'Layer {layer}')

        if layer == steps:
            print(sum([line.count("o") for line in graph.board]))
            break

        for nabo in graph.get_adjacent(row, col, coords=True, exclude=["#"]):
            nrow, ncol = nabo
            graph.board[row][col] = "."
            graph.board[nrow][ncol] = "o"
            queue.append((nabo, layer + 1))

        graph.print_matrix()



def main():
    res = bfs(matrix, start, 6)
    print(f'(ite) From {start}: {res}')


if __name__ == "__main__":
    main()
