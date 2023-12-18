import tkinter as tk
from tkinter import messagebox
from annet.algoritmer.Matrix import Matrix

class TreasureHuntGameGUI:
    def __init__(self, size):
        self.size = size
        self.board = Matrix(size)
        self.moves = 0
        self.directions = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1), "e": None}

        self.setup_game()

    def setup_game(self):
        self.board.place_start(self.size)
        self.board.place_treasure()
        self.srow, self.scol = self.board.center

    def move(self, to):
        row, col = self.directions[to]
        row, col = self.srow + row, self.scol + col
        self.moves += 1

        if self.board.inside_bounds(row, col) and self.board.board[row][col] == "O":
            self.show_message(f'You found the treasure in {self.moves} moves!')
            self.reset_game()
        elif self.board.inside_bounds(row, col):
            self.board.swap((self.srow, self.scol), (row, col))
            self.srow, self.scol = row, col
            self.draw_board()
        else:
            self.show_message("Out of bounds - try again")

    def reset_game(self):
        self.moves = 0
        self.board = Matrix(self.size)  # Create a new matrix object
        self.setup_game()
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 30

        for i, row in enumerate(self.board.board):
            for j, cell in enumerate(row):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size

                if cell == ".":
                    color = "white"
                elif cell == "X":
                    color = "gray"
                elif cell == "O":
                    color = "gold"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

        self.canvas.update()

    def show_message(self, message):
        self.draw_board()
        self.root.withdraw()
        messagebox.showinfo("Game Over", message)
        self.reset_game()
        self.root.deiconify()

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up":
            self.move("w")
        elif key == "Down":
            self.move("s")
        elif key == "Left":
            self.move("a")
        elif key == "Right":
            self.move("d")

    def run_gui(self):
        self.root = tk.Tk()
        self.root.title("Treasure Hunt Game")

        self.canvas = tk.Canvas(self.root, width=self.size * 30, height=self.size * 30, bg="white")
        self.canvas.pack()

        frame = tk.Frame(self.root)
        frame.pack()

        button_up = tk.Button(frame, text="Up", command=lambda: self.move("w"))
        button_up.grid(row=0, column=1)

        button_left = tk.Button(frame, text="Left", command=lambda: self.move("a"))
        button_left.grid(row=1, column=0)

        button_down = tk.Button(frame, text="Down", command=lambda: self.move("s"))
        button_down.grid(row=1, column=1)

        button_right = tk.Button(frame, text="Right", command=lambda: self.move("d"))
        button_right.grid(row=1, column=2)

        self.draw_board()

        self.root.bind("<Up>", self.on_key_press)
        self.root.bind("<Down>", self.on_key_press)
        self.root.bind("<Left>", self.on_key_press)
        self.root.bind("<Right>", self.on_key_press)

        self.root.mainloop()

if __name__ == "__main__":
    size = int(input("Board size: "))
    game = TreasureHuntGameGUI(size)
    game.run_gui()
