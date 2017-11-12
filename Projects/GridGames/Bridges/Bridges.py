import time

from Bridges.Grid import Grid


class Bridges(object):
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = Grid(grid_size, grid_size)

    def set_grid(self, cells):
        self.grid.define(cells)
        print("Grid: \n{}".format(self.grid.print()))

    def solve(self):
        start_time = time.time()

        self.grid.find_potential_bridges()
        self.grid.

        end_time = time.time()
        duration = end_time - start_time
        print("Duration: {:.6f} s".format(duration))
