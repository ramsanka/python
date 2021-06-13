import random

#display the board.

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-+')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-+')
    print(board[1] + '|' + board[2] + '|' + board[3])

#letting the player choose
#returns the player letter first/ computer second.
def inputPlayerletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("you can select only X or O")
        letter = input().upper()

    if letter == 'X':
        return['X','O']
    elif letter == 'O':
        return['O','X']

#use rand to figure out who goes first.
def first():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'



#placing a mark on the board.
#we make references to list. dict.
def makeaMove(board, letter, move):
    board[move] = letter


#how to check if it winner.
#list down all the combination.
def isWinner(bo, le):
    return((bo[7] == le and bo[8] == le and bo[9] == le) or
           (bo[4] == le and bo[5] == le and bo[6] == le) or
           (bo[1] == le and bo[2] == le and bo[3] == le) or
           (bo[7] == le and bo[4] == le and bo[1] == le) or
           (bo[8] == le and bo[8] == le and bo[2] == le) or
           (bo[9] == le and bo[6] == le and bo[3] == le) or 
           (bo[7] == le and bo[5] == le and bo[3] == le) or
           (bo[9] == le and bo[5] == le and bo[1] == le))


#make a copy of the board
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


#checking if there is space in the board.
def isSpaceFree(board, move):
    return board[move] == ' '


#letting the player make a move
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move(1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movelist):
    possibleMoves = []
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:   
        return None

def getComputerMove(board, computerLetter):
    if computerLetter  == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeaMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    if isSpaceFree(board,5):
        return 5

    return chooseRandomMoveFromList(board, [2,4,6,8])


def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True


print('welcome to tic tac toe game')


while True:
    theboard = [' '] * 10
    playletter, computerletter = inputPlayerletter()
    turn = first()

    print('the ' + turn + 'will go first')
    gameplaying = True


    while gameplaying:
        if turn == 'player':
            drawBoard(theboard)
            move = getPlayerMove(theboard)
            makeaMove(theboard, playletter, move)

            if isWinner(theboard, playletter):
                drawBoard(theboard)
                print('the winner is the player')
                gameplaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('the game is a tie')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theboard, computerletter)
            makeaMove(theboard, computerletter, move)

            if isWinner(theboard, computerletter):
                drawBoard(theboard)
                print('the winner is the computer')
                gameplaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('the game is a tie')
                    break
                else:
                    turn = 'player'

    print('do you want to continue')
    if input().lower().startswith('y'):
        print('game on')
    else:
        print('good bye')
        break

