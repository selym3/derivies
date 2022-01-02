# from PIL import Image

import sys
from typing import Tuple
sys.path.insert(0, '../derivies') # <-- fml

import exp as e
from frame import Frame


class LineSegment: pass
    # def __init__()

def graph(f: e.exp, region: Tuple[float, float], size: Tuple[int, int] = (300, 300)):
    """ f is an expression assumed to be in the form f(x, y) = 0 """
    
    def region_to_screen(x, y):
        pass

    fr = Frame(*size)



if __name__ == "__main__":
    pass