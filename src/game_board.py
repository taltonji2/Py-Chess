from pieces import Pawn, Piece, Rook, Knight, Bishop, Queen, King
from coordinate import Coordinate

class Game_board:
    color_index = [[0 for x in range(8)] for y in range(8)]
    board = [[0 for x in range(8)] for y in range(8)]
    active_player = 'white'
    checkmate_w = False
    checkmate_b = False
    castle_w = False
    castle_b = False
    castling = False
    
    def __init__(self) -> None:
        whiteside = True
        for y in range(8):
            for x in range(8): 
                if whiteside:
                    self.color_index[x][y] = ['white',set()]
                else:
                    self.color_index[x][y] = ['black',set()]
                
            whiteside = not whiteside
            x = 0
            
        for y in range(2):
            for x in range(8):
                if y == 1: 
                    self.board[x][y] = Pawn('black', Coordinate(x,y))
                if x == 0 and y ==0:
                    self.board[x][y] = Rook('black', Coordinate(x,y))
                if x == 1 and y ==0:
                    self.board[x][y] = Knight('black', Coordinate(x,y))
                if x == 2 and y ==0:
                    self.board[x][y] = Bishop('black', Coordinate(x,y))
                if x == 3 and y ==0:
                    self.board[x][y] = Queen('black', Coordinate(x,y))
                if x == 4 and y ==0:
                    self.board[x][y] = King('black', Coordinate(x,y))
                # if x == 5 and y ==0:
                #     self.board[x][y] = Bishop('black', Coordinate(x,y))
                # if x == 6 and y ==0:
                #     self.board[x][y] = Knight('black', Coordinate(x,y))
                if x == 7 and y ==0:
                    self.board[x][y] = Rook('black', Coordinate(x,y))
        
        for y in range(6,8):
            for x in range(8):
                if y == 6: 
                    self.board[x][y] = Pawn('white', Coordinate(x,y))
                if x == 0 and y ==7:
                    self.board[x][y] = Rook('white', Coordinate(x,y))
                # if x == 1 and y ==7:
                #     self.board[x][y] = Knight('white', Coordinate(x,y))
                # if x == 2 and y ==7:
                #     self.board[x][y] = Bishop('white', Coordinate(x,y))
                # if x == 3 and y ==7:
                #     self.board[x][y] = Queen('white', Coordinate(x,y))
                if x == 4 and y ==7:
                    self.board[x][y] = King('white', Coordinate(x,y))
                if x == 5 and y ==7:
                    self.board[x][y] = Bishop('white', Coordinate(x,y))
                if x == 6 and y ==7:
                    self.board[x][y] = Knight('white', Coordinate(x,y))
                if x == 7 and y ==7:
                    self.board[x][y] = Rook('white', Coordinate(x,y))
        
        self.update_available_moves()


    def update_pawn(self, x, y):
        if(self.board[x][y].color == 'white'):
            if (x-1 >= 0 and y-1 >= 0):
                upper_left_coordinate = Coordinate(x-1, y-1)
                if (self.board[x-1][y-1] == 0):
                    self.board[x][y].available_coordinates.add(upper_left_coordinate)
                    self.color_index[x-1][y-1][1].add(Coordinate(x,y))
                elif (isinstance(self.board[x-1][y-1], Piece) and self.board[x-1][y-1].color != self.board[x][y].color):
                    self.board[x][y].available_coordinates.add(upper_left_coordinate)
                    self.color_index[x-1][y-1][1].add(Coordinate(x,y))
            if (y-2 >= 0 and self.board[x][y-2] == 0 and y == 6):
                up_up_coordinate = Coordinate(x, y-2)
                self.board[x][y].available_coordinates.add(up_up_coordinate)
                self.color_index[x][y-2][1].add(Coordinate(x,y))
            if (y-1 >= 0 and self.board[x][y-1] == 0):
                up_coordinate = Coordinate(x, y-1)
                self.board[x][y].available_coordinates.add(up_coordinate)
                self.color_index[x][y-1][1].add(Coordinate(x,y))
            if (x+1 <= 7 and y-1 >= 0):
                upper_right_coordinate = Coordinate(x+1, y-1)
                if self.board[x-1][y-1] == 0:
                    self.board[x][y].available_coordinates.add(upper_right_coordinate)
                    self.color_index[x-1][y-1][1].add(Coordinate(x,y))
                elif isinstance(self.board[x+1][y-1], Piece) and self.board[x+1][y-1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(upper_right_coordinate)
                    self.color_index[x+1][y-1][1].add(Coordinate(x,y))
                    
        else:
            if (x-1 >= 0 and y+1 <= 7):
                lower_left_coordinate = Coordinate(x-1, y+1)
                if (self.board[x-1][y+1] == 0):
                    self.board[x][y].available_coordinates.add(lower_left_coordinate)
                    self.color_index[x-1][y+1][1].add(Coordinate(x,y))
                elif (isinstance(self.board[x-1][y+1], Piece) and self.board[x-1][y+1].color != self.board[x][y].color):
                    self.board[x][y].available_coordinates.add(lower_left_coordinate)
                    self.color_index[x-1][y+1][1].add(Coordinate(x,y))
            if (y+2 <= 7 and self.board[x][y+2] == 0 and y == 1):
                down_down_coordinate = Coordinate(x, y+2)
                self.board[x][y].available_coordinates.add(down_down_coordinate)
                self.color_index[x][y+2][1].add(Coordinate(x,y))
            if (y+1 <= 7 and self.board[x][y+1] == 0):
                down_coordinate = Coordinate(x, y+1)
                self.board[x][y].available_coordinates.add(down_coordinate)
                self.color_index[x][y+1][1].add(Coordinate(x,y))
            if (x+1 <= 7 and y+1 <= 7):
                lower_right_coordinate = Coordinate(x+1, y+1)
                if self.board[x+1][y+1] == 0:
                    self.board[x][y].available_coordinates.add(lower_right_coordinate)
                    self.color_index[x+1][y+1][1].add(Coordinate(x,y))
                elif isinstance(self.board[x+1][y+1], Piece) and self.board[x+1][y+1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(lower_right_coordinate)
                    self.color_index[x+1][y+1][1].add(Coordinate(x,y))
               

    def update_rook(self, x, y):
        left_coordinate = Coordinate(x-1, y)
        while left_coordinate.x >= 0:
            if self.board[left_coordinate.x][left_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(left_coordinate.x, left_coordinate.y))
                self.color_index[left_coordinate.x][y][1].add(Coordinate(x,y))
            elif self.board[left_coordinate.x][left_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(left_coordinate.x, left_coordinate.y))
                self.color_index[left_coordinate.x][y][1].add(Coordinate(x,y))
                break
            left_coordinate.x = left_coordinate.x - 1
        
        right_coordinate = Coordinate(x+1, y)
        while right_coordinate.x <= 7:
            if self.board[right_coordinate.x][right_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(right_coordinate.x, right_coordinate.y))
                self.color_index[right_coordinate.x][y][1].add(Coordinate(x,y))
            elif self.board[right_coordinate.x][right_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(right_coordinate.x, right_coordinate.y))
                self.color_index[right_coordinate.x][y][1].add(Coordinate(x,y))
                break
            right_coordinate.x = right_coordinate.x + 1
        
        up_coordinate = Coordinate(x, y-1)
        while up_coordinate.y >= 0:
            if self.board[up_coordinate.x][up_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(up_coordinate.x, up_coordinate.y))
                self.color_index[x][up_coordinate.y][1].add(Coordinate(x,y))
            elif self.board[x][up_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(up_coordinate.x, up_coordinate.y))
                self.color_index[x][up_coordinate.y][1].add(Coordinate(x,y))
                break
            up_coordinate.y = up_coordinate.y-1
        
        down_coordinate = Coordinate(x, y+1)
        while down_coordinate.y <= 7:
            if self.board[down_coordinate.x][down_coordinate.y] == 0:
                self.board[x][y].available_coordinates.add(Coordinate(down_coordinate.x, down_coordinate.y))
                self.color_index[x][down_coordinate.y][1].add(Coordinate(x,y))
            elif self.board[x][down_coordinate.y].color == self.board[x][y].color:
                break
            else: 
                self.board[x][y].available_coordinates.add(Coordinate(down_coordinate.x, down_coordinate.y))
                self.color_index[x][down_coordinate.y][1].add(Coordinate(x,y))
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
            if isinstance(self.board[x-1][y-2], Piece):
                if self.board[x-1][y-2].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(up_left)
                    self.color_index[up_left.x][up_left.y][1].add(Coordinate(x,y))
            else:
                self.board[x][y].available_coordinates.add(up_left)
                self.color_index[up_left.x][up_left.y][1].add(Coordinate(x,y))
            
        if x+1<=7 and y-2>=0:
            if isinstance(self.board[x+1][y-2], Piece):
                if self.board[x+1][y-2].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(up_right)
                    self.color_index[up_right.x][up_right.y][1].add(Coordinate(x,y))
            else:
                self.board[x][y].available_coordinates.add(up_right)
                self.color_index[up_right.x][up_right.y][1].add(Coordinate(x,y))
            
        if x-2>=0 and y-1>=0:
            if isinstance(self.board[x-2][y-1], Piece):
                if self.board[x-2][y-1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(left_up)
                    self.color_index[left_up.x][left_up.y][1].add(Coordinate(x,y))
            else:
                self.board[x][y].available_coordinates.add(left_up)
                self.color_index[left_up.x][left_up.y][1].add(Coordinate(x,y))
            
        if x-2>=0 and y+1<=7:
            if isinstance(self.board[x-2][y+1], Piece):
                if self.board[x-2][y+1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(left_down)
                    self.color_index[left_down.x][left_down.y][1].add(Coordinate(x,y))
            else: 
                self.board[x][y].available_coordinates.add(left_down)
                self.color_index[left_down.x][left_down.y][1].add(Coordinate(x,y))

        if x+2<=7 and y-1>=0:
            if isinstance(self.board[x+2][y-1], Piece):
                if self.board[x+2][y-1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(right_up)
                    self.color_index[right_up.x][right_up.y][1].add(Coordinate(x,y))
            else:
                self.board[x][y].available_coordinates.add(right_up)
                self.color_index[right_up.x][right_up.y][1].add(Coordinate(x,y))
            
        if x+2<=7 and y+1<=7:
            if isinstance(self.board[x+2][y+1], Piece):
                if self.board[x+2][y+1].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(right_down)
                    self.color_index[right_down.x][right_down.y][1].add(Coordinate(x,y))
            else:
                self.board[x][y].available_coordinates.add(right_down)
                self.color_index[right_down.x][right_down.y][1].add(Coordinate(x,y))

        if x-1>=0 and y+2<=7:
            if isinstance(self.board[x-1][y+2], Piece):
                if self.board[x-1][y+2].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(down_left)
                    self.color_index[down_left.x][down_left.y][1].add(Coordinate(x,y))
            else: 
                self.board[x][y].available_coordinates.add(down_left)
                self.color_index[down_left.x][down_left.y][1].add(Coordinate(x,y))

        if x+1<=7 and y+2<=7:
            if isinstance(self.board[x+1][y+2], Piece):
                if self.board[x+1][y+2].color != self.board[x][y].color:
                    self.board[x][y].available_coordinates.add(down_right)
                    self.color_index[down_right.x][down_right.y][1].add(Coordinate(x,y))
            else: 
                self.board[x][y].available_coordinates.add(down_right)
                self.color_index[down_right.x][down_right.y][1].add(Coordinate(x,y))
    
    def update_bishop(self, x, y):
        original_x = x
        original_y = y
        
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            up_left_diagonal = Coordinate(x, y)
            if isinstance(self.board[x][y], Piece):
                if self.board[x][y].color != self.board[original_x][original_y].color:
                    self.board[original_x][original_y].available_coordinates.add(up_left_diagonal)
                    self.color_index[x][y][1].add(Coordinate(original_x,original_y))
                    break
                else:
                    break
            else:
                self.board[original_x][original_y].available_coordinates.add(up_left_diagonal)
                self.color_index[x][y][1].add(Coordinate(original_x,original_y))
        
        x = original_x
        y = original_y
        
        while x+1 < 7 and y-1 > 0:
            x += 1
            y -= 1
            up_right_diagonal = Coordinate(x, y)
            if isinstance(self.board[x][y], Piece):
                if self.board[x][y].color != self.board[original_x][original_y].color:
                    self.board[original_x][original_y].available_coordinates.add(up_right_diagonal)
                    self.color_index[x][y][1].add(Coordinate(original_x,original_y))
                    break
                else:
                    break
            else:
                self.board[original_x][original_y].available_coordinates.add(up_right_diagonal)
                self.color_index[x][y][1].add(Coordinate(original_x,original_y))
        
        x = original_x
        y = original_y

        while x-1 > 0 and y+1 < 7:
            x = x - 1
            y = y + 1
            down_left_diagonal = Coordinate(x, y)
            if isinstance(self.board[x][y], Piece):
                if self.board[x][y].color != self.board[original_x][original_y].color:
                    self.board[original_x][original_y].available_coordinates.add(down_left_diagonal)
                    self.color_index[x][y][1].add(Coordinate(original_x,original_y))
                    break
                else:
                    break
            else:
                self.board[original_x][original_y].available_coordinates.add(down_left_diagonal)
                self.color_index[x][y][1].add(Coordinate(original_x,original_y))
        
        x = original_x
        y = original_y
        while x+1 < 7 and y+1 < 7:
            x += 1
            y += 1
            down_right_diagonal = Coordinate(x, y)
            if isinstance(self.board[x][y], Piece):
                if self.board[x][y].color != self.board[original_x][original_y].color:
                    self.board[original_x][original_y].available_coordinates.add(down_right_diagonal)
                    self.color_index[x][y][1].add(Coordinate(original_x,original_y))
                    break
                else:
                    break
            else:
                self.board[original_x][original_y].available_coordinates.add(down_right_diagonal)
                self.color_index[x][y][1].add(Coordinate(original_x,original_y))

    def update_queen(self, x, y):
        self.update_bishop(x,y)
        self.update_rook(x, y)

    def update_king(self, x, y):
        if x-1>=0 and y-1 >=0:
            upper_left = Coordinate(x-1, y-1)
            if self.board[x-1][y-1] == 0 or self.board[x-1][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(upper_left)
        if y-1>=0:
            up = Coordinate(x, y-1)
            if self.board[x][y-1] == 0 or self.board[x][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(up)
        if x+1<=7 and y-1>=0:
            upper_right = Coordinate(x+1, y-1)
            if self.board[x+1][y-1] == 0 or self.board[x+1][y-1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(upper_right)
        if x-1>=0:
            left = Coordinate(x-1, y)
            if self.board[x-1][y] == 0 or self.board[x-1][y].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(left)
        if x+1<=7:
            right = Coordinate(x+1, y)
            if self.board[x+1][y] == 0 or self.board[x+1][y].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(right)
        if x-1>=0 and y+1<=7:
            lower_left = Coordinate(x-1, y+1)
            if self.board[x-1][y+1] == 0 or self.board[x-1][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(lower_left)
        if x+1<=7 and y+1<=7:
            lower_right = Coordinate(x+1, y+1)
            if self.board[x+1][y+1] == 0 or self.board[x+1][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(lower_right)
        if y+1<=7:
            down = Coordinate(x, y+1)
            if self.board[x][y+1] == 0 or self.board[x][y+1].color != self.board[x][y].color:
                self.board[x][y].available_coordinates.add(down)
    
    def update_available_moves(self):
        for x in range(8):
                for y in range(8):
                    self.color_index[x][y][1].clear()
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
        def move(x1, y1, x2, y2):
            self.board[x1][y1].move(x2, y2)
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = 0

        def castle():
                move(x1, y1, x2, y2)
                if (x2 == 2):
                    move(0,y2,3,y2)
                else:
                    move(7,y2,5,y2)
        
        if (self.castling):
            castle()
            self.castling = False
        else: 
            move(x1,y1,x2,y2)

    def is_a_move(self, x1, y1, x2, y2):
        if isinstance(self.board[x1][y1], King):
            if self.board[x1][y1].color == "white" and (x2 == x1+2 or x2 == x1-2) and y2 == y1 and self.castle_w == False:
                if self.check_castle(self.board[x1][y1]):
                    self.castle_w = True
                    self.castling = True
                    return True
            if self.board[x1][y1].color == "black" and (x2 == x1-2 or x2 == x1+2) and y2 == y1 and self.castle_b == False:
                if self.check_castle(self.board[x1][y1]):
                    self.castle_b = True
                    self.castling = True
                    return True
        else:
            for coordinate in self.board[x1][y1].available_coordinates:
                if coordinate.x == x2 and coordinate.y == y2:
                    return True
            return False

    def check_castle(self, piece : King):
        # The king and rook involved in castling must not have previously moved;
        if piece.color == "black" and piece.moved == False:
            # left
            def check_black_left ():
                for i in range(1,4):
                    if self.board[piece.coordinate.x-i][0] != 0:
                        return False
                for j in range(5):
                    for cord in self.color_index[piece.coordinate.x-j][0][1]:
                        if self.board[cord.x][cord.y].color == "white":
                            return False
                rook = self.board[piece.coordinate.x-4][0]
                if isinstance(rook, Rook) and rook.color == "black" and rook.moved == False:
                    return True
            
            def check_black_right():
                for i in range(1,3):
                    if self.board[piece.coordinate.x+i][0] != 0:
                        return False
                for j in range(4):
                    for cord in self.color_index[piece.coordinate.x+j][0][1]:
                        if self.board[cord.x][cord.y].color == "white":
                            return False
                rook = self.board[piece.coordinate.x+3][0]
                if isinstance(rook, Rook) and rook.color == "black" and rook.moved == False:
                    return True
            left = check_black_left()
            right = check_black_right()
            return left or right
            
                
        if piece.color == "white" and piece.moved == False and self.castle_w == False:
            
            def check_white_left ():
                for i in range(1,4):
                    if self.board[piece.coordinate.x-i][7] != 0:
                        return False
                for j in range(5):
                    for cord in self.color_index[piece.coordinate.x-j][7][1]:
                        if self.board[cord.x][cord.y].color != "black":
                            return False
                rook = self.board[piece.coordinate.x-4][7]
                if isinstance(rook, Rook) and rook.color == "white"  and rook.moved == False:
                    return True

            def check_white_right():
                for i in range(1,3):
                    if self.board[piece.coordinate.x+i][7] != 0:
                        return False
                for j in range(4):
                    for cord in self.color_index[piece.coordinate.x+j][7][1]:
                        if self.board[cord.x][cord.y].color == "black":
                            return False
                rook = self.board[piece.coordinate.x+3][7]
                if isinstance(rook, Rook) and rook.color == "white" and rook.moved == False:
                    return True
            
            left = check_white_left()
            right = check_white_right()
            return left or right
    