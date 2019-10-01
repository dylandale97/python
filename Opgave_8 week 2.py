from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4

# initializing board
board = []

for x in range(BOARD_SIZE):
 board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

# start the game and printing the board
print("Let's play Battleship!")
print_board(board)

# define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)


guessL = []
won = 0

while NR_GUESSES > 0:
    tempL = [0,0]

    print('Make a guess: ')
    print('Wich row?: ')
    guessrow = int(input())
    print('Wich place?: ')
    guessplace = int(input())

    for x in guessL:
        while x[0] == guessrow and x[1] == guessplace:
            print('This value is already chosen')
            print('Wich row?: ')
            guessrow = int(input())
            print('Wich place?: ')
            guessplace = int(input())
    while guessplace<=0 or guessrow<=0 or guessplace>4 or guessrow>4:
        print('Pick a value between 0 and 4')
        print('Wich row?: ')
        guessrow = int(input())
        print('Wich place?: ')
        guessplace = int(input())

    tempL[0] = guessrow
    tempL[1] = guessplace


    if guessrow == ship_row and guessplace == ship_col:
        print('You won!')
        won = 1
        break

    for x in range(BOARD_SIZE):
        if x+1 == guessrow:
            temp = board[guessrow-1]
            temp[guessplace-1] = 'x'

    print_board(board)


    guessL.append(tempL)

    NR_GUESSES = NR_GUESSES -1



if won == 0:
    print ("Game Over")

