"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1
    
    if count_X > count_O:
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    i,j = action

    if copied_board[i][j] is not EMPTY:
        raise Exception("Invalid action")
    
    copied_board[i][j] = player(board) 
    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O

    diagonal1 = [board[i][i] for i in range(3)]
    if diagonal1.count(X) == 3:
        return X
    if diagonal1.count(O) == 3:
        return O
    
    diagonal2 = [board[i][2 - i] for i in range(3)] 
    if diagonal2.count(X) == 3:
        return X
    if diagonal2.count(O) == 3:
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_action = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    else:
        best_value = math.inf
        best_action = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

        return best_action

def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = math.inf

    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    
    return value

def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = -math.inf

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    
    return value