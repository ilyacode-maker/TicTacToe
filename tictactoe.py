"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None

'''An iterator to search for X and O'''
class X_O_iter():
    def __init__(self,board,search):
        self.board = board
        self.search = search

    def __iter__(self):
        self.i = 0
        self.j = -1
        self.counter = 0
        self.returned = False
        return self

    def __next__(self):
        if self.returned:
            raise StopIteration
        
        self.j += 1
        
        if self.board[self.i][self.j] == self.search:
            self.counter +=1
            
        if self.i == 2 and self.j == 2:
            self.returned = True
            return self.counter
        
        if self.j == 2:
            self.j = -1
            self.i += 1

'''Iterator looking for empty spots'''
class action_iter():
    def __init__(self, board):
        self.board = board

    def __iter__(self):
        self.i = 0
        self.j = -1
        return self

    def __next__(self):
        if self.j == 2:
            self.j = -1
            self.i += 1
        
        if self.i > 2:
            raise StopIteration

        self.j += 1
        if self.board[self.i][self.j] == None:
            return (self.i, self.j)

        if self.j == 2:
            self.j = -1
            self.i += 1


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
    XCOUNTER = [i for i in X_O_iter(board, X) if i != None][0]
    OCOUNTER = [i for i in X_O_iter(board, O) if i != None][0]
    
    if XCOUNTER == OCOUNTER:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = [i for i in action_iter(board) if i != None]
    if len(actions_list) == 0:
        return None

    return actions_list

'''Invalid action'''
class ActionException(Exception):
    def __init__(self,message):
        self.message = message

from copy import deepcopy
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in (i for i in action_iter(board) if i != None):
        error = f'The action: {action} is invalid on the board: {board}'
        raise ActionException(error)

    deep_board = deepcopy(board)
    deep_board[action[0]][action[1]] = player(board)

    return deep_board

#COMPARING TWO LISTS

'''To further upgrade: Make the iterator check for both O and X at the same time'''
class equal():
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 2:
            raise StopIteration
        if self.list_1[self.i] == self.list_2[self.i]:
            return True
        return False

#ITERATING OVER TWO LISTS TO GET THE WIN LINE (0,2 - 1,1 - 2-0)
class iter_two():
    def __init__(self):
        pass

    def __iter__(self):
        self.i = -1
        self.j = 3
        return self

    def __next__(self):
        self.i += 1
        self.j -= 1

        if self.i > 2 or self.j < 0:
            raise StopIteration

        return (self.i, self.j)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    '''For further upgrade: eliminate checking based on where X is in the search (Use a Heuristic function) '''
    #CHEKING FOR A ROW WIN
    for j in range(3):
        #FOR X
        if all(i for i in equal(board[j], [X,X,X])):
            return X
        #FOR O
        if all(i for i in equal(board[j], [O,O,O])):
            return O
    
    #CHECKING EACH COLUMN
    for i in range(3):
        #FOR X
        if all(h for h in equal([board[j][i] for j in range(3)], [X,X,X])):
            return X

        #FOR O
        if all(h for h in equal([board[j][i] for j in range(3)], [O,O,O])):
            return O
        
    #OBLIQUE LINE GOING FROM 0-0 TO 2-2
    #__FOR X
    if all(i for i in equal([board[j][j] for j in range(3)], [X,X,X])):
        return X
    #__FOR O
    if all(i for i in equal([board[j][j] for j in range(3)], [O,O,O])):
        return O

    #CHECKING THE OTHER OBLIQUE LINE 0-2 2-0 (using the iter_two to generate indexs)
    #__FOR X
    if all(i for i in equal([board[tup[0]][tup[1]] for tup in iter_two()] ,[X,X,X])):
        return X

    #__FOR O
    if all(i for i in equal([board[tup[0]][tup[1]] for tup in iter_two()] ,[O,O,O])):
        return O

    '''if none checked...it's a tie'''
    return None
#RETURNS TRUE IF A CELL IS EMPTY AND NONE IF IT'S NOT
class not_filled():
    def __init__(self, board):
        self.board = board

    def __iter__(self):
        self.i = 0
        self.j = -1
        return self

    def __next__(self):
        if self.j == 2:
            self.j = -1
            self.i += 1
        if self.i > 2:
            raise StopIteration
        self.j += 1
        if self.board[self.i][self.j] == None:
            return True
        
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #IF SOMEONE WON THE GAME IS OVER
    if winner(board) is not None:
        return True

    if any(i for i in not_filled(board)):
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #A tie
    if winner(board) == None:
        return 0
    #X won
    if winner(board) == X:
        return 1
    #O won
    if winner(board) == O:
        return -1

from math import inf
def maxvalue(board):
    v = -inf
    move = ()
    if terminal(board):
        return utility(board) , None
    for action in actions(board):
        a , m = minvalue(result(board, action))
        if a > v:
            v = a
            move = action
            if v == 1:
                return v, move
    return v, move
    

def minvalue(board):
    v = inf
    move = ()
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        a, m=maxvalue(result(board, action))
        if a < v:
            v = a
            move = action
            if v == - 1:
                return v, move
    return v, move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    #if it's x turn we'll try to maximaze
    if player(board) == X:
        value, move = maxvalue(board)
        return move


    else:
        value, move = minvalue(board)
        return move
       