# ----- matrix functions start ----- #
# ----- matrix parse -----
from annet.algoritmer.Matrix import Matrix

# creates matrix using matrix-class
with open("input", "r") as f:
    data = Matrix(f.read())

# ----- matrix element retriever -----
def get_coords(mat: Matrix, match: str) -> tuple[int, int]:
    for i, row in enumerate(mat.board):
        for j, elem in enumerate(row):
            if elem == match: return i, j
# ----- matrix functions end ----- #


# Iterative Depth-First-Search
def dfs(graph: Matrix, start: str) -> list[str]:
    visited = set(start)
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        row, col = get_coords(graph, node)
        result.append(node)

        for nabo in graph.get_adjacent(row, col):
            if nabo not in visited:
                visited.add(nabo)
                stack.append(nabo)

    return result


# recursive Depth-First-Search
def dfs_rec(graph, node, visited=[]):
    visited += node
    row, col = get_coords(graph, node)

    for nabo in graph.get_adjacent(row, col):
        if nabo not in visited:
            visited = dfs_rec(graph, nabo, visited)
    return visited


def main():
    start = '0'
    res = dfs(data, start)
    rec_res = dfs_rec(data, start)
    print(f'(ite) From {start}: {res}')
    print(f'(rec) From {start}: {rec_res}')
    print(f'Size ite: {len(res)} size rec {len(rec_res)} dimensions {data.max_rows} * {data.max_cols}')


if __name__ == "__main__":
    main()
