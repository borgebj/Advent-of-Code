# ----- matrix functions start ----- #
# ----- matrix parse -----
from typing import Tuple

with open("input", "r") as f:
    data = [[x for x in line.split()] for line in f]


# ----- matrix boundary check -----
def inside_bounds(row: int, col: int, max_rows: int, max_cols: int):
    return 0 <= row < max_rows and 0 <= col < max_cols


# ----- matrix element retriever -----
def get_coords(mat: list[list[str]], match: str) -> tuple[int, int]:
    for i, row in enumerate(mat):
        for j, elem in enumerate(row):
            if elem == match: return i, j


# ----- matrix adjacent -----
def get_adjacent(mat: list[list[str]], row: int, col: int):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  # (-1, -1), (-1, 1),(1, -1), (1, 1)
                  ]
    # Nord - Sør - Vest - Øst - Nordvest - Nordøst - Sørvest - Sørøst
    adjacent = []
    max_rows = len(mat)     # upper row boundary
    max_cols = len(mat[0])  # upper column boundary

    for dr, dc in directions:
        if inside_bounds(row + dr, col + dc, max_rows, max_cols):
            adjacent.append(mat[row + dr][col + dc])

    return adjacent


# ----- matrix functions end ----- #


# Iterative Depth-First-Search
def dfs(graph: list[list[str]], start: str) -> list[str]:
    visited = set(start)
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        row, col = get_coords(graph, node)
        result.append(node)

        for nabo in get_adjacent(graph, row, col):
            if nabo not in visited:
                visited.add(nabo)
                stack.append(nabo)

    return result


# recursive Depth-First-Search
def dfs_rec(graph, node, visited=[]):
    visited += node
    row, col = get_coords(graph, node)
    for nabo in get_adjacent(graph, row, col):
        if nabo not in visited:
            visited = dfs_rec(graph, nabo, visited)
    return visited


def main():
    res = dfs(data, "0")
    res_rec = dfs_rec(data, "0")
    print(res)
    print(res_rec)
    print(len(res), len(res_rec), len(data)*len(data[0]))


if __name__ == "__main__":
    main()
