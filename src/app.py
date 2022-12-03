from coordinate import Coordinate
from pieces import rook, king, knight, pawn, queen, bishop
import re

active_player = ''
game_board_color_index = [[0 for x in range(8)] for y in range(8)]
game_board = [[0 for x in range(8)] for y in range(8)]

def create_game_board_color_index():
    whiteturn = True
    for y in range(8):
        for x in range(8): 
            if whiteturn:
                game_board_color_index[x][y] = 'white'
            else:
                game_board_color_index[x][y] = 'black'
            
        whiteturn = not whiteturn
        x = 0
        
def create_game_board():
    for y in range(2):
        for x in range(8):
            if y == 1: 
                game_board[x][y] = pawn('white', Coordinate(x,y))
            if x == 0 and y ==0:
                game_board[x][y] = rook('white', Coordinate(x,y))
            if x == 1 and y ==0:
                game_board[x][y] = knight('white', Coordinate(x,y))
            if x == 2 and y ==0:
                game_board[x][y] = bishop('white', Coordinate(x,y))
            if x == 3 and y ==0:
                game_board[x][y] = queen('white', Coordinate(x,y))
            if x == 4 and y ==0:
                game_board[x][y] = king('white', Coordinate(x,y))
            if x == 5 and y ==0:
                game_board[x][y] = bishop('white', Coordinate(x,y))
            if x == 6 and y ==0:
                game_board[x][y] = knight('white', Coordinate(x,y))
            if x == 7 and y ==0:
                game_board[x][y] = rook('white', Coordinate(x,y))
    
    for y in range(6,8):
        for x in range(8):
            if y == 6: 
                game_board[x][y] = pawn('black', Coordinate(x,y))
            if x == 0 and y ==7:
                game_board[x][y] = rook('black', Coordinate(x,y))
            if x == 1 and y ==7:
                game_board[x][y] = knight('black', Coordinate(x,y))
            if x == 2 and y ==7:
                game_board[x][y] = bishop('black', Coordinate(x,y))
            if x == 3 and y ==7:
                game_board[x][y] = queen('black', Coordinate(x,y))
            if x == 4 and y ==7:
                game_board[x][y] = king('black', Coordinate(x,y))
            if x == 5 and y ==7:
                game_board[x][y] = bishop('black', Coordinate(x,y))
            if x == 6 and y ==7:
                game_board[x][y] = knight('black', Coordinate(x,y))
            if x == 7 and y ==7:
                game_board[x][y] = rook('black', Coordinate(x,y))


def print_game_board():
    i = 0
    c = 65
    for y in range(8):
        print('\n')
        print( f"{8+i} ", end=' ')
        for x in range(8):
            if game_board[x][y] != 0: 
                print(f"{game_board[x][y].letter} ", end=' ')
            else: 
                print(f".", end='  ')

        i-=1
    
    print("\n   ", end='')
    for i in range(8):
        print(f"{chr(c+i).lower()}", end='  ')
            

def start_prompt():
    print("White or black? ")
    active_player = input()
    pattern = "[WwHhIiTtEe]|[BbLlAaCcKk]"
    if re.search(pattern, active_player):
        print(active_player.lower()+"\'s move")
    else:
        print("please make a valid selection.")
        start_prompt()

def start():
    start_prompt()
    create_game_board_color_index()
    create_game_board()
    print_game_board()

start()
