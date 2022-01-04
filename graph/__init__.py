# from PIL import Image

import sys
from typing import Tuple
sys.path.insert(0, '../derivies') # <-- fml

import exp as e
from frame import Frame


class LineSegment: pass
    # def __init__()

class Span:
    def __init__(self, mi, mx):
        self.mi = min(mi, mx)
        self.mx = max(mi, mx)

    def contains(self, value):
        return self.mi<=value<=self.mx

    def normalize(self, value):
        return (value-self.mi)/(self.mx - self.mi) 

    def lerp(self, t):
        return t * (self.mx-self.mi) + self.mi

    def map(self, value, other):
        return other.lerp(self.normalize(value))

    def range(self):
        return self.mx - self.mi

class Region:
    def __init__(self, *spans):
        self.spans = spans

    def normalize(self, values):
        return (span.normalize(value) for span, value in zip(self.spans, values))

    def lerp(self, times):
        return (span.lerp(time) for span, time in zip(self.spans, times))

    def map(self, values, other):
        return (span.map(value, other) for span, value, other in zip(self.spans, values, other.spans))

SquareMap = [

    # top right corner is above curve
    lambda sq: ((sq[0][0] + sq[1][0]/2, sq[0][1]), (sq[0][0] + sq[1][0], sq[0][1] + sq[1][1]/2)),

    # top left corner is above curve
    lambda sq: ((sq[0][0] + sq[1][0]/2, sq[0][1]), (sq[0][0], sq[0][1] + sq[1][1]/2)),

    # bottom 

]

def graph(f: e.exp, region: Region):
    """ f is an expression assumed to be in the form f(x, y) = 0 """

    # goal: divide world into 20x20 grid
    sqn = 200
    sqx = region.spans[0].range()/sqn
    sqy = region.spans[1].range()/sqn

    for dy in range(0, sqn):
        dy *= sqy
        for dx in range(0, sqn):
            dx *= sqx

            px = dx + region.spans[0].mi
            py = dy + region.spans[1].mi

            corners = [
                (px + sqx, py),
                (px, py),
                (px, py + sqy),
                (px + sqx, py + sqy)
            ]

            # find the type of curve through square
            pattern = 0
            for cid, corner in enumerate(corners):
                value = f.eval(corner).value
                if value <= 0:
                    pattern |= (1<<cid)
            
            # if it does go through the square
            if 0<pattern<15:
                square = ((px, py), (sqx, sqy))
                yield SquareMap[0](square)


if __name__ == "__main__":
    # f = e.sub(e.y(), e.x())
    x_2 = e.pow(e.x(), e.const(2))
    f = e.sub(e.pow(e.y(),e.const(2)), e.mul(x_2, e.sin(x_2)))
    graph_reg = Region(Span(-50,50), Span(-50,50))
    
    image_size = (300, 300)
    image = Region(Span(0,image_size[0]), Span(0,image_size[1]))
    frame = Frame(*image_size)

    for a, b in graph(f, graph_reg):
        
        a = list(graph_reg.map(a, image))
        b = list(graph_reg.map(b, image))

        frame.line(
            (255, 0, 0),
            a[0],image_size[1]-a[1],b[0],image_size[1]-b[1]
        )

    frame.image().save('graph/graph.png')