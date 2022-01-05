def top_right(square):
    return [
        (
            (square.x + square.w/2, square.y), 
            (square.x + square.w, square.y + square.h/2)
        )
    ]

def top_left(square): 
    return [
        (
            (square.x + square.w/2, square.y), 
            (square.x, square.y + square.h/2)
        )
    ]

def top_right_left(square):
    return [
        (
            (square.x, square.y + square.h/2), 
            (square.x + square.w, square.y + square.h/2)
        )
    ]

def segm(square):
    return [
        (
            (square.x, square.y), 
            (square.x + square.w, square.y + square.h)
        )
    ]

contour_lines = [
    lambda _: [],       # 0b0000
    top_right,          # 0b0001
    top_left,           # 0b0010
    top_right_left,     # 0b0011
    segm,               # 0b0100
    segm,               # 0b0101
    segm,               # 0b0110
    segm,               # 0b0111
    segm,               # 0b1000
    segm,               # 0b1001
    segm,               # 0b1010
    segm,               # 0b1011
    segm,               # 0b1100
    segm,               # 0b1101
    segm,               # 0b1110
    lambda _: [],       # 0b1111
]

def get_segments(square, pattern):
    return contour_lines[pattern](square)