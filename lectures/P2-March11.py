# ---------- dziedziczenie
from __future__ import annotations
from abc import ABC, abstractmethod

DEFAULT_STYLE = {"fill": None, "stroke": "black", "stroke_width": "1"}


class Style:
    def __init__(self, **style):
        self.fill = style.get("fill", DEFAULT_STYLE["fill"])
        self.stroke = style.get("stroke", DEFAULT_STYLE["stroke"])
        self.stroke_width = style.get("stroke_width", DEFAULT_STYLE["stroke_width"])

    def __str__(self):
        style_str = ""
        if self.fill is not None:
            style_str += f"fill={self.fill}"
        if self.stroke is not None:
            style_str += f"stroke={self.fill}"
        if self.stroke_width is not None:
            style_str += f"stroke-width={self.stroke_width}"
        return style_str

class OtherStyle:
    def __init__(self, **style):
        self.__params = style

    @property
    def fill(self):
        return self.__params.get("fill", "#000000")

class YetAnotherStyle:
    def __init__(self, **style):
        self.__params = style

    def get_value(self, name):
        if name in self.__params:
            return self.__params[name]
        raise ValueError(f"No such styling parameter: {name}")

o = OtherStyle()
o.fill
y = YetAnotherStyle()
y.get_value("fill")

s1 = Style(fill="red", stroke="green")
s1 = Style("red", "green", "1.0")

class Figura(ABC):

    def __init__(self, my_id):
        self.__my_id = my_id
        self.style = Style()

    @property
    def my_id(self):
        return self.__my_id

    @abstractmethod
    def pole(self):
        pass

    def __str__(self):
        return f"bazowowa figura: {self.__my_id}"


class Kolo(Figura):
    def __init__(self, my_id, r):
        super().__init__(my_id)
        self.__r = r

    def pole(self):
        return 3.14159 * self.__r * self.__r

    def draw(self):
        return f"<circle id={self.id} r='{self.__r}' cx='{self.__cx}' cy='{self.__cy}' style='{self.style}' />"


class Kwadrat(Figura):
    def __init__(self, my_id, a):
        super().__init__(my_id)
        self.__a = a

    def pole(self):
        return self.__a * self.__a


class Prostokat(Figura):
    def __init__(self, my_id, a, b):
        super().__init__(my_id)
        self.__a = a
        self.__b = b

    def pole(self):
        return self.__a * self.__b



if __name__ == "__main__":
    st = Style()

    figury = [Kolo("C1", 3.4), Kwadrat("S1", 3.0), Prostokat("R1", 3,4)]
    for f in figury:
        p = f.pole()
        if isinstance(f, Kolo):
            w = f.style.stroke_width
            f.style.stroke_width = w*1.3
        print(f"Pole {f.my_id} = {p}")
        if isinstance(f, Kolo):
            f.style.stroke_width = w