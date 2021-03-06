import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


class Gridmap(object):
    # Visualization tools
    #    occupancy:        A binary array encoding an occupancy grid of
    #                      the environment (1: occupied, 0: free)
    #    xres, yres:       Map resolution
    def __init__(self, occupancy, xres=1, yres=1):
        # Flip the occupancy grid so that indexing starts in the lower-left
        self.occupancy = occupancy[::-1, :]
        self.xres = xres
        self.yres = yres
        self.m = self.occupancy.shape[0]
        self.n = self.occupancy.shape[1]

    # Returns True if (x, y) is in collision
    #   ij:   Indicates whether (x,y) are array indices
    def inCollision(self, x, y, ij=False):

        if ij == True:
            j = x
            i = y
        else:
            # j = int(np.ceil(x/self.xres))
            # i = int(np.ceil(y/self.yres))
            j = int(np.floor(x / self.xres))
            i = int(np.floor(y / self.yres))
            # i = (self.m-1) - int(np.floor(y/self.yres)) # Since i=0 is upper-left

        if (i >= self.m) or (j >= self.n):
            print(
                "inCollision: Index out of range (i,j) = (%d,%d) where size = (%d, %d)"
                % (i, j, self.m, self.n)
            )
            return True
        if self.occupancy[i, j] == 1:
            return True
        else:
            return False

    # Returns the height and width of the occupancy
    # grid in terms of the number of cells
    #
    # Returns:
    #   m: Height in number of cells
    #   n: Width in number of cells
    def getShape(self):
        return self.m, self.n

    # Converts an (i,j) integer pair to an (x,y) pair
    #   i:   Row index (zero at bottom)
    #   j:   Column index
    #
    # Returns
    #   x:   x position
    #   y:   y position
    def ij2xy(self, i, j):
        x = np.float(j * self.xres)
        y = np.float(i * self.yres)

        return (x, y)

    # Converts an (i,j) integer pair to an (x,y) pair
    #   x:   x position
    #   y:   y position
    #
    # Returns:
    #   i:   Row index (zero at bottom)
    #   j:   Column index
    def xy2ij(self, x, y):
        i = int(np.floor(y / self.yres))
        j = int(np.floor(x / self.yres))

        return (i, j)
