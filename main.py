
import checkers

def game ():
    # prompt for size of board
    size = int(input("Enter a square board size between 4-16: "))
    # pass the size to the build_board function
    board = checkers.build_board(size)
    print(board)
    # count each cell occurence
    empty_count = checkers.get_count(board, "Empty")
    red_count = checkers.get_count(board, "Red")
    black_count = checkers.get_count(board, "Black")
    # print counts
    print("Empty:", empty_count)
    print("Red:", red_count)
    print("Black:", black_count)


# check if code is running as a main

if __name__ =="__main__":
    game()
