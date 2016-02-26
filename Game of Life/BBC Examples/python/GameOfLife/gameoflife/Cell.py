class Cell(object):
    
    def __init__(self, x, y):
        self.x = x  #The cell will use x locations (on a grid), defined in CellTest
        self.y = y  #The cell will use y locations (on a grid), defined in CellTest
        
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y