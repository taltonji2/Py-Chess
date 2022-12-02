from coordinate import Coordinate

active_player = 'white'
game_board = []


# while active_player is not 'none':
    

def create_game_board():
    j = 0
    for i in range(64):
        game_board[i] = Coordinate('white', )

def turn_rotation():
    print(f'{active_player}\'s move')