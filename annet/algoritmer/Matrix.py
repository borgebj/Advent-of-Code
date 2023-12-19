import random


class Matrix:
    def __init__(self, inp):
        self.board = []
        self.center = set()

        # int -> create inp x inp board
        if isinstance(inp, int):
            self.create_board(inp)

        # str -> blueprint of board from inp
        elif isinstance(inp, str):
            self.initiate(inp)

        # array -> create from already existing
        elif isinstance(inp, list):
            self.board = inp

        self.max_rows, self.max_cols = len(self.board), len(self.board[0])

    def initiate(self, inp):
        self.board = [line.split() for line in inp.split("\n")]

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



    # ---------- [ for game ] ----------
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
    # ---------- [ for game ] ----------


    # ---------- [ for printing ] ----------
    def print_to_html(self, output_file):
        with open(output_file, mode="w") as f:
            f.write("<html><head><style>")
            f.write(
                "body { background-color: #1E1E1E; color: #FFFFFF; padding: 20px; margin: 0; font-family: monospace; }")
            f.write("</style></head><body><pre>")

            for row in self.board:
                for i, x in enumerate(row):
                    if i < len(row) - 1:
                        f.write(f"{x} ")
                    else:
                        f.write(f"{x}<br>")
            f.write("</pre></body></html>")
    # ---------- [ for printing ] ----------


    def __str__(self):
        return self.board

    def __len__(self):
        return len(self.board)
