# TIC-TAC-TOE
# Classic board game, where player can choose to play against human opponent or against the computer.
# Computer opponent comes with 3 difficulties (Easy, Medium and Hard)

import random
import os


# 3x3 board is marked with numbers 1-9
#             1|2|3
#             -+-+-
#             4|5|6
#             -+-+-
#             7|8|9
# Players are given usual TicTacToe game symbols X and O, which are used in string representation of the board,
# and blank variable is used for string representation of the blank field.

board_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X, O, blank = 'X', 'O', ' '


# main function of the game
def main():
    # initialization of opponent, difficulty and blank game board
    print ("Welcome to Tic-Tac-Toe board game!\n")
    print("1. Humas VS Human\n2. Human VS Computer ?")
    choice = int(input("> "))
    if choice == 2:
        difficulty = int(input("Choose difficulty:\n1. Easy | 2. Medium | 3. Hard \n> "))
    gameboard = getBlankBoard()
    currentPlayer, nextPlayer = X, O
    turn_counter = 0
    player_turn = True

    while True:
        turn_counter +=1
        os.system('cls')
        print(getBoardStr(gameboard))
        move = None

        # determining move according to the selected difficulty
        if choice == 2 and not player_turn:
            if difficulty == 1:
                move = random.choice(board_spaces)      # Easy (random empty field)
            elif difficulty == 2:
                move = medium(gameboard, nextPlayer)
            elif difficulty == 3:
                move = hard(gameboard, nextPlayer)
            player_turn = True
        
        # if the move is not valid, player will be asked to input it again
        while not isValid(move):
            move = int(input('> '))
            player_turn = False
        
        # updateing the game board
        updateBoard(gameboard, currentPlayer, move)
        
        # if there is less than 5 moves, there is no need to check for the winner
        if turn_counter > 4:
            if isWinner(gameboard, currentPlayer):
                print(getBoardStr(gameboard))
                print('Player {} has won the game!'.format(currentPlayer))
                if input("New game (Y/N)? > ").lower() == 'n':
                    break
                else:
                    # reseting the counter and the game board
                    turn_counter = 0
                    gameboard = getBlankBoard()

            # if 9th turn is finished, and there is no winner, game is a tie        
            elif turn_counter == 9:
                print('Board is full! Game is a tie!')
                print(getBoardStr(gameboard))
                if input("New game (Y/N)? > ").lower() == 'n':
                    break
                else:
                    # reseting the counter and the game board
                    turn_counter = 0
                    gameboard = getBlankBoard()

        # switching players turn
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    

# function used to get the blank board for a new game
def getBlankBoard():
    # all board spaces become available to play again
    global board_spaces
    board_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # initializing board as a dictionary and making all spaces blank
    board = {}
    for space in board_spaces:
        board[space] = blank
    return board



# function to get string representation of the board
def getBoardStr(board):
    return '''
    {}|{}|{}   1 2 3
    -+-+-
    {}|{}|{}   4 5 6
    -+-+-
    {}|{}|{}   7 8 9'''.format(board[1], board[2], board[3],
                               board[4], board[5], board[6],
                               board[7], board[8], board[9])



# updating game board with player's sign and move
def updateBoard(board, player, move):
    board[move] = player
    # used space becomes unavailable to play
    # (helps with faster move choice when playing against computer)
    board_spaces.remove(move)
    
    

# determining if the move is valid 
def isValid(move):
    return move in board_spaces


# determining if there is a winner
def isWinner(board, player):
    return ((board[1] == board[2] == board[3] == player) or
            (board[4] == board[5] == board[6] == player) or
            (board[7] == board[8] == board[9] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[3] == board[6] == board[9] == player) or
            (board[1] == board[5] == board[9] == player) or
            (board[3] == board[5] == board[7] == player))



# determining a computer move in medium difficulty
def medium(board, player):
    if board[1] == board[2] == player and board[3] == blank: 
        return 3
    elif board[2] == board[3] == player and board[1] == blank:
        return 1
    elif board[1] == board[3] == player and board[2] == blank:
        return 2
    elif board[4] == board[5] == player and board[6] == blank:
        return 6
    elif board[5] == board[6] == player and board[4] == blank:
        return 4
    elif board[4] == board[6] == player and board[5] == blank:
        return 5
    elif board[7] == board[8] == player and board[9] == blank:
        return 9
    elif board[8] == board[9] == player and board[7] == blank:
        return 7
    elif board[7] == board[9] == player and board[8] == blank:
        return 8
    elif board[1] == board[4] == player and board[7] == blank:
        return 7
    elif board[4] == board[7] == player and board[1] == blank:
        return 1
    elif board[1] == board[7] == player and board[4] == blank:
        return 4
    elif board[2] == board[5] == player and board[8] == blank:
        return 8
    elif board[5] == board[8] == player and board[2] == blank:
        return 2
    elif board[2] == board[8] == player and board[5] == blank:
        return 5
    elif board[3] == board[6] == player and board[9] == blank:
        return 9
    elif board[6] == board[9] == player and board[3] == blank:
        return 3
    elif board[3] == board[9] == player and board[6] == blank:
        return 6
    elif board[1] == board[5] == player and board[9] == blank:
        return 9
    elif board[5] == board[9] == player and board[1] == blank:
        return 1
    elif board[1] == board[9] == player and board[5] == blank:
        return 5
    elif board[3] == board[5] == player and board[7] == blank:
        return 7
    elif board[5] == board[7] == player and board[3] == blank:
        return 3
    elif board[3] == board[7] == player and board[5] == blank:
        return 5
    else:
        return random.choice(board_spaces)
    


