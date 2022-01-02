import numpy as np
from PIL import Image

class Frame:
    """ simple rgb frame buffer """

    CHANNELS = 3

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.buffer = np.zeros(
            shape=(height, width, Frame.CHANNELS),
            dtype=np.uint8
        )
    
    def image(self):
        return Image.fromarray(self.buffer)

    def __getitem__(self, pixel):
        return self.buffer[pixel]
    def __setitem__(self, pixel, color):
        self.buffer[pixel] = color

    def line(self, color, x1, y1, x2, y2):
        """ todo: https://www.cs.virginia.edu/~lat7h/blog/posts/492.html """

        # create vector from one point to the other
        dx, dy = (x2-x1), (y2-y1)

        # normalize vector to the number of pixels
        pixels = max(abs(dx), abs(dy))
        dx /= pixels
        dy /= pixels

        # fill pixels
        for _ in range(pixels): 
            self[int(x1), int(y1)] = color

            x1 += dx
            y1 += dy



if __name__ == "__main__":
    fr = Frame(300, 300)
    fr.line((255, 0, 0), 0, 0, 300, 300)
    
    fr.image().save("darkness.png")
