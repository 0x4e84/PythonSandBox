import sys

from PyQt5.QtWidgets import QApplication

from Bridges.Bridges import Bridges

if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("Bridges Game starting...")
    bridges = Bridges(10)
    bridges.set_grid([".1..3.3.2.",
                      "2.1..1.2.2",
                      ".1..4.1.1.",
                      ".....2.4.4",
                      "3.2.4.4.2.",
                      ".......3.4",
                      ".2..3.3.1.",
                      "2.2....2.3",
                      ".1....2.2.",
                      "1.3.3..2.2"])

    sys.exit(app.exec_())
