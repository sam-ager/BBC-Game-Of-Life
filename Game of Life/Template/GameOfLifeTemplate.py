from collections import Counter

def life(world, new): #Generate new grid
    for generate in range(new+1): #Add grid for each for each genration
        display(world, generate) #Display the grid
        counts = Counter(new for c in world for new in offset(neighbour_cells, c))
        world = {c for c in counts
                if counts[c] == 3 or (counts[c] == 2 and c in world)}

neighbour_cells = [(-1, -1), (-1, 0), (-1, 1), #Defines where the neighbour cells should be located
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]

def offset(cells, delta):
    (dx, dy) = delta
    return {(x+dx, y+dy) for (x, y) in cells}

def display(world, generate): #Create's the grid
    print '          Test: {}'.format(generate) #Displays which state of generation test is i.e. Test: 1, Test: 2
    Xs, Ys = zip(*world)
    Xrange = range(min(Xs), max(Xs)+1) #Takes the minimum of input cells to form x axis grid around it
    for y in range(min(Ys), max(Ys)+1): #Takes the minimum of input cells to form y axis grid around it
        print '  '.join('O' if (x, y) in world else '.' #Sets live cells as o's and dead cells as .'s
                      for x in Xrange)

#blinker = {(1, 0), (1, 1), (1, 2)}
#block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
#toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
#glider  = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
#world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
#           | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))
world   = {(1, 1),
           (1, 2),
           (1, 3),
           (2,4), (3,4), (4,4)} #Location of live cells (defined by user)


life(world, 8) #How many transitions to be visualised