# o = MyClass()
# o.x = 2
# o.y = 3
# o.fill = 4
# o.x2 = 2
# o.y2 = 3
# o.stroke_width = 4
#
# o = MyClass().x(2).y(3).with_fill("back").stroke_width(4).x2(2).y2(3)

# ---------- Przykład 'method chaining'
napis = " Ala ma  kota "
n = (napis
     .replace("  "," ")
     .strip()
     .capitalize())

class MyClass:
    pass

class MyClassBuilder:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__fill = "black"
        self.__str_w = 1

    def x(self, v):
        self.__x = v
        return self

    def y(self, v):
        self.__y = v
        return self

    def fill(self, f):
        self.__fill = f
        return self

    def stroke_width(self, w):
        self.__str_w = w
        return self

    def end(self):
        return MyClass()

    @staticmethod
    def statyczna():
        b = MyClassBuilder()
        print(b.__x)
        b.__x = 0

def statyczna2():
    b = MyClassBuilder()
    print(b.__x)
    return b
statyczna2()

o = MyClassBuilder().x(2).y(3).stroke_width(2).fill("blue").end()
b = MyClassBuilder()
MyClassBuilder.statyczna()

print(o)

# x1=Axis()
# ax = Axes(x1, y1, x2, y2, "black", 1.0)


print(n)


class AxesBuilder:

    def __init__(self):
        self.__stroke = "black"
        self.__stroke_w = 3

    @staticmethod
    def xy0():
        """Build X, Y axes crossing at 0,0"""
        b = AxesBuilder()
        return b

    @staticmethod
    def rectangular():
        """Build X, Y, X2 Y2 rectangular axes"""
        b = AxesBuilder()
        return b

    def with_stroke(self, s):
        self.__stroke = s

AxesBuilder.rectangular().with_stroke("blue").with_stroke_width(2.3)

from abc import ABC, abstractmethod
from typing import Tuple, List
class Shape(ABC):
    @abstractmethod
    def draw(self):pass


# class PlotTransformation:
#     """converts from plot to screen coordinates and back"""
#     pass

class Axis(Shape):
    """Single axis of a plot
    """
    def __init__(self):
        self.__ntics = 0
        self.__visible = True
        self.__data_from = 0
        self.__data_to = 1

    def resize(self, data: List[float]) -> None:
        pass

    def on_axis(self, x: float) -> float:
        """returns position of point x as a fraction of this axis [0,1]"""
        pass


class Axes(Shape):
    """keeps all the four Axis instances"""

    def __init__(self):
        self._screen_xb = 0
        self._screen_xe = 100
        self.__bottom: Axis = None
        self.__intercep = 0

    def to_screen(self, x, y) -> Tuple[float, float]:
        """Converts plot data to screen coordinates"""
        screen_x = (self._screen_xe-self._screen_xb) * self.__bottom.on_axis(x) + self._screen_xb
        screen_y = 0.0 # as above
        return screen_x, screen_y

# Axes to plot sin() function
axes = (
    Axes(150, 50, 550, 250)
        .bottom(0.0, 6.28)
        .left(-1.0, 1.0)
        .top(0.0, 6.28)
        .with_stroke("black")
        .with_stroke_width(1.5)
        .right(-1.0, 1.0).end()
)

import math
x = [i/100.0 for i in range(0,360)]
y = [math.sin(x*3.14159/180) for xi in x]
pl = Plot(axes)
pl.scatter(x, y)

def scatter(x, y):
    circles = []
    for (i, (ix, iy)) in enumerate(zip(x, y)):
        circles.append( Circle(id=str(i), x=ix, y=iy) )
