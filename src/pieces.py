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

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def check_move():
        pass

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
    
    def move(self, x, y):
        self.coordinate = Coordinate(x,y)

    def create_move_set(self):
        self.legal_moves.clear()
        if(self.color == 'black'):
            upper_left_coordinate = Coordinate(self.coordinate.x-1, self.coordinate.y-1)
            self.legal_moves.add(upper_left_coordinate)
            up_coordinate = Coordinate(self.coordinate.x, self.coordinate.y-1)
            self.legal_moves.add(up_coordinate)
            upper_right_coordinate = Coordinate(self.coordinate.x+1, self.coordinate.y-1)
            self.legal_moves.add(upper_right_coordinate)
        else:
            upper_left_coordinate = Coordinate(self.coordinate.x-1, self.coordinate.y+1)
            self.legal_moves.add(upper_left_coordinate)
            up_coordinate = Coordinate(self.coordinate.x, self.coordinate.y+1)
            self.legal_moves.add(up_coordinate)
            upper_right_coordinate = Coordinate(self.coordinate.x+1, self.coordinate.y+1)
            self.legal_moves.add(upper_right_coordinate)
    
    def check_move(self, new_x, new_y):
        for move in self.legal_moves:
            if move.x == new_x and move.y == new_y:
                return True
        return False
        
class Rook(Piece):
    name = 'rook'
    letter = 'r'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def move(self, newCoordinate):
        self.coordinate = newCoordinate

    def create_move_set(self):
        self.legal_moves.clear()
        # left
        # up
        # right
        # down

class Knight(Piece):
    name = 'knight'
    letter = 'k'
    color = ''
    color_letter = ''
    coordinate = None
    legal_moves = None

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def move(self, newCoordinate):
        self.coordinate = newCoordinate
    
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

    def move(self, newCoordinate):
        self.coordinate = newCoordinate
    
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

    def move(self, newCoordinate):
        self.coordinate = newCoordinate
    
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

    def move(self, newCoordinate):
        self.coordinate = newCoordinate
    
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