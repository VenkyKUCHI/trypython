class Point:
    pass
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def reset(self):
        self.x = 0
        self.y = 0
    def print(self):
        print(self.x, self.y)

p = Point(4, 5)
p.print()
p.reset()
p.print()

new_point = Point()
new_point.print()