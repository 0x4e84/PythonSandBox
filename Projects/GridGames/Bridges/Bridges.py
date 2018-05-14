import time

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from Bridges.Grid import Grid


class Bridges(QMainWindow):
    def __init__(self, grid_size):
        super().__init__()

        self.grid_size = grid_size
        self.grid = Grid(grid_size, grid_size)

        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Solve')
        btn.clicked.connect(self.solve)
        btn.setToolTip('Solve the grid')
        btn.resize(btn.sizeHint())
        #btn.move(8, 8)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addStretch(1)

        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.grid)

        widget = QWidget(self)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Ready')
        self.resize(410, 410)
        self.move(400, 200)
        self.setWindowTitle('Bridges: {0}x{0} Grid'.format(self.grid_size))
        self.show()

    def set_grid(self, cells):
        self.grid.define(cells)
        self.grid.show_grid()
        print("Grid: \n{}".format(self.grid.print()))

    def solve(self):
        start_time = time.time()

        self.grid.find_potential_bridges()
        #self.grid.

        end_time = time.time()
        duration = end_time - start_time
        print("Duration: {:.6f} s".format(duration))
