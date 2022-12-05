from coordinate import Coordinate
from game_board import Game_board
import re

gb = Game_board()
board = gb.board

def print_game_board():
    i = 0
    c = 65
    for y in range(8):
        print('\n')
        print( f"{8+i} ", end=' ')
        for x in range(8):
            if board[x][y] != 0: 
                print(f"{board[x][y].letter} ", end=' ')
            else: 
                print(f".", end='  ')

        i-=1
    print("\n   ", end='')
    for i in range(8):
        print(f"{chr(c+i).lower()}", end='  ')
            

def start_prompt():
    print("White or black? ")
    active_player = input()
    pattern = "white| White | black | Black"
    if re.search(pattern, active_player):
        print(active_player.lower()+"\'s move")
    else:
        print("please make a valid selection.")
        start_prompt()

# Here
def check_move_input():
    move = input()
    pattern = "([a-h][1-8]\s[a-h][1-8])"
    if re.search(pattern, move):
        print(move)
        return
    else:
        print("invalid selection.")
        check_move_input()

def translate_move(input:str):
    #8   . . . . . . . .
    #7   . . . . . . . .
    #6   . . . . . . . .
    #5   . . . . . . . .
    #4   . . . . . . . .
    #3   . . . . . . . .
    #2   . . . . . . . .
    #1   . . . . . . . .
    #    a b c d e f g h
    input.lower()

def game_loop():
    print_game_board()
    while gb.active_player != None:
        print(f'\n{gb.active_player}\'s move: ')
        print("what will it be? ")
        check_move_input()
        if(gb.active_player == 'white'):
            gb.active_player = 'black'
        else:
            gb.active_player = 'white'
            

        
def start():
    start_prompt()
    game_loop()

start()
