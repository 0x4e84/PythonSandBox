import numpy as np
from PIL import Image


class Fractals(object):

    def __init__(self):
        print("Initializing...")
        self.max_iterations = 500
        self.width = 640
        self.height = 480
        self.image = np.zeros((self.width, self.height), dtype=np.uint8)

    def configure_mandelbrot(self, max_iterations):
        self.max_iterations = max_iterations

    def start_mandelbrot(self, center_x, center_y, radius):
        print("Mandelbrot fractal")

        image = Image.new("RGB", (self.width, self.height))

        delta = 2 * radius / self.width
        start_x = center_x - radius / 2
        start_y = center_y - (self.height / 2) * delta

        y = start_y
        for j in range(self.height):
            # print("Processing row {}".format(j))
            x = start_x
            for i in range(self.width):
                self.image[i, j] = self.process_point(complex(x, y))
                x += delta
            y += delta

    def process_point(self, c):
        z = 0.0j
        for i in range(self.max_iterations):
            z = z * z + c
            if (z.real * z.real + z.imag * z.imag) >= 4:
                return i

        return self.max_iterations
