class Coordinate():
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y
        
    
#   8    0  1  2  3  4  5  6  7
#   7    8  9 10 11 12 13 14 15
#   6   16 17 18 19 20 21 22 23
#   5   24 25 26 27 28 29 30 31
#   4   32 33 34 35 36 37 38 39
#   3   40 41 42 43 44 45 46 47
#   2   48 49 50 51 52 53 54 55
#   1   56 57 58 59 60 61 62 63
# 
#        a  b  c  d  e  f  g  h
# 
# # # # # # # # # # # # # # # #


#       8       0  1  0  1  0  1  0  1
#       7       1  0  1  0  1  0  1  0
#       6       0  1  0  1  0  1  0  1
#       5       1  0  1  0  1  0  1  0
#       4       0  1  0  1  0  1  0  1
#       3       1  0  1  0  1  0  1  0
#       2       0  1  0  1  0  1  0  1
#       1       1  0  1  0  1  0  1  0
# 
#               a  b  c  d  e  f  g  h
#        
# # # # # # # # # # # # # # # # # # # #
    # 0 : white    1 : black