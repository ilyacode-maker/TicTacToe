

from typing import Pattern

import sys
X = 'X'
O = 'O'
EMPTY = None


class x_iter():
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

class ActionException(Exception):
    def __init__(self,message):
        self.message = message



    
class not_equal():
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
            return False
        return True


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


class filled():
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
        
   
'''
class InitialBoard():
    def __init__(self, board):
        self.values = []
        self.board = board
        self.actions = []
        self.sons = []
        if t.terminal(self.board):
            self.value += t.utility(self.board)
        else:
            self.actions = t.actions(self.board)
            self.make_all_sons()
            self.get_sons_values()

    def make_all_sons(self):
        for action in self.actions:
            self.sons.append((SonBoard(t.result(self.board, action), self)))

    def get_sons_values(self):
        for son in self.sons:
            self.values.append((son.value))
            
            
class SonBoard():
    def __init__(self, board, father):
        self.value = 0
        self.board = board
        self.father = father
        self.actions = []
        self.sons = []

        if t.terminal(self.board):
            self.value += t.utility(self.board)
            self.add_value_to_father()
        else:
            self.actions = t.actions(self.board, )
            self.make_all_sons()
    
    def add_value_to_father(self):
        self.father.value += self.value

    def make_all_sons(self):
        for action in self.actions:
            self.sons.append(SonBoard(t.result(self.board, action), self))

'''
import tictactoe as t
act = ()
def maxvalue(board):
    global act
    v = -1000
    a = 0
    if t.terminal(board):
        return t.utility(board)
    for action in t.actions(board):
        a = max(v, minvalue(t.result(board, action)))
        if a > v:
            v = a
            act = action
        else:
            v = a
    return v

def minvalue(board):
    v = 1000
    a=0
    if t.terminal(board):
        return t.utility(board)
    for action in t.actions(board):
        a=min(v, maxvalue(t.result(board, action)))
        if a < v:
            v = a
            act = action
        else:
            v = a
    return v


board = [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

print(maxvalue(board))
print(act)