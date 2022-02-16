from ast import Pass

class HelloClass:
    Pass
    def reset(self):
        self.x = 0 
    def square(self):
        self.x = self.x**2
    def print(current):
        print(current.x)

P = HelloClass()
P.x =6
print(P.x)
P.square()
print(P.x)
P.reset()
print(P.x)

