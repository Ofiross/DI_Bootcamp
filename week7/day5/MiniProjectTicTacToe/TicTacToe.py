# Tic Tac Toe

def display_board(board):
    """
    Info: function that create a play board of 3*3 for tic tac toe.
    """
    print('*****************')
    print('*   ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '   *')
    print('*  ---|---|---  *')
    print('*   ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '   *')
    print('*  ---|---|---  *')
    print('*   ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '   *')
    print('*****************')

##########################################################################################################################################


def player_input():
    """
    Info: a function that decides if player number 1 will be X or O.
    """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X'
    else:
        return 'O'


##########################################################################################################################################


def place_marker(board, marker, position):
    """
    Info: a function that places the marker on the board base on the player choice.
    """
    board[position] = marker

##########################################################################################################################################


def win_check(board, mark):
    """
    Info: function to check for a winner.
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

##########################################################################################################################################


def space_check(board, position):
    """
    Info: checking if the position the player chooses is free or not.
    """
    return board[position] == ' '

##########################################################################################################################################


def full_board_check(board):
    """
    Info: The function is checking if the board is full, if it is, then it is a tie game.
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

##########################################################################################################################################


def player_choice(board):
    """
    Info: a function that asks the player to make a move by choosing a position from 1-9
    """
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position
##########################################################################################################################################


def replay():
    """
    Info: a function that asks the players if they want to play again.
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

##########################################################################################################################################


print('Welcome to Tic Tac Toe!')
print('For make your moves you will use the num pad as a game board with each number presenting the position for the marker.')

# A while loop to call all the functions and repeat them to create the game in the correct order.
while True:

    theBoard = [' '] * 10
    play_game = input(
        'Are you ready to play? Enter y for Yes or n No: ').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        break
    player1_marker = player_input()
    print(f'Player 1 will go first and his marker is:{player1_marker}')
    turn = 'Player 1'
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            print('Player 1 turn:')
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            print('Player 2 turn:')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
