from coordinate import Coordinate
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, coordinate):
        self.color = color
        self.coordinate = coordinate
        self.legal_moves = set()
        self.create_move_set()
    
    @property
    def full_name(self):
        return f"{self.color_letter}{self.letter}"

    def move(self, x, y):
        self.coordinate = Coordinate(x,y)

    def check_move(self, new_x, new_y):
        for move in self.legal_moves:
            if move.x == new_x and move.y == new_y:
                return True
        return False
    
    @abstractmethod
    def create_move_set():
        pass

class Pawn(Piece):
    name = 'pawn'
    letter = 'p'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
      
    def update_coordinate(self, new_coordinate):
        self.coordinate = new_coordinate
        self.create_move_set()

    def create_move_set(self):
        self.legal_moves.clear()
        x = self.coordinate.x
        y = self.coordinate.y
        
        if(self.color == 'black'):
            if (x-1 > -1 and y-1 > -1):
                upper_left_coordinate = Coordinate(x-1, y-1)
                self.legal_moves.add(upper_left_coordinate)
            if (y-1 > -1):
                up_coordinate = Coordinate(x, y-1)
                self.legal_moves.add(up_coordinate)
            if (x+1 < 8 and y-1 > -1):
                upper_right_coordinate = Coordinate(self.coordinate.x+1, self.coordinate.y-1)
                self.legal_moves.add(upper_right_coordinate)
        else:
            if (x-1 > -1 and y+1 < 8):
                upper_left_coordinate = Coordinate(self.coordinate.x-1, self.coordinate.y+1)
                self.legal_moves.add(upper_left_coordinate)
            if (y+1 < 8):
                up_coordinate = Coordinate(self.coordinate.x, self.coordinate.y+1)
                self.legal_moves.add(up_coordinate)
            if (x+1< 8 and y+1 < 8):
                upper_right_coordinate = Coordinate(self.coordinate.x+1, self.coordinate.y+1)
                self.legal_moves.add(upper_right_coordinate)

class Rook(Piece):
    name = 'rook'
    letter = 'r'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def create_move_set(self):
        self.legal_moves.clear()
        x = self.coordinate.x
        y = self.coordinate.y

        for xi in range(x):
            left_coordinate = Coordinate(xi, y)
            self.legal_moves.add(left_coordinate)

        for yi in range(0, y):
            up_coordinate = Coordinate(x, yi)
            self.legal_moves.add(up_coordinate)

        for xi in range(x, 8):
            right_coordinate = Coordinate(xi, y)
            self.legal_moves.add(right_coordinate)

        for yi in range(y, 8):
                down_coordinate = Coordinate(x, yi)
                self.legal_moves.add(down_coordinate)


class Knight(Piece):
    name = 'knight'
    letter = 'k'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
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
        
class Bishop(Piece):
    name = 'bishop'
    letter = 'b'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
    def create_move_set(self):
        self.legal_moves.clear()
        # left-diagonals
        # right-diagonals

class Queen(Piece):
    name = 'queen'
    letter = 'q'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def create_move_set(self):
        self.legal_moves.clear()
        # inheret from bishop and rook

class King(Piece):
    name = 'king'
    letter = 'K'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
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