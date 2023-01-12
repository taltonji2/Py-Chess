from pieces import Pawn, Piece, Rook, Knight, Bishop, Queen, King
from coordinate import Coordinate

class Game_board:
    color_index = [[0 for x in range(8)] for y in range(8)]
    board = [[0 for x in range(8)] for y in range(8)]
    active_player = 'white'
    
    def __init__(self) -> None:
        whiteside = True
        for y in range(8):
            for x in range(8): 
                if whiteside:
                    self.color_index[x][y] = 'white'
                else:
                    self.color_index[x][y] = 'black'
                
            whiteside = not whiteside
            x = 0
            
        for y in range(2):
            for x in range(8):
                if y == 1: 
                    self.board[x][y] = Pawn('white', Coordinate(x,y))
                if x == 0 and y ==0:
                    self.board[x][y] = Rook('white', Coordinate(x,y))
                if x == 1 and y ==0:
                    self.board[x][y] = Knight('white', Coordinate(x,y))
                if x == 2 and y ==0:
                    self.board[x][y] = Bishop('white', Coordinate(x,y))
                if x == 3 and y ==0:
                    self.board[x][y] = Queen('white', Coordinate(x,y))
                if x == 4 and y ==0:
                    self.board[x][y] = King('white', Coordinate(x,y))
                if x == 5 and y ==0:
                    self.board[x][y] = Bishop('white', Coordinate(x,y))
                if x == 6 and y ==0:
                    self.board[x][y] = Knight('white', Coordinate(x,y))
                if x == 7 and y ==0:
                    self.board[x][y] = Rook('white', Coordinate(x,y))
        
        for y in range(6,8):
            for x in range(8):
                if y == 6: 
                    self.board[x][y] = Pawn('black', Coordinate(x,y))
                if x == 0 and y ==7:
                    self.board[x][y] = Rook('black', Coordinate(x,y))
                if x == 1 and y ==7:
                    self.board[x][y] = Knight('black', Coordinate(x,y))
                if x == 2 and y ==7:
                    self.board[x][y] = Bishop('black', Coordinate(x,y))
                if x == 3 and y ==7:
                    self.board[x][y] = Queen('black', Coordinate(x,y))
                if x == 4 and y ==7:
                    self.board[x][y] = King('black', Coordinate(x,y))
                if x == 5 and y ==7:
                    self.board[x][y] = Bishop('black', Coordinate(x,y))
                if x == 6 and y ==7:
                    self.board[x][y] = Knight('black', Coordinate(x,y))
                if x == 7 and y ==7:
                    self.board[x][y] = Rook('black', Coordinate(x,y))
        
        self.update_available_moves()
    
    def update_pawn(self, x, y):
        if(self.board[x][y].color == 'black'):
            if (x-1 > -1 and y-1 > -1):
                upper_left_coordinate = Coordinate(x-1, y-1)
                if (self.board[x-1][y-1] == 0):
                    self.board[x][y].available_coordinates.add(upper_left_coordinate)
                elif (isinstance(self.board[x-1][y-1], Piece) and self.board[x-1][y-1].color != self.board[x][y].color):
                    self.board[x][y].available_coordinates.add(upper_left_coordinate)
                
            if (y-1 > -1 and self.board[x-1][y-1] == 0):
                up_coordinate = Coordinate(x, y-1)
                self.board[x][y].available_coordinates.add(up_coordinate)

            if (x+1 < 8 and y-1 > -1):
                upper_right_coordinate = Coordinate(x+1, y-1)
                if self.board[x-1][y-1] == 0:
                    self.board[x][y].available_coordinates.add(upper_right_coordinate)
                elif isinstance(self.board[x+1][y-1], Piece) and self.board[x+1][y-1].color != self.board[x][y].color:
                     self.board[x][y].available_coordinates.add(upper_right_coordinate)
                
        else:
            if (x-1 > -1 and y+1 < 8):
                lower_left_coordinate = Coordinate(x-1, y+1)
                if (self.board[x-1][y+1] == 0):
                    self.board[x][y].available_coordinates.add(lower_left_coordinate)
                elif (isinstance(self.board[x-1][y+1], Piece) and self.board[x-1][y+1].color != self.board[x][y].color):
                    self.board[x][y].available_coordinates.add(lower_left_coordinate)
                
            if (y+1 < 8 and self.board[x][y+1] == 0):
                down_coordinate = Coordinate(x, y+1)
                self.board[x][y].available_coordinates.add(down_coordinate)

            if (x+1 < 8 and y+1 < 8):
                lower_right_coordinate = Coordinate(x+1, y+1)
                if self.board[x+1][y+1] == 0:
                    self.board[x][y].available_coordinates.add(lower_right_coordinate)
                elif isinstance(self.board[x+1][y+1], Piece) and self.board[x+1][y+1].color != self.board[x][y].color:
                     self.board[x][y].available_coordinates.add(lower_right_coordinate)
               
        
    def update_rook(self, x, y):
        left_coordinate = Coordinate(x-1, y)
        while left_coordinate.x > -1:
            if self.board[left_coordinate.x][left_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(left_coordinate.x, left_coordinate.y))
            elif self.board[left_coordinate.x][left_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(left_coordinate.x, left_coordinate.y))
                break
            left_coordinate.x = left_coordinate.x - 1
        
        right_coordinate = Coordinate(x+1, y)
        while right_coordinate.x < 8:
            if self.board[right_coordinate.x][right_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(right_coordinate.x, right_coordinate.y))
            elif self.board[right_coordinate.x][right_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(right_coordinate.x, right_coordinate.y))
                break
            right_coordinate.x = right_coordinate.x + 1
        
        up_coordinate = Coordinate(x, y-1)
        while up_coordinate.y > -1:
            if self.board[up_coordinate.x][up_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(up_coordinate.x, up_coordinate.y))
            elif self.board[up_coordinate.x][up_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(up_coordinate.x, up_coordinate.y))
                break
            up_coordinate.y = up_coordinate.y-1
        
        down_coordinate = Coordinate(x, y+1)
        while down_coordinate.y < 8:
            if self.board[down_coordinate.x][down_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(down_coordinate.x, down_coordinate.y))
            elif self.board[down_coordinate.x][down_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(down_coordinate.x, down_coordinate.y))
                break
            down_coordinate.y = down_coordinate.y + 1

        

    def update_knight(self, x, y):
        up_left = Coordinate(x-1,y-2)
        up_right = Coordinate(x+1, y-2)
        left_up = Coordinate(x-2, y-1)
        left_down = Coordinate(x-2, y+1)
        right_up = Coordinate(x+2, y-1)
        right_down = Coordinate(x+2, y+1)
        down_left = Coordinate(x-1, y+2)
        down_right = Coordinate(x+1, y+2)
        
        if x-1>=0 and y-2>=0:
            if self.board[x-1][y-2] == 0:
                self.board[x][y].available_coordinates.add(up_left)
            if self.board[x-1][y-2] != 0 and self.board[x-1][y-2].color != self.board[x][y].color:
               self.board[x][y].available_coordinates.add(up_left)
        if x+1<=7 and y-2>=0:
            if self.board[x+1][y-2] == 0:
                self.board[x][y].available_coordinates.add(up_right)
            if self.board[x+1][y-2] != 0 and self.board[x-1][y-2].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(up_right)
        if x-2>=0 and y-1>=0:
            if self.board[x-2][y-1] == 0:
                self.board[x][y].available_coordinates.add(left_up)
            if self.board[x-2][y-1] != 0 and self.board[x-2][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(left_up)
        if x-2>=0 and y+1<=7:
            if self.board[x-2][y+1] == 0:
                self.board[x][y].available_coordinates.add(left_down)
            if self.board[x-2][y+1] != 0 and self.board[x-2][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(left_down)
        if x+2<=7 and y-1>=0:
            if self.board[x+2][y-1] == 0:
                self.board[x][y].available_coordinates.add(right_up)
            if self.board[x+2][y-1] != 0 and self.board[x+2][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(right_up)
        if x+2<=7 and y+1<=7:
            if self.board[x+2][y+1] == 0:
                self.board[x][y].available_coordinates.add(right_down)
            if self.board[x+2][y+1] != 0 and self.board[x+2][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(right_down)
        if x-1>=0 and y+2<=7:
            if self.board[x-1][y+2] == 0:
                self.board[x][y].available_coordinates.add(down_left)
            if self.board[x-1][y+2] != 0 and self.board[x-1][y+2].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(down_left)
        if x+1<=7 and y+2<=7:
            if self.board[x+1][y+2] == 0:
                self.board[x][y].available_coordinates.add(down_right)
            if self.board[x+1][y+2] != 0 and self.board[x+1][y+2].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(down_right)
    
    def update_bishop(self, x, y):
        originalx = x
        originaly = y
        
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            up_left_diagonal = Coordinate(x, y)
            if self.board[x][y] == 0:
                print(self.board[x][y])
                self.board[x][y].available_coordinates.add(up_left_diagonal)
            elif self.board[x][y].color != self.board[originalx][originaly].color:
                self.board[x][y].available_coordinates.add(up_left_diagonal)
                break
            else:
                break
        
        x = originalx
        y = originaly
        
        while x+1 < 7 and y-1 > 0:
            x += 1
            y -= 1
            up_right_diagonal = Coordinate(x, y)
            if self.board[x][y] == 0:
                self.board[x][y].available_coordinates.add(up_right_diagonal)
            elif self.board[x][y].color != self.board[originalx][originaly].color:
                self.board[x][y].available_coordinates.add(up_right_diagonal)
                break
            else:
                break
        
        x = originalx
        y = originaly

        while x-1 > 0 and y+1 < 7:
            x = x - 1
            y = y + 1
            down_left_diagonal = Coordinate(x, y)
           
            if self.board[x][y] == 0:
                self.board[x][y].available_coordinates.add(down_left_diagonal)
            elif self.board[x][y].color != self.board[originalx][originaly].color:
                self.board[x][y].available_coordinates.add(down_left_diagonal)
                break
            else:
                break
        
        x = originalx
        y = originaly
        
        while x+1 < 7 and y+1 < 7:
            x += 1
            y += 1
            down_right_diagonal = Coordinate(x, y)
            if self.board[x][y] == 0:
                self.board[x][y].available_coordinates.add(down_right_diagonal)
            if self.board[x][y] != 0 and self.board[x][y].color != self.board[originalx][originaly].color:
                self.board[x][y].available_coordinates.add(down_right_diagonal)
                break
            else:
                break

    def update_queen(self, x, y):
        self.update_bishop(x,y)
        self.update_rook(x, y)

    def update_king(self, x, y):
        if x-1>0 and y-1 >0:
            upper_left = Coordinate(x-1, y-1)
            if self.board[x-1][y-1] == 0 or self.board[x-1][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(upper_left)
        if y-1>0:
            up = Coordinate(x, y-1)
            if self.board[x][y-1] == 0 or self.board[x][y-1].color != self.board[x][y].color:
                self.board[x][y].board[x][y].available_coordinates.add(up)
        if x+1<7 and y-1>0:
            upper_right = Coordinate(x+1, y-1)
            if self.board[x+1][y-1] == 0 or self.board[x+1][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(upper_right)
        if x-1>0:
            left = Coordinate(x-1, y)
            if self.board[x-1][y] == 0 or self.board[x-1][y].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(left)
        if x+1<7:
            right = Coordinate(x+1, y)
            if self.board[x+1][y] == 0 or self.board[x+1][y].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(right)
        if x-1>0 and y+1<7:
            lower_left = Coordinate(x-1, y+1)
            if self.board[x-1][y+1] == 0 or self.board[x-1][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(lower_left)
        if x+1<7 and y+1<7:
            lower_right = Coordinate(x+1, y+1)
            if self.board[x+1][y+1] == 0 or self.board[x+1][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(lower_right)
        if y+1<7:
            down = Coordinate(x, y+1)
            if self.board[x][y+1] == 0 or self.board[x][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(down)
    
    def update_available_moves(self):
        for x in range(8):
                for y in range(8):
                    if isinstance(self.board[x][y], Piece):
                        if type(self.board[x][y]) is int:
                            continue
                        elif type(self.board[x][y]) is Pawn:
                            self.board[x][y].available_coordinates.clear()  
                            self.update_pawn(x, y)
                        elif type(self.board[x][y]) is Knight:  
                            self.board[x][y].available_coordinates.clear() 
                            self.update_knight(x, y)
                        elif type(self.board[x][y]) is Rook:  
                            self.board[x][y].available_coordinates.clear() 
                            self.update_rook(x, y)
                        elif type(self.board[x][y]) is Bishop:  
                            self.board[x][y].available_coordinates.clear() 
                            self.update_bishop(x, y)
                        elif type(self.board[x][y]) is King:  
                            self.board[x][y].available_coordinates.clear() 
                            self.update_king(x, y)
                        elif type(self.board[x][y]) is Queen:  
                            self.board[x][y].available_coordinates.clear() 
                            self.update_rook(x, y)
                            self.update_bishop(x, y)
    
    def move_piece(self, x1, y1, x2, y2):
        self.board[x1][y1].move(x2, y2)
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = 0

    def is_a_move(self, x1, y1, x2, y2):
        for coordinate in self.board[x1][y1].available_coordinates:
            if coordinate.x == x2 and coordinate.y == y2:
                return True
        return False

    