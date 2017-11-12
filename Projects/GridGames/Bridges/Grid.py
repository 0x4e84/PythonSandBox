from Bridges.Bridge import Bridge
from Bridges.Island import Island


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.total_required_bridges = 0
        self.islands = []
        self.bridges = []
        index = 0
        # Initializing an empty grid
        self.grid = [[None for x in range(width)] for y in range(height)]
        print("Grid size: {}x{}".format(width, height))

    def define(self, cells):
        index = 0
        cell_sum = 0
        for y in range(self.height):
            for x in range(self.width):
                try:
                    required_bridges = int(cells[y][x])
                    new_island = Island(index, x, y, required_bridges)
                    self.islands.append(new_island)
                    self.grid[y][x] = new_island
                    cell_sum += required_bridges
                    index += 1
                except ValueError:
                    pass

        if cell_sum % 2 == 0:
            self.total_required_bridges = int(cell_sum / 2)
            print("Found {} islands that require a total of {} bridges".format(index, self.total_required_bridges))
        else:
            print("The grid is not valid!")

    def print(self):
        grid_string = ""
        for y in range(self.height):
            for x in range(self.width):
                island = self.grid[y][x]
                if island is None:
                    grid_string += "     "
                else:
                    grid_string += "  {}  ".format(island.required_bridges)
            grid_string += "\n\n"

        return grid_string

    def find_potential_bridges(self):
        for island1 in self.islands:
            found_right = False
            found_below = False
            index = island1.index + 1

            while index < len(self.islands) and not (found_right and found_below):
                island2 = self.islands[index]
                index += 1

                if not found_right and island1.x == island2.x:
                    self.bridges.append(Bridge(island1, island2))
                    if island1.required_bridges > 1 and island2.required_bridges > 1:
                        self.bridges.append(Bridge(island1, island2))
                    found_right = True

                if not found_below and island1.y == island2.y:
                    self.bridges.append(Bridge(island1, island2))
                    if island1.required_bridges > 1 and island2.required_bridges > 1:
                        self.bridges.append(Bridge(island1, island2))
                    found_below = True

        potential = len(self.bridges)
        print("Found {} possible bridges, whereas {} are required"
              .format(potential, self.total_required_bridges))
