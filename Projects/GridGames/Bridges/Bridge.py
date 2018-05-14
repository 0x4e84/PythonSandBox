class Bridge(object):
    def __init__(self, island1, island2, possible_count):
        self.island1 = island1
        self.island2 = island2
        self.possible_count = min(possible_count, 2)
        self.confirmed_count = 0

        self.horizontal = island1.y == island2.y
        self.vertical = island1.x == island2.x

        self.connected_cells = []
        if self.horizontal:
            for x in range(island1.x+1, island2.x-1):
                self.connected_cells.append([x, island1.y])
        if self.vertical:
            for y in range(island1.y+1, island2.y-1):
                self.connected_cells.append([island1.x, y])

        print("Bridge between [{}, {}] and [{}, {}]"
              .format(island1.y, island1.x, island2.y, island2.x))

    def exclude(self):
        if self.possible_count > 0 and self.possible_count > self.confirmed_count:
            self.possible_count -= 1

    def confirm(self):
        if self.possible_count > self.confirmed_count:
            self.confirmed_count += 1
