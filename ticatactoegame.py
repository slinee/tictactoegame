# Imports ---------------
from guizero import App, Box, PushButton, Text, Picture  # Here we import different modules


# Functions -------------
def clear_board():
    new_board = [[None, None, None], [None, None, None], [None, None, None]]    # initialise each variable i "none" -->
    # aka empty
    for x in range(3):
        for y in range(3):
            button = PushButton(board, text="", grid=[x, y], width=3, command=choose_square, args=[x, y])
            new_board[x][y] = button    # stores reference to each button in the 2 dimensional list

    return new_board # returns the value of the new_board variable


def choose_square(x, y):
    board_squares[x][y].text = turn     # adds text to the clicked button
    board_squares[x][y].disable()       #disables the button, so u can't click on it again
    toggle_player()
    check_win()


def toggle_player(): # just a function which lets toogles X to O and O to X
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    message.value = "It is your turn, " + turn  # displays the said text and then X or O


def check_win():    #function for checking the winner
    winner = None
    # in the functions bellow all of the patterns are checked if they are true, this is the east pythonic but the simple
    # way of how ot do this

    # Vertical lines
    if (
            board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][0]

    elif (
            board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text
    ) and board_squares[1][2].text in ["X", "O"]:
        winner = board_squares[1][0]
    elif (
            board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[2][0]

    # Horizontal lines
    elif (
            board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text
    ) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (
            board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text
    ) and board_squares[2][1].text in ["X", "O"]:
        winner = board_squares[0][1]
    elif (
            board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][2]

    # Diagonals
    elif (
            board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (
            board_squares[2][0].text == board_squares[1][1].text == board_squares[0][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][2]

    if winner is not None:
        message.value = winner.text + " wins!"
        text = Text(app, text=winner.text, size=200, color="red") # displays the winner in the big text

    elif moves_taken() == 9:
        message.value = "It's a draw"


def moves_taken():
    moves = 0
    # nested loop for finding the position of the square to check
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O": #if ther is X or O in the aquare moves variable is increased
                moves += 1
    return moves


# Variables -------------
turn = "X" # starting variable whihc is X

# App -------------------
app = App("Tic tac toe") # name of ht eapp

board = Box(app, layout="grid")     #giving the grid layout to the box
board_squares = clear_board()       # makes hte board blank
message = Text(app, text="It is your turn, " + turn)    #said meassage plus X or O
picture = Picture(app, image="tictactoe.png") # display pircure with the name tictactoe.png on the screen
text = Text(app, text="The Best Tic-Tac-Toe Game", size=30, color="red") # displays the text on the screen.

app.display()      # Displays/Runs the game