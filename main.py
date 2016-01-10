# Hello World program in Python
from enum import Enum

class Direction(Enum):
    T = "Top"
    B = "Bottom"
    
class ImType(Enum):
    T_1 = "Image 1"
    T_2 = "Image 2"
    T_3 = "Image 3"
    T_4 = "Image 4"
    
class Edge():
    def __init__(self, direction, imtype):
        if not isinstance(direction, Direction) or not isinstance(imtype, ImType):
            raise TypeError("direction must be a Direction Enum and imtype must be an ImType Enum")
        self.direction = direction
        self.imtype = imtype
        
class Square():
    def __init__(self, number, rotation, top, left, right, bottom):
        self.number = number
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
        self.rotation = rotation
        
    def rotate():
        return Square(self.number, self.rotate + 90, self.left, self.bottom, self.top, self.right)

class Board():
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9):
        if not isinstance(s1, Square) or not isinstance(s2, Square) or not isinstance(s3, Square) or not isinstance(s4, Square) or not isinstance(s5, Square) or not isinstance(s6, Square) or not isinstance(s7, Square) or not isinstance(s8, Square) or not isinstance(s9, Square):
            raise TypeError("Invalid square type, must be of type Square for all 9 pieces input")
        print(str("Finished"))


def hardcoded_yosemite():
    # Square 1
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece1 = Square(1, 0, t, l, r, b)
    # Square 2
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece2 = Square(2, 0, t, l, r, b)
    # Square 3
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.B , ImType.T_1 )
    piece3 = Square(3, 0, t, l, r, b)
    # Square 4
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_2 )
    r = Edge(Direction.B , ImType.T_4 )
    b = Edge(Direction.T , ImType.T_1 )
    piece4 = Square(4, 0, t, l, r, b)
    # Square 5
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_2 )
    r = Edge(Direction.B , ImType.T_4 )
    b = Edge(Direction.T , ImType.T_3 )
    piece5 = Square(5, 0, t, l, r, b)
    # Square 6
    t = Edge(Direction.B , ImType.T_4 )
    l = Edge(Direction.T , ImType.T_3 )
    r = Edge(Direction.T , ImType.T_1 )
    b = Edge(Direction.T , ImType.T_2 )
    piece6 = Square(6, 0, t, l, r, b)
    # Square 7
    t = Edge(Direction.T , ImType.T_4 )
    l = Edge(Direction.B , ImType.T_3 )
    r = Edge(Direction.B , ImType.T_1 )
    b = Edge(Direction.T , ImType.T_2 )
    piece7 = Square(7, 0, t, l, r, b)
    # Square 8
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_1 )
    r = Edge(Direction.T , ImType.T_2)
    b = Edge(Direction.T , ImType.T_4 )
    piece8 = Square(8, 0, t, l, r, b)
    # Square 9
    t = Edge(Direction.T , ImType.T_3 )
    l = Edge(Direction.B , ImType.T_1 )
    r = Edge(Direction.T , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece9 = Square(9, 0, t, l, r, b)
    # Return board with 9 pieces made above
    return Board(piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9)


if __name__ == "__main__":
    board = hardcoded_yosemite()
    
