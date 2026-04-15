# from visualife.core import HtmlViewport
from abc import ABC, abstractmethod


class AbstractWindow(ABC):

    @abstractmethod
    def draw(self, viewport): pass

    @property
    @abstractmethod
    def x(self): pass

    @property
    @abstractmethod
    def y(self): pass

    @property
    @abstractmethod
    def w(self): pass

    @property
    @abstractmethod
    def h(self): pass


class AbstractDecorator(AbstractWindow):

    def __init__(self, decorated: AbstractWindow):
        self._decorated = decorated

    @abstractmethod
    def draw(self, viewport): pass

    @property
    def x(self): return self._decorated.x

    @property
    def y(self): return self._decorated.y

    @property
    def w(self): return self._decorated.w

    @property
    def h(self): return self._decorated.h



class SimpleWindow(AbstractWindow):
    def __init__(self, x, y, w, h):
        self.__x, self.__y = x, y
        self.__w, self.__h = w, h
        self.fill = "white"
        self.stroke = "black"

    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y

    @property
    def w(self): return self.__w

    @property
    def h(self): return self.__h

    def draw(self, viewport):
        viewport.rect("", self.x, self.y, self.w, self.h, fill=self.fill, stroke=self.stroke, stroke_width=1)


class TitlebarWindow(AbstractDecorator):

    def __init__(self, a_window, bar_height=10):
        super().__init__(a_window)
        self.bar_height = bar_height

    def draw(self, viewport):
        # --- draw the simple window
        self._decorated.draw(viewport)
        # --- and draw the decoration - a title bar and the title itself
        viewport.rect("", self.x, self.y, self.w, self.bar_height, stroke_width=1)
        viewport.text("", self.x+30, self.y+8, "window title", stroke_width=0, fill="white", text_anchor="start")


class DropShadow(AbstractDecorator):

    def __init__(self, a_window):
        super().__init__(a_window)

    def draw(self, viewport):
        # --- draw the shadow first
        viewport.rect("", self.x+5, self.y+5, self.w, self.h, fill="lightgray", stroke_width=0)
        # --- and draw the main window
        self._decorated.draw(viewport)

o = SimpleWindow()
o_tb = TitlebarWindow(o)
o_tb_sh = DropShadow(o_tb)
o_tb_sh.draw()