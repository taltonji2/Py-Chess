# class piece():


class pawn():
    name = 'pawn'
    letter = 'p'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')


class knight():
    name = 'knight'
    letter = 'k'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')


class rook():
    name = 'rook'
    letter = 'r'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')


class bishop():
    name = 'bishop'
    letter = 'b'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')


class king():
    name = 'king'
    letter = 'K'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')


class queen():
    name = 'queen'
    letter = 'q'

    def __init__(self, color, coordinate) -> None:
        self.color = color
        self.coordinate = coordinate

    def move(self):
        print('nice move')
