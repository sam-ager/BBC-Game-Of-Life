import random
import sys
import os
import Tkinter as tk

'''
    Initialising Space (Creating the grid in which the Game of Life will be executed)
'''

grid = [[-1] * 8 for n in range(8)]  # Creates a list of 1s similar to that of the grid I will be creating (8x8)
grid[1][1] = 1  # Test to make sure the cell is coloured red

w = 70  # Width of each cell


def setup():
    size(600, 400)  # Size of the Game Board


def draw():
    x, y = 0, 0  # Starting at top left corner

    for row in grid:  # Loops through each row in the grid
        for col in row:
            if col == 1:
                fill(250, 0, 0)  # If the col is 1 then fill it in red
            else:
                fill(255)  # Otherwise fill it white
            rect(x, y, w, w)  # Draws a rectangle to fit the screen
            x = x + w  # Move right
        y = y + w  # Move down
        x = 0  # Float left
		
'''
In this segment, my aim was to create a grid which was 8x8, consisting of squares. 
These squares would be white until clicked of which they would then becomre red
'''


'''
    Generate Arrays for Cells
'''


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


'''
    Plot Initial Points
'''


def mousePressed():  # When mouse clicks a cell
    grid[mouseY / w][mouseX / w] = -1 * grid[mouseY / w][
        mouseX / w]  # If mouse clicks on a cell, it gives it a -1 integer and colours it red
		
'''
In this segment, the "mousePressed" function would change the colour of the selected cell on the grid, letting the user know it was selected
The main point of this was to give the cell an integer of 1, letting the code know that the cell had been selected
'''


'''
    Analyse Live Cells
'''


class Life(object):
    def __init__(self, initialState):
        self.live_cells = initialState

    def cell_should_survive(self, num_neighbours):
        sys.exit("Not Implemented")


class testLife(unittest.TestCase):
    def test_can_be_initialised_with_array_of_cells(self):
        initialState = [Cell(1, 2), Cell(2, 1)]
        life = Life(initialState[1])  #Giving the cell the 1 value to show it's alive
        self.assertEquals(initialState, life.live_cells, "Initialisation")

    def test_underpopulation(self):
        life = Life([0])
        self.assertFalse(life.cell_should_survive(0),
                         "Cell does not survive with 0 neighbours")  # If the cell's neighbours are less than 0, set cell's life to false

						 
'''
This section would need to be linked to the "mousePressed" function. By connecting to the "mousePressed" function, it can tell the the "testlife" function
that the cell has been assigned the value of 1 and that it is alive.
'''

'''
    Generate Neighbours
'''

neighbour_cells = [(-1, -1), (-1, 0), (-1, 1),  # Defines where the neighbour cells should be located
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

'''
After determining if the cell is alive, this function would then run to determine where it's neighbours should be located around it.
'''


'''
	Neighbour Overpopulation/ Under Population
'''

def neighbourtest
        neighbour = Counter(new for c in world for new in offset(neighbour_cells, c))
        world = {c for c in counts
                if (counts[c] == 2,3, life == 1 #If the cell has 3 neighbour it shall live, giving it a integer of 1 
				else if (counts[c] == <2 or 
						counts [c] == >3 and c in world, life == 0 )} #If it has less or more than 3 neighbours it shall die, giving it an integer of 0
						
'''
This loop would then determine if the cell should live based on the amount of cells that are alive around it. If the cell has 3 cells that are alive
around it, then it shall stay alive. Whereas if there are less than, or more than 3 cells alive around it, it shall die.
'''

print "Conway's The Game of Life" #Print's the name of the game so that user know's what they are playing


class MAIN(object):

    def __init__(self, master, **kwargs):
        frame = tk.Frame(master, borderwidth=5)
        frame.grid()
        et1 = tk.Entry(frame)
        et1.insert(0, 10)
        et1.grid(row=0,column=0,sticky=tk.W)
        label_contents = tk.StringVar()
        label_contents.set(et1.get())
        tk.Label(frame, textvariable=label_contents).grid(row=1, column=0, sticky=tk.W)
        refresh = tk.Button(frame, text='Refresh', command = self.refresh_clicked)
        refresh.grid(row=2, column=0, sticky=tk.W)

    #per comments:
    def refresh_clicked(event):
        #update labels here
root=tk.Tk()
app=MAIN(root)
root.mainloop() #This is a refresh button so that if the game ends, the user an start again
