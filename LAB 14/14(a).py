#Bahopiya Dhaval
import math

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r**2
    def perimeter(self):
        return 2 * math.pi * self.r

# Example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
