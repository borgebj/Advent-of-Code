import random


class matrix:
    def __init__(self, inp):
        self.board = []
        self.center = set()

        # int -> create inp x inp board
        if isinstance(inp, int):
            self.create_board(inp)

        # str -> blueprint of board from inp
        elif isinstance(inp, str):
            self.initiate(inp)

        self.max_rows, self.max_cols = len(self.board), len(self.board[0])

    def initiate(self, inp):
        self.board = [[x for x in line.strip()] for line in inp]

    def create_board(self, size):
        self.board = [["." for _ in range(size)] for _ in range(size)]

    def inside_bounds(self, row: int, col: int):
        return 0 <= row < self.max_rows and 0 <= col < self.max_cols

    def get_adjacent(self, row: int, col: int):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      # (-1, -1), (-1, 1),(1, -1), (1, 1)
                      ]
        # Nord - Sør - Vest - Øst - Nordvest - Nordøst - Sørvest - Sørøst
        adjacent = []

        for dr, dc in directions:
            if self.inside_bounds(row + dr, col + dc):
                adjacent.append(self.board[row + dr][col + dc])

        return adjacent

    # for game
    def place_treasure(self):
        srow, scol = self.center
        i, j = -1, -1

        # find valid index
        while not self.inside_bounds(i, j) or (i, j) == (srow, scol):
            i, j = random.randint(0, self.max_rows - 1), random.randint(0, self.max_cols - 1)

        self.board[i][j] = "O"

    def place_start(self, size):
        center = size // 2
        self.board[center][center] = "X"
        self.center = center, center

    def print_matrix(self):
        print("\n+" + "-" * (3 * len(self.board[0])) + "+")
        for row in self.board:
            print("| " + "  ".join(row) + " |")
        print("+" + "-" * (3 * len(self.board[0])) + "+\n")

    def swap(self, first, second):
        a, b = first
        c, d = second
        self.board[a][b], self.board[c][d] = self.board[c][d], self.board[a][b]