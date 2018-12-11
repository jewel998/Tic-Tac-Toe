# CS-UY 1114
# Final project

from turtle import *
import turtle
import time
import random

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.

# For the moves
n = [0]

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
hideturtle()
def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.setheading(0)
    turtle.clear()
    pencolor("black")
    title("Tic-Tac-Toe")
    setup(600, 600)
    speed(10)
    turtle.pu()
    turtle.pensize(10)

    goto(-300, 100)
    turtle.pendown()
    forward(600)
    turtle.penup()
    goto(-300, -100)
    turtle.pendown()
    forward(600)
    up()

    goto(-100, 300)
    setheading(-90)
    down()
    forward(600)
    up()
    goto(100, 300)
    down()
    forward(600)
    up()
    turtle.update()

"""

def getRow(y):
    row1 = (105, 300)
    row2 = (-95, 95)
    row3 = (-300, -105)
    rows = [row1, row2, row3]
    row = 0
    for y1, y2 in rows:
        if y > y1 and y < y2:
            return row
        else:
            row += 1

def getColumn(x):
    column1 = (-300, -105)
    column2 = (-95, 95)
    column3 = (105, 300)
    columns = [column1, column2, column3]
    column = 0
    for x1, x2 in rows:
        if x > x1 and x < x2:
            return column
        else:
            column += 1

"""

def getPosition(x, y):
    #coordinates = [(xmin, xmax, ymin, ymax), (xmin, xmax, ymin, ymax), etc.]
    
    coordinates = [(-300, -105, 105, 300), (-95, 95, 105, 300), (105, 300, 105, 300),
                   (-300, -105, -95, 95), (-95, 95, -95, 95), (105, 300, -95, 95),
                   (-300, -105, -300, -105), (-95, 95, -300, -105), (105, 300, -300, -105)]
    square = 0
    for (xmin, xmax, ymin, ymax) in coordinates:
        if (x > xmin and x < xmax) and (y > ymin and y < ymax):
            return square
        square += 1
        
    

def checkEmpty(board):
    emptyPosition = 0
    emptySquares = []
    for square in board:
        if square == "_":
            emptySquares.append(emptyPosition)
            emptyPosition += 1
        else:
            emptyPosition += 1
    return emptySquares

def cross(x, y):    # function to draw a cross
    up()
    goto(x + 20, y - 20)
    setheading(-45)
    down()
    forward(226)
    up()
    goto(x + 180, y - 20)
    setheading(-135)
    down()
    forward(226)
    up()

def nought(x, y):   #function to draw a nought
    up()
    goto(x + 100, y - 180)
    setheading(0)
    down()
    circle(80)
    up()

def drawPieces(pieces): 
    x = -300
    y = 300
    for piece in pieces:
        if piece == "X":
            cross(x, y)
        elif piece == "O":
            nought(x, y)
        x = x + 200
        if x > 100:
            x = -300
            y = y - 200


def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    emptySquares = checkEmpty(board)
    position = getPosition(x, y)
    counter = 0
    for square in emptySquares:
        if square == position:
            board[position] = "O"
            print("User Move:")
            return True
        elif counter == len(emptySquares):
            return False
        else:
            counter += 1
    drawPieces(board)

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    if (the_board[0] == "O" and the_board[1] == "O" and the_board[2] == "O")\
        or (the_board[3] == "O" and the_board[4] == "O" and the_board[5] == "O")\
        or (the_board[6] == "O" and the_board[7] == "O" and the_board[8] == "O")\
        or (the_board[0] == "O" and the_board[3] == "O" and the_board[6] == "O")\
        or (the_board[1] == "O" and the_board[4] == "O" and the_board[7] == "O")\
        or (the_board[2] == "O" and the_board[5] == "O" and the_board[8] == "O")\
        or (the_board[0] == "O" and the_board[4] == "O" and the_board[8] == "O")\
        or (the_board[6] == "O" and the_board[4] == "O" and the_board[2] == "O"):
            print("User wins!")
            pass
    elif (the_board[0] == "X" and the_board[1] == "X" and the_board[2] == "X")\
        or (the_board[3] == "X" and the_board[4] == "X" and the_board[5] == "X")\
        or (the_board[6] == "X" and the_board[7] == "X" and the_board[8] == "X")\
        or (the_board[0] == "X" and the_board[3] == "X" and the_board[6] == "X")\
        or (the_board[1] == "X" and the_board[4] == "X" and the_board[7] == "X")\
        or (the_board[2] == "X" and the_board[5] == "X" and the_board[8] == "X")\
        or (the_board[0] == "X" and the_board[4] == "X" and the_board[8] == "X")\
        or (the_board[6] == "X" and the_board[4] == "X" and the_board[2] == "X"):
            print("Computer wins!")
    check = 0
    for i in range(9):
        if board[i] == "X" or board[i] == "O":
            check = check + 1
    if check == 9:
        print("Stalemate: Clearing Board")
        clearBoard(board)

