import numpy as np
from PIL import Image
import webbrowser


class Canvas:
    """
        Creates a canvas of given dimensions and fill color
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # creating a 3D array using zeros method in numpy
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        image = Image.fromarray(self.data, 'RGB')
        image.save(image_path)
        webbrowser.open(image_path)
