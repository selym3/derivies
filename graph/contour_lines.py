def none(square):
    return []

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

def bottom_left(square):
    return [
        (
            (square.x, square.y + square.h/2),
            (square.x + square.w/2, square.y + square.h)
        )
    ]

def bottom_left_top_right(square):
    return [
        (
            (square.x + square.w/2, square.y),
            (square.x, square.y + square.h/2),
        ),
        (
            (square.x + square.w/2, square.y + square.h),
            (square.x + square.w, square.y + square.h/2)
        )
    ]

def bottom_left_top_left(square):
    return [
        (
            (square.x + square.w/2, square.y),
            (square.x + square.w/2, square.y + square.h)
        )
    ]

def bottom_left_top_right_left(square):
    return bottom_right(square)

def bottom_right(square):
    return [
        (
            (square.x + square.w/2, square.y + square.h),
            (square.x + square.w, square.y + square.h/2)
        )
    ]

def bottom_right_top_right(square):
    return bottom_left_top_left(square)

def bottom_right_top_left(square):
    return [
        (
            (square.x + square.w/2, square.y),
            (square.x + square.w, square.y + square.h/2)
        ),
        (
            (square.x, square.y + square.h/2),
            (square.x + square.w/2, square.y + square.h)
        )
    ]

def bottom_right_top_right_left(square):
    return bottom_left(square)

def bottom_right_left(square):
    return top_right_left(square)

def bottom_right_left_top_right(square):
    return top_left(square)

def bottom_right_left_top_left(square):
    return top_right(square)

def all(square):
    return []

contour_lines = [
    none,                        # 0b0000
    top_right,                   # 0b0001
    top_left,                    # 0b0010
    top_right_left,              # 0b0011
    bottom_left,                 # 0b0100
    bottom_left_top_right,       # 0b0101
    bottom_left_top_left,        # 0b0110
    bottom_left_top_right_left,  # 0b0111
    bottom_right,                # 0b1000
    bottom_right_top_right,      # 0b1001
    bottom_right_top_left,       # 0b1010
    bottom_right_top_right_left, # 0b1011
    bottom_right_left,           # 0b1100
    bottom_right_left_top_right, # 0b1101
    bottom_right_left_top_left,  # 0b1110
    all,                         # 0b1111
]

def get_segments(square, pattern):
    segms = contour_lines[pattern](square)
    
    # this is hacky idk why it needs to be here
    out = []
    for segm in segms:
        out += [(
            (segm[0][0], square.y + (square.h-(segm[0][1]-square.y))),
            (segm[1][0], square.y + (square.h-(segm[1][1]-square.y))),
        )]
    return out