def clearBoard(board):
    for i in range(9):
        board[i] = "_"
    n[0] = 0

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    print("Computer Move:")
    #win_horizontal
    if board[0] == "X" and board[1] == "X" and board[2] == "_" :
        the_board[2] = "X"
    elif board[0] == "X" and board[2] == "X" and board[1] == "_":
        the_board[1] = "X"
    elif board[1] == "X" and board[2] == "X" and board[0] == "_" :
        the_board[0] = "X"
    
    elif board[3] == "X" and board[4] == "X" and board[5] == "_" :
        the_board[5] = "X"
    elif board[3] == "X" and board[5] == "X" and board[4] == "_" :
        the_board[4] = "X"
    elif board[4] == "X" and board[5] == "X" and board[3] == "_" :
        the_board[3] = "X"
    
    elif board[6] == "X" and board[7] == "X" and board[8] == "_" :
        the_board[8] = "X"
    elif board[6] == "X" and board[8] == "X" and board[7] == "_" :
        the_board[7] = "X"
    elif board[7] == "X" and board[8] == "X" and board[6] == "_" :
        the_board[6] = "X" 
    
    #win_vertical 
    elif board[0] == "X" and board[3] == "X" and board[6] == "_" :
        the_board[6] = "X"
    elif board[0] == "X" and board[6] == "X" and board[0] == "_" :
        the_board[3] = "X"
    elif board[3] == "X" and board[6] == "X" and board[3] == "_" :
        the_board[0] = "X"
    
    elif board[1] == "X" and board[4] == "X" and board[7] == "_" :
        the_board[7] = "X"
    elif board[1] == "X" and board[7] == "X" and board[4] == "_" :
        the_board[4] = "X"
    elif board[4] == "X" and board[7] == "X" and board[1] == "_" :
        the_board[1] = "X"
    
    elif board[2] == "X" and board[5] == "X" and board[8] == "_" :
        the_board[8] = "X"
    elif board[2] == "X" and board[8] == "X" and board[5] == "_" :
        the_board[5] = "X"
    elif board[5] == "X" and board[8] == "X" and board[2] == "_" :
        the_board[2] = "X"    
    
    #win_diagonal
    elif board[0] == "X" and board[4] == "X" and board[8] == "_" :
        the_board[8] = "X"
    elif board[0] == "X" and board[8] == "X" and board[4] == "_" :
        the_board[4] = "X"
    elif board[4] == "X" and board[8] == "X" and board[0] == "_" :
        the_board[0] = "X"
        
    elif board[2] == "X" and board[6] == "X" and board[4] == "_" :
        the_board[4] = "X"
    elif board[2] == "X" and board[4] == "X" and board[6] == "_":
        the_board[6] = "X"
    elif board[4] == "X" and board[6] == "X" and board[2] == "_":
        the_board[2] = "X"   
    
    #block_vertical
    elif board[0] == "O" and board[3] == "O" and board[6] == "_":
        the_board[6] = "X"
    elif board[0] == "O" and board[6] == "O" and board[3] == "_":
        the_board[3] = "X"
    elif board[3] == "O" and board[6] == "O" and board[0] == "_":
        the_board[0] = "X"
    
    elif board[1] == "O" and board[4] == "O" and board[7] == "_":
        the_board[7] = "X"
    elif board[1] == "O" and board[7] == "O" and board[4] == "_":
        the_board[4] = "X"
    elif board[4] == "O" and board[7] == "O" and board[1] == "_":
        the_board[1] = "X"
    
    elif board[2] == "O" and board[5] == "O" and board[8] == "_":
        the_board[8] = "X"
    elif board[2] == "O" and board[8] == "O" and board[5] == "_":
        the_board[5] = "X"
    elif board[5] == "O" and board[8] == "O" and board[2] == "_":
        the_board[2] = "X" 

    #block_horizontal
    elif board[0] == "O" and board[1] == "O" and board[2] == "_":
        the_board[2] = "X"
    elif board[0] == "O" and board[2] == "O" and board[1] == "_":
        the_board[1] = "X"
    elif board[1] == "O" and board[2] == "O" and board[0] == "_":
        the_board[0] = "X"
    
    elif board[3] == "O" and board[4] == "O" and board[5] == "_":
        the_board[5] = "X"
    elif board[3] == "O" and board[5] == "O" and board[4] == "_":
        the_board[4] = "X"
    elif board[4] == "O" and board[5] == "O" and board[3] == "_":
        the_board[3] = "X"

    elif board[6] == "O" and board[7] == "O" and board[8] == "_":
        the_board[8] = "X"
    elif board[6] == "O" and board[8] == "O" and board[7] == "_":
        the_board[7] = "X"
    elif board[7] == "O" and board[8] == "O" and board[6] == "_":
        the_board[6] = "X"
    
    #block_diagonal
    elif board[2] == "O" and board[4] == "O" and board[6] == "_":
        the_board[6] = "X"
    elif board[2] == "O" and board[6] == "O" and board[4] == "_":
        the_board[4] = "X"
    elif board[4] == "O" and board[6] == "O" and board[2] == "_":
        the_board[2] = "X"
        
    elif board[0] == "O" and board[4] == "O" and board[8] == "_":
        the_board[8] = "X"
    elif board[0] == "O" and board[8] == "O" and board[4] == "_":
        the_board[4] = "X"
    elif board[4] == "O" and board[8] == "O" and board[0] == "_":
        the_board[0] = "X"

    #first random choice
    elif n[0] == 1:
        done = 0
        while done != 1:
            x = random.randint(0,8)
            if board[x] == "_":
                board[x] = "X"
                done = 1
                break
    #corner
    elif board[2] == "_":
        the_board[2] = "X"
    elif board[6] == "_":
        the_board[6] = "X"
    elif board[8] == "_":
        the_board[8] = "X"
    elif board[0] == "_":
        the_board[0] = "X"
    #center
    elif board[4] == "_":
        the_board[4] = "X"
    #sides
    elif board[1] == "_":
        the_board[1] = "X"
    elif board[3] == "_":
        the_board[3] = "X"
    elif board[5] == "_":
        the_board[5] = "X"
    elif board[7] == "_":
        the_board[7] = "X"

    pass



def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            n[0] = n[0] + 1
            do_computer_move(the_board)
            n[0] = n[0] + 1
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
