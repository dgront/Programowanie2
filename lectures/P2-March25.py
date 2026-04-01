from typing import Dict, Any, Callable, List, IO, AnyStr

# ---------- Wzorzec dyspozytor

from abc import ABC, abstractmethod

class SvgElement(ABC): pass

class Circle(SvgElement):
    def __init__(self, x:float, y:float): pass


class Rect(SvgElement):
    def __init__(self, x:float, y:float): pass


class Line(SvgElement):
    def __init__(self, x:float, y:float): pass


def create_circle(x: float, y: float) -> Circle:
    el = Circle(x, y)
    return el

def create_rectangle(x: float, y: float) -> Rect:
    el = Rect(x, y)
    return el

shape_dispatch: Dict[str, Callable[[float, float], SvgElement]] = {
    'c' : create_circle,
    'r' : create_rectangle,
}

class MarkerDispatch:
    def __init__(self):
        self.__dispatch: Dict[str, Callable[[float, float], SvgElement]] = {
            'c': create_circle,
            'r': create_rectangle,
        }

    def marker(self, m:str, *args):
        x, y = args
        return self.__dispatch[m](x, y)

    def define_new_marker(self, symbol, drawing_func):
        if symbol in self.__dispatch.keys():
            raise ValueError(f"Symbol {symbol} has been already taken by {self.__dispatch[symbol]}")
        self.__dispatch[symbol] = drawing_func

# ------------------
x, y = 10 ,10
c = 'c'
el = shape_dispatch[c](x, y)
def draw_diamond(x:float, y:float):
    # rysuje romb
    return Rect(x, y)

# markers = MarkerDispatch()
# markers.define_new_marker('d', draw_diamond)
# el = shape_dispatch['c'](x, y)
# markers.define_new_marker('c', draw_diamond)

#
# if c == 'o':
#     create_circle(x, y)
# elif c == 's':
#     create_rectangle(x, y)
# elif c == '-':
#     el = Line()
# else:
#     pass


# -------- DYGRESJA: fn vs cls


class Square:
    def __call__(self, x:float): return x*x

def func(x: float):
    return x*x

func = Square()

print(func(2))

# fabryka klas
class AbstractMaker(ABC):
    @abstractmethod
    def make_shape(self, *args) -> SvgElement: pass

class CircleMaker(AbstractMaker):

    def __init__(self):
        self.default_radius = 3

    def make_shape(self, *args) -> SvgElement:
        x, y = args
        return Circle(x, y, self.default_radius)

class RectMaker(AbstractMaker):
    def make_shape(self, *args) -> Rect:
        x, y = args
        return Rect(x, y)


class MarkerFactory:
    def __init__(self):
        self.__dispatch: Dict[str, AbstractMaker] = {
            'c': CircleMaker(),
            'r': RectMaker(),
        }

    def marker(self, m: str, *args):
        x, y = args
        return self.__dispatch[m].make_shape(x, y)

    def define_new_marker(self, symbol, drawing_maker: AbstractMaker):
        if symbol in self.__dispatch.keys():
            raise ValueError(f"Symbol {symbol} has been already taken by {self.__dispatch[symbol]}")
        self.__dispatch[symbol] = drawing_maker


# ax = AxisBuilder().from(0.0).to(10.0).tics(5).mtics(2).arrowhead(True)


from svg_plotter import SvgElement, MarkerMaker, MarkerFactory
fct = MarkerFactory()
class Unicorn(SvgElement): pass
class UnicornMaker(MarkerMaker): pass
fct.define_new_marker('u', UnicornMaker())

class Plot:
    def __init__(self):
        self.__default_marker = 'c'

    def scatter(self, x:List[float], y: List[float], **kwargs):
        marker = kwargs.get("marker", self.__default_marker)
        pass

    def save_fig(self, buffer: IO[AnyStr] | str):
        if isinstance(buffer, str):
            buffer = open(buffer, "w")
        buffer.write("<svg>")
        buffer.close()


plt = Plot()
plt.scatter(x, y, marker='o')
plt.save_fig("plik.svg")
