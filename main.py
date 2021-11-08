import exp as e

class eq(e.exp):

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return f'{self.l} = {self.r}'

    def deriv(self):
        return eq(self.l.deriv(), self.r.deriv())

# equation = eq(
#     e.add(e.pow(e.x(), 2), e.pow(e.y(), 2)),
#     e.const(1)
# )

# print(equation)
# print(equation.deriv())

# a = (e.mul(e.pow(e.x(), 2), e.y()))
# a = eq(
#     e.add(
#         e.mul(
#             e.pow(e.x(),2),
#             e.y()
#         ),
#         e.mul(
#             e.x(),
#             e.pow(e.y(), 2)
#         )
#     ),
#     e.mul(
#         e.x(),
#         e.const(3)
#     )
# )

# a = eq(
#     e.add(
#         e.mul(
#             e.pow(e.x(), 2),
#             e.pow(e.y(), 2)
#         ),
#         e.mul(
#             e.x(),
#             e.sin(e.y())
#         )
#     ),
#     e.const(4)
# )

# a = eq(
#     e.mul(
#         e.const(4),
#         e.mul(
#             e.cos(e.x()),
#             e.sin(e.y())
#         )
#     ),
#     e.const(1)
# )

# a = eq(
#     e.tan(e.div(e.x(), e.y())),
#     e.add(e.x(), e.y())
# )

a = eq(
    e.add(
        e.mul(e.const(4), e.pow(e.x(), 2)),
        e.mul(e.const(9), e.pow(e.y(), 2))
    ),
    e.const(72)
)

print(a)
print(a.deriv())

