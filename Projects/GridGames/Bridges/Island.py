class Island(object):
    def __init__(self, index, x, y, required_bridges):
        self.index = index
        self.x = x
        self.y = y
        self.required_bridges = required_bridges
        self.added_bridges = []
        self.is_complete = False
        print(self.to_string())

    def add_bridge(self, bridge):
        self.added_bridges.append(bridge)
        if len(self.added_bridges) == self.required_bridges:
            self.is_complete = True

    def to_string(self):
        return "Island {} at [{}, {}], requires {} connections"\
            .format(self.index, self.y, self.x, self.required_bridges)
