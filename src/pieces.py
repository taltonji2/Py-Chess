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
    
    def update_coordinate(self, new_coordinate):
        self.coordinate = new_coordinate
        self.create_move_set()

    @abstractmethod
    def create_move_set():
        pass

class Pawn(Piece):
    name = 'pawn'
    letter = 'p'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def create_move_set(self, gb):
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

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def create_move_set(self, gb):
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

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
    def create_move_set(self, gb):
        self.legal_moves.clear()
        x = self.coordinate.x
        y = self.coordinate.y

        up_left = Coordinate(x-1,y-2)
        up_right = Coordinate(x+1, y-2)
        left_up = Coordinate(x-2, y-1)
        left_down = Coordinate(x-2, y+1)
        right_up = Coordinate(x+2, y-1)
        right_down = Coordinate(x+2, y+1)
        down_left = Coordinate(x-1, y+2)
        down_right = Coordinate(x+1, y+2)
        
        if x-1 > -1 and y-2 > -1:
            self.legal_moves.add(up_left)
        if x+1<8 and y-2>-1:
            self.legal_moves.add(up_right)
        if x-2 > -1 and y-1 > -1:
            self.legal_moves.add(left_up)
        if x-2 > -1 and y+1 < 8:
            self.legal_moves.add(left_down)
        if x+2 < 8 and y-1 > -1:
            self.legal_moves.add(right_up)
        if x+2 < 8 and y+1 < 8:
            self.legal_moves.add(right_down)
        if x-1 > -1 and y+2 < 8:
            self.legal_moves.add(down_left)
        if x+1 < 8 and y+2 < 8:
            self.legal_moves.add(down_right)

class Bishop(Piece):
    name = 'bishop'
    letter = 'b'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
    def create_move_set(self, gb):
        self.legal_moves.clear()
        x = self.coordinate.x, y = self.coordinate.y
        while x > -1 and y > -1:
            x -= 1
            y -= 1
            up_left_diagonal = Coordinate(x, y)
            self.legal_moves.add(up_left_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x < 8 and y > -1:
            x += 1
            y -= 1
            up_right_diagonal = Coordinate(x, y)
            self.legal_moves.add(up_right_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x > -1 and y < 8:
            x -= 1
            y += 1
            down_left_diagonal = Coordinate(x, y)
            self.legal_moves.add(down_left_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x < 8 and y < 8:
            x += 1
            y += 1
            down_right_diagonal = Coordinate(x, y)
            self.legal_moves.add(down_right_diagonal)
        
class Queen(Piece):
    name = 'queen'
    letter = 'q'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)

    def create_move_set(self, gb):
        self.legal_moves.clear()

        x = self.coordinate.x, y = self.coordinate.y
        
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

        while x > -1 and y > -1:
            x -= 1
            y -= 1
            up_left_diagonal = Coordinate(x, y)
            self.legal_moves.add(up_left_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x < 8 and y > -1:
            x += 1
            y -= 1
            up_right_diagonal = Coordinate(x, y)
            self.legal_moves.add(up_right_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x > -1 and y < 8:
            x -= 1
            y += 1
            down_left_diagonal = Coordinate(x, y)
            self.legal_moves.add(down_left_diagonal)
        x = self.coordinate.x, y = self.coordinate.y
        while x < 8 and y < 8:
            x += 1
            y += 1
            down_right_diagonal = Coordinate(x, y)
            self.legal_moves.add(down_right_diagonal)   

class King(Piece):
    name = 'king'
    letter = 'K'

    def __init__(self, color, coordinate) -> None:
        super().__init__(color, coordinate)
    
    def create_move_set(self, gb):
        self.legal_moves.clear()
        x = self.coordinate.x, y = self.coordinate.y
        if x-1>-1 and y-1 >-1:
            upper_left = Coordinate(x-1, y-1)
            self.legal_moves.add(upper_left)
        if y-1>-1:
            up = Coordinate(x, y-1)
            self.legal_moves.add(up)
        if x+1<8 and y-1>-1:
            upper_right = Coordinate(x+1, y-1)
            self.legal_moves.add(upper_right)
        if x-1>-1:
            left = Coordinate(x-1, y)
            self.legal_moves.add(left)
        if x+1<8:
            right = Coordinate(x+1, y)
            self.legal_moves.add(right)
        if x-1>-1 and y+1<8:
            lower_left = Coordinate(x-1, y+1)
            self.legal_moves.add(lower_left)
        if x+1<8 and y+1<8:
            lower_right = Coordinate(x+1, y+1)
            self.legal_moves.add(lower_right)
        if y+1<8:
            down = Coordinate(x, y+1)
            self.legal_moves.add(down)