from gameoflife.Life import Life
from gameoflife.Cell import Cell
import unittest

class testLife(unittest.TestCase):
    
    def test_can_be_initialised_with_array_of_cells(self):
        initialState = [Cell(1,2), Cell(2,1)]   #When function starts, plot cells in these points
        life = Life(initialState)   #When function starts, set cells to live
        self.assertEquals(initialState, life.live_cells, "Initialisation")
        
    def test_underpopulation(self):
        life = Life([])
        self.assertFalse(life.cell_should_survive(0), "Cell does not survive with 0 neighbours")    #If the cell's neighbours are less than 0, set cell's life to false

  