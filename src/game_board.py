from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from coordinate import Coordinate

class Game_board:
    color_index = [[0 for x in range(8)] for y in range(8)]
    board = [[0 for x in range(8)] for y in range(8)]
    active_player = 'white'
    
    def __init__(self) -> None:
        whiteturn = True
        for y in range(8):
            for x in range(8): 
                if whiteturn:
                    self.color_index[x][y] = 'white'
                else:
                    self.color_index[x][y] = 'black'
                
            whiteturn = not whiteturn
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