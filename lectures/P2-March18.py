# klasa i jej obiekty
# składowe klasy to atrybuty (pola) i metody
# składowe mogą być publiczne, chronione i prywatne
# klasa potomna dziedziczy po bazowej
# dziedziczenie dotyczy składowych publicznych i chronionych
# klasa może posiadać konstruktor
# klasa potomna musi wywołać konstruktor klasy bazowej
# metody można przeciążać = klasa może posiadać metody przeciążone (overloading)
# klasa potomna może implementować i/lub przesłaniać metody klasy bazowej (overriding)
# dziedziczenie + przesłanianie -> polimorfizm klas
# destruktor

from typing import List
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self): pass


class Rect(Shape):
    def draw(self):
        print("rysuje rect")


class Group(Shape):
    def __init__(self):
        self.__elelements: List[Shape] = []

    def draw(self):
        print("<g>")
        for e in self.__elelements:
            e.draw()
        print("</g>")

    def add_shape(self, s):
        self.__elelements.append(s)

class Line(Shape):
    def draw(self):
        print("linia")

class Grid(Group):
    def __init__(self, xBL, yBL, xTR, yTR, nx, ny):
        super().__init__()
        # create nx lines from yBL to yTR
        lines_x = Group()
        for i in range(nx):
            lines_x.add_shape(Line())
        self.add_shape(lines_x)
        # create ny lines from xBL to xTR
        lines_y = Group()
        for i in range(ny):
            lines_y.add_shape(Line())
        self.add_shape(lines_y)


if __name__ == "__main__":
    g = Grid(0, 0, 10, 8, 10, 8)
    g.draw()
