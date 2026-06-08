import math

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

class SimpleDrawing:
    def __init__(self):
        self.fig = None
        self.ax = None
        self.x = 0.0
        self.y = 0.0
        self.a = 0
        self.pen_down = True

    def start_figure(self, width=6, height=6):
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_aspect("equal")
        self.ax.axis("off")
        self.x = 0.0
        self.y = 0.0
        self.pen_down = True

    def move_to(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def forward(self, n: float):
        x = self.x + n * math.sin(self.__to_rad(self.a))
        y = self.y + n * math.cos(self.__to_rad(self.a))
        if self.pen_down:
            self.ax.plot([self.x, x], [self.y, y], color="black")
        self.x = x
        self.y = y

    def left(self, angle): self.a += angle

    def right(self, angle): self.a -= angle

    def finish_figure(self, filename=None):
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.margins(0.1)

        if filename is not None:
            self.fig.savefig(filename, bbox_inches="tight")

        plt.show()

    def __to_rad(self, a): return 3.14159*a / 180


class LogoInterpreter:
    def __init__(self, backend: SimpleDrawing):
        self.backend: SimpleDrawing = backend

    def run(self, program):
        lines = program.splitlines()
        lines = [line.strip() for line in lines]

        # remove empty lines and comments
        lines = [
            line for line in lines
            if line and not line.startswith("#")
        ]

        self._run_lines(lines)

    def _run_lines(self, lines):
        i = 0
        loops_open = 0
        loop = []

        while i < len(lines):
            parts = lines[i].split()
            command = parts[0].upper()

            if command == "MOVETO":
                x = float(parts[1])
                y = float(parts[2])
                self.backend.move_to(x, y)

            elif command == "UP":
                self.backend.pen_down = False

            elif command == "DOWN":
                self.backend.pen_down = True

            elif command == "LEFT" or command == "L":
                a = float(parts[1])
                self.backend.left(a)

            elif command == "RIGHT" or command == "R":
                a = float(parts[1])
                self.backend.right(a)

            elif command == "FORWARD" or command == "F":
                n = float(parts[1])
                self.backend.forward(n)

            elif command == "REPEAT":
                n = int(parts[1])
                loops_open = 1
                block = []
                i += 1
                while loops_open > 0:
                    if lines[i].startswith("REPEAT"):
                        loops_open += 1
                    if lines[i].startswith("END"):
                        loops_open -= 1
                    block.append(lines[i])
                    i += 1

                for _ in range(n):
                    self._run_lines(block)

            elif command == "END":
                return

            else:
                raise ValueError(f"Unknown command: {command}")

            i += 1

squares = """

REPEAT 100
UP
L 45
F 50
R 45
R 95
DOWN
    REPEAT 4
    F 100
    L 90
    END
MOVETO 0 0
END
"""

if __name__ == "__main__":
    backend = SimpleDrawing()

    backend.start_figure()

    interpreter = LogoInterpreter(backend)

    # backend.left(10)
    # backend.forward(100)
    # backend.left(90)
    # backend.forward(100)
    # backend.left(90)
    # backend.forward(100)
    # backend.left(90)
    # backend.forward(100)
    # backend.finish_figure("logo_output.pdf")
    interpreter.run(squares)
    backend.finish_figure(None)