# class piece():


class pawn():
    name = 'pawn'
    letter = 'p'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()
        
    def move(self):
        print('nice move')

    def create_move_set(self):
        self.legal_moves.clear()
        # upper-left
        # up
        # upper-right

class rook():
    name = 'rook'
    letter = 'r'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()

    def move(self):
        print('nice move')

    def create_move_set(self):
        self.legal_moves.clear()
        # left
        # up
        # right
        # down

class knight():
    name = 'knight'
    letter = 'k'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()

    def move(self):
        print('nice move')
    
    def create_move_set(self):
        self.legal_moves.clear()
        # up-left
        # up-right
        # left-up
        # left-down
        # right-up
        # right-down
        # down-left
        # down-right
        
class bishop():
    name = 'bishop'
    letter = 'b'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()

    def move(self):
        print('nice move')
    
    def create_move_set(self):
        self.legal_moves.clear()
        # left-diagonals
        # right-diagonals

class queen():
    name = 'queen'
    letter = 'q'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()

    def move(self):
        print('nice move')
    
    def create_move_set(self):
        self.legal_moves.clear()
        # inheret from bishop and rook

class king():
    name = 'king'
    letter = 'K'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()

    def move(self):
        print('nice move')
    
    def create_move_set(self):
        self.legal_moves.clear()
        # upper-left
        # up
        # upper-right
        # left
        # right
        # lower-left
        # lower-right
        # down



