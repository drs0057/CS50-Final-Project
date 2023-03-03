class Piece():
    """Class describing a generic piece"""

    def __init__(self, coor, type):
        """Initialize attributes of the piece"""
        self.coor = coor
        self.type = type
        
bishop = Piece('A3', 'bishop')

print(bishop.coor)
print(bishop.type)