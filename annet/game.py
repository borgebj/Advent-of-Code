import random
import time

from annet.algoritmer.Matrix import Matrix

def main():
    size = int(input("Board size: "))
    board = Matrix(size)
    moves = 0

    board.place_start(size)  # places start in board
    board.place_treasure()  # places treasure somewhere
    srow, scol = board.center  # extract start coordinates

    directions = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1), "e": None}

    # game .. start!
    board.print_matrix()
    to = input("Direction (wasd): ").lower()

    while directions[to]:
        row, col = directions[to]
        row, col = srow + row, scol + col
        moves += 1

        # case: treasure found!
        if board.inside_bounds(row, col) and board.board[row][col] == "O":
            print(f'\n{"-" * 34}\nYou found the treasure in {moves} moves!\n{"-" * 34}')
            break

        # case: move in direction
        elif board.inside_bounds(row, col):
            board.swap((srow, scol), (row, col))
            srow, scol = row, col

            board.print_matrix()
            to = input("Direction: ").lower()

        # case: out of bounds
        elif not board.inside_bounds(row, col):
            print("\nOut of bounds - try again\n")
            time.sleep(1)

            board.print_matrix()
            to = input("Direction: ").lower()


if __name__ == "__main__":
    main()