# determining computer move in hard difficulty
def hard(board, player):
    if player == "X":
        computer = "O"
    else: 
        computer = "X"
    
    if board[1] == board[2] == computer and board[3] == blank: 
        return 3
    elif board[2] == board[3] == computer and board[1] == blank:
        return 1
    elif board[1] == board[3] == computer and board[2] == blank:
        return 2
    elif board[4] == board[5] == computer and board[6] == blank:
        return 6
    elif board[5] == board[6] == computer and board[4] == blank:
        return 4
    elif board[4] == board[6] == computer and board[5] == blank:
        return 5
    elif board[7] == board[8] == computer and board[9] == blank:
        return 9
    elif board[8] == board[9] == computer and board[7] == blank:
        return 7
    elif board[7] == board[9] == computer and board[8] == blank:
        return 8
    elif board[1] == board[4] == computer and board[7] == blank:
        return 7
    elif board[4] == board[7] == computer and board[1] == blank:
        return 1
    elif board[1] == board[7] == computer and board[4] == blank:
        return 4
    elif board[2] == board[5] == computer and board[8] == blank:
        return 8
    elif board[5] == board[8] == computer and board[2] == blank:
        return 2
    elif board[2] == board[8] == computer and board[5] == blank:
        return 5
    elif board[3] == board[6] == computer and board[9] == blank:
        return 9
    elif board[6] == board[9] == computer and board[3] == blank:
        return 3
    elif board[3] == board[9] == computer and board[6] == blank:
        return 6
    elif board[1] == board[5] == computer and board[9] == blank:
        return 9
    elif board[5] == board[9] == computer and board[1] == blank:
        return 1
    elif board[1] == board[9] == computer and board[5] == blank:
        return 5
    elif board[3] == board[5] == computer and board[7] == blank:
        return 7
    elif board[5] == board[7] == computer and board[3] == blank:
        return 3
    elif board[3] == board[7] == computer and board[5] == blank:
        return 5
    
    if board[1] == board[2] == player and board[3] == blank: 
        return 3
    elif board[2] == board[3] == player and board[1] == blank:
        return 1
    elif board[1] == board[3] == player and board[2] == blank:
        return 2
    elif board[4] == board[5] == player and board[6] == blank:
        return 6
    elif board[5] == board[6] == player and board[4] == blank:
        return 4
    elif board[4] == board[6] == player and board[5] == blank:
        return 5
    elif board[7] == board[8] == player and board[9] == blank:
        return 9
    elif board[8] == board[9] == player and board[7] == blank:
        return 7
    elif board[7] == board[9] == player and board[8] == blank:
        return 8
    elif board[1] == board[4] == player and board[7] == blank:
        return 7
    elif board[4] == board[7] == player and board[1] == blank:
        return 1
    elif board[1] == board[7] == player and board[4] == blank:
        return 4
    elif board[2] == board[5] == player and board[8] == blank:
        return 8
    elif board[5] == board[8] == player and board[2] == blank:
        return 2
    elif board[2] == board[8] == player and board[5] == blank:
        return 5
    elif board[3] == board[6] == player and board[9] == blank:
        return 9
    elif board[6] == board[9] == player and board[3] == blank:
        return 3
    elif board[3] == board[9] == player and board[6] == blank:
        return 6
    elif board[1] == board[5] == player and board[9] == blank:
        return 9
    elif board[5] == board[9] == player and board[1] == blank:
        return 1
    elif board[1] == board[9] == player and board[5] == blank:
        return 5
    elif board[3] == board[5] == player and board[7] == blank:
        return 7
    elif board[5] == board[7] == player and board[3] == blank:
        return 3
    elif board[3] == board[7] == player and board[5] == blank:
        return 5
    else:
        return random.choice(board_spaces)



# starting game if it's being called from main script
if __name__ == '__main__':
    main()