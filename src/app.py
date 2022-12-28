from coordinate import Coordinate
from game_board import Game_board
import re

gb = Game_board()

def print_game_board():
    i = 0
    c = 65
    for y in range(8):
        print('\n')
        print( f"{8+i} ", end=' ')
        for x in range(8):
            if gb.board[x][y] != 0:
                board_piece =  gb.board[x][y].color[0] + gb.board[x][y].letter
                print(f"{board_piece} ", end='')
            else: 
                print(f".", end='  ')
        i-=1
    print("\n   ", end='')
    for i in range(8):
        print(f"{chr(c+i).lower()}", end='  ')
            

def start_prompt():
    print("White or black? ")
    active_player = input().lower()
    if active_player == "white" or "black":
        print(active_player+"\'s move")
    else:
        print("please make a valid selection.")
        start_prompt()

def check_move_input():
    move = input().lower()
    if move == "exit":
        quit()
    pattern = "([a-h][1-8]\s[a-h][1-8])"
    if re.search(pattern, move) and len(move) == 5:
        move = move.split()
        if move[0] == move[1]:
            invalid_move()
        else:
            move = translate_move(move)
            if gb.board[move[0][0], move[0][1]].check_move(move[1][0], move[1][1]):
                    gb.board[move[0][0], move[0][1]].move(move[1][0], move[1][1])
                    gb.update_available_moves()
            else:
                invalid_move()
    else:
        invalid_move()

def invalid_move():
    print("invalid selection.")
    print(f'{gb.active_player}\'s move: ')
    print("what will it be? ")
    check_move_input()

def translate_move(move:list):
    letter_array = ['a','b','c','d','e','f','g','h']
    new_move = []
    for position in move:
        x = letter_array.index(position[0])
        y = 8 - int(position[1])
        new_move.append([x,y])
    return new_move


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
