from coordinate import Coordinate
from abc import ABC

class Piece(ABC):
    def __init__(self, color, coordinate):
        self.color = color
        self.coordinate = coordinate
        self.available_coordinates = set()
        self.moved = False
    
    @property
    def full_name(self):
        return f"{self.name}{self.color}"

    def move(self, x, y):
        self.coordinate = Coordinate(x,y)
        self.moved = True

    def check_move(self, new_x, new_y):
        for move in self.available_coordinates:
            if move.x == new_x and move.y == new_y:
                return True
        return False
    
    def __repr__(self):
        return self.letter + self.color



class Pawn(Piece):
    name = 'pawn'
    letter = 'p'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def promote(self, piece):
        self.available_coordinates.clear()

class Rook(Piece):
    name = 'rook'
    letter = 'r'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)


class Knight(Piece):
    name = 'knight'
    letter = 'k'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
            

class Bishop(Piece):
    name = 'bishop'
    letter = 'b'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
        
class Queen(Piece):
    name = 'queen'
    letter = 'q'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    
class King(Piece):
    name = 'king'
    letter = 'K'
    

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
    
        
       
