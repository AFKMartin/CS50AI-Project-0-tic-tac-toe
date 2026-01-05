import math

X = "X"
O = "O"

# IMPORTANT KEEP THIS IN MIND
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
    # Count Xs and Os
    xc = sum(row.count(X) for row in board)
    oc = sum(row.count(O) for row in board)

    # Determinate the player
    if xc == oc:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Empty set to store data
    s = set()

    # Loop through every row (i) and column (j)
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            # Check if they are empty
            if board[i][j] == EMPTY:
                # If they are add the tuple to the set
                s.add((i, j))
    
    # Return the set
    return s

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Extract the (i, j) position from the action tuple
    i, j = action

    # Check if action is valid
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
        raise Exception("Invalid action")
    
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    
    # Create a copy of the board
    new_board = new_board = [row[:] for row in board]

    # Determinate wich player is about to move
    current_player = player(board)

    # Place the player symbol
    new_board[i][j] = current_player

    # Return the new board with the move applied
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # For each row:
    for row in board:

        # All three are the same
        if row[0] == row[1] == row[2] != EMPTY:
        
        # Return the winner
            return row[0]

    # For each column:
    for j in range(3):

        # All three are the same
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:

        # Return the winner
            return board[0][j]

    # Check if main diagonal cells match or are empty
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]

    # Check if anti-diagonal cells match or are empty
    if board[2][0] == board[1][1] == board[0][2] != EMPTY:
        return board[1][1]

    # If no winner return none
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If someone has alredy won return true
    if winner(board) is not None:
        return True

    # If there is NOT empty cells return false
    for row in board:
        if EMPTY in row:
            return False

    # If no winner and no empty cells it's a draw return True
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check who won
    win = winner(board)

    # If X did, return 1
    if win == X:
        return 1
    
    # If O did, return - 1
    elif win  == O:
        return - 1
    
    # If none did, return 0
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check if game is alredy over
    if terminal(board):
        return None

    current = player(board)

    # X wants to maximize
    if current == X:
        best_value = float("-inf")
        best_action = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    # O wants to minimize
    else:
        best_value = float("inf")
        best_action = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

        return best_action

