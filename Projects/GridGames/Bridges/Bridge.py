class Bridge(object):
    def __init__(self, island1, island2):
        self.island1 = island1
        self.island2 = island2
        self.is_possible = True
        self.is_confirmed = False
        print("Bridge between [{}, {}] and [{}, {}]"
              .format(island1.y, island1.x, island2.y, island2.x))

    def exclude(self):
        self.is_possible = False
        self.is_confirmed = False

    def confirm(self):
        self.is_possible = True
        self.is_confirmed = True
