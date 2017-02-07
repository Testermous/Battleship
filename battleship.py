#Created by Dan 'Testermous' Testerman

#Need to add:  multiple ships, a way to resart a finished game,
#              error check user input, ships with varing sizes,
#              when printing the board include user readable row and col nunbers

from random import randint

class Board:
    def __int__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
    for x in range(self.rows):  #Number of rows
        self.board.append(["O"] * self.cols)  #Number of cols
    def print_board(board):
        for row in board:
            print(" ".join(row))

Board(10, 10)
print("Let's play Battleship!")
print("Use the numbers 1 through 10 for location commands.")
print("You have 7 chances.")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Maybe convert everything below this into a function or two
for turn in range(7):
    inputRow = input("Guess Row:")
    guessRow = int(inputRow)
    inputCol = input("Guess Col:")
    guessCol = int(inputCol)

    #Convert user commands to board comands
    guessCol = guessCol - 1
    if guessRow == 10:
        guessRow = 0
    elif guessRow == 9:
        guessRow = 1
    elif guessRow == 8:
        guessRow = 2
    elif guessRow == 7:
        guessRow = 3
    elif guessRow == 6:
        guessRow = 4
    elif guessRow == 5:  #redundent try something different
        guessRow = 5
    elif guessRow == 4:
        guessRow = 6
    elif guessRow == 3:
        guessRow = 7
    elif guessRow == 2:
        guessRow = 8
    elif guessRow == 1:
        guessRow = 9
    else:                #have a way for it to loop back into taking the input for guessRow
        print("That is not a valid command.")
        print("Try again")

    if guessRow == ship_row and guessCol == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guessRow][guessCol] = "B"
        print_board(board)
        break
    else:
        if (guessRow < 0 or guessRow > 9) or (guessCol < 0 or guessCol > 9):  #Checks converted input to see if it is still on board.
            print("Oops, that's not even in the ocean.")
        elif(board[guessRow][guessCol] == "X"):
            print("You guessed that one already.")
        else:   
            print("You missed my battleship!")
            board[guessRow][guessCol] = "X"
            if turn == 4:
                print("Game Over")
        print(6-turn, " tries left")
        print_board(board)
