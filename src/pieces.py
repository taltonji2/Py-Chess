from coordinate import Coordinate
from abc import ABC, abstractmethod

from game_board import Game_board

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
    
    def castle_check(self, gb : Game_board):
        # The king and rook involved in castling must not have previously moved;
        if self.color == "black" and self.moved == False:
            for i in range(1,3):
                if gb.board[self.coordinate.x+i][self.coordinate.y] != 0:
                    return False
            for j in range(3):
                for cord in gb.color_index[self.coordinate.x+j][self.coordinate.y][1]:
                    if cord.color != "black":
                        return False
            rook = gb.board[self.coordinate.x+3][self.coordinate.y]
            if isinstance(rook, Rook) and rook.color == "black" and rook.moved == False:
                return True
                
        if self.color == "white" and self.moved == False:
            for i in range(1,3):
                if gb.board[self.coordinate.x-i][self.coordinate.y] != 0:
                    return False
            for j in range(3):
                for cord in gb.color_index[self.coordinate.x-j][self.coordinate.y][1]:
                    if cord.color != "black":
                        return False
            rook = gb.board[self.coordinate.x+3][self.coordinate.y]
            if isinstance(rook, Rook) and rook.color == "black" and rook.moved == False:
                return True
        
        return False
        
       
