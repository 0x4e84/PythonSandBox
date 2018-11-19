import os

from Bridges.Bridge import Bridge
from Bridges.GridItem import GridItem
from Bridges.Island import Island

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QFont, QImage, QPixmap


class Grid(QGraphicsView):
    def __init__(self, width, height):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        #scene.setSceneRect(0, 0, 400, 100)
        self.setScene(self.scene)
        #self.view = QGraphicsView(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        grid_item = GridItem(10, 10, 30)
        #grid_item.setScale(2.0)
        self.scene.addItem(grid_item)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.grid_layout)
        self.font = QFont('SansSerif', 18)

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
                    text_item = QGraphicsTextItem(str(required_bridges))
                    text_item.setFont(self.font)
                    text_item.setPos(30*x+5, 30*y-2)
                    self.scene.addItem(text_item)
                    cell_sum += required_bridges
                    index += 1
                except ValueError:
                    pass

        if cell_sum % 2 == 0:
            self.total_required_bridges = int(cell_sum / 2)
            print("Found {} islands that require a total of {} bridges".format(index, self.total_required_bridges))
        else:
            print("The grid is not valid!")

    def get(self, i, j):
        island = self.grid[i][j]
        if island is None:
            return ""
        else:
            return str(island)

    def get_widget(self, i, j):
        island = self.grid[i][j]
        if island is None:
            label = QLabel("", self)
            pixmap = QPixmap(os.getcwd() + "/Images/horizontal_2.png")
            label.setPixmap(pixmap)
            return label
        else:
            label = QLabel(str(island), self)
            label.setFont(self.font)
            return label

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

    def show_grid(self):
        #for island in self.islands:
        #    label = QLabel(str(island.required_bridges), self)
        #    label.setFont(self.font)
        #    self.grid_layout.addWidget(label, island.y+1, island.x+1)

        horizontal_bridges = [0 for _ in range(self.width) for _ in range(self.height)]
        vertical_bridges = [0 for _ in range(self.width) for _ in range(self.height)]


#        for j in range(self.width):
#            for i in range(self.height):
#                self.grid_layout.addWidget(self.get_widget(i, j), i+1, j+1)

    def find_potential_bridges(self):
        bridge_count = 0
        for island1 in self.islands:
            found_right = False
            found_below = False
            index = island1.index + 1

            while index < len(self.islands) and not (found_right and found_below):
                island2 = self.islands[index]
                index += 1

                if not found_right and island1.x == island2.x:
                    count = 2 if island1.required_bridges > 1 and island2.required_bridges > 1 else 1
                    self.bridges.append(Bridge(island1, island2, count))
                    bridge_count += count
                    found_right = True

                if not found_below and island1.y == island2.y:
                    count = 2 if island1.required_bridges > 1 and island2.required_bridges > 1 else 1
                    self.bridges.append(Bridge(island1, island2, count))
                    bridge_count += count
                    found_below = True

        len(self.bridges)
        print("Found {} possible bridges, whereas {} are required"
              .format(bridge_count, self.total_required_bridges))
