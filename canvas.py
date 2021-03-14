import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.width = width
        self.height = height

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # set color of the canvas. Color = {'black': [0, 0, 0], 'white': [255, 255, 255]}
        self.data[:] = color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
