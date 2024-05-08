# import numpy random so it can randomly populate the board with red, black, or empty
import numpy as np
from numpy import random

# function for generating game board that takes a parameter representing the size of the board
def build_board(size):
    board = random.choice(["Empty", "Red", "Black"], size=(size, size))
    return board

# function to count how many " " are in the board
def get_count(board, target):
    # count the elements in "board" equal to target. target allows to specify what you want to count
    count = np.count_nonzero(board == target)
    return count


# check if code is running as a main

if __name__ =="__main__":
    print("File is not intended to be run as a main.")
