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

# Here
def check_move_input():
    move = input()
    if move.lower() == "exit":
        quit()
    pattern = "([a-h][1-8]\s[a-h][1-8])"
    if re.search(pattern, move) and len(move) == 5:
        move = move.split()
        if move[0] == move[1]:
            print("invalid selection.")
            print(f'{gb.active_player}\'s move: ')
            print("what will it be? ")
            check_move_input()
        else:
            # accept move
            gb.update_available_moves()
            return
    else:
        print("invalid selection.")
        print(f'{gb.active_player}\'s move: ')
        print("what will it be? ")
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
