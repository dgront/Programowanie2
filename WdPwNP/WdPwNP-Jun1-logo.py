import math

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 90
        self.is_pen_down = False
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_aspect("equal")
        self.ax.axis("off")

    def up(self): self.is_pen_down = False

    def down(self): self.is_pen_down = True

    def left(self, angle_deg: float): self.a += angle_deg

    def right(self, angle_deg: float): self.a -= angle_deg

    def forward(self, n):

        x = self.x + math.cos(self.__a_rad())
        y = self.y + math.sin(self.__a_rad())
        if self.is_pen_down:
            self.ax.plot([self.x, x], [self.y, y], color="black")
        self.x = x
        self.y = y

    def show(self, figname=None):
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.margins(0.1)
        if figname:
            plt.savefig(figname)
        else:
            plt.show()

    def __a_rad(self): return 3.14159 * self.a / 180.0

square_prog = """
DOWN
REPEAT 9
    REPEAT 5
        REPEAT 4
            F 10
            L 90
        END
        L 70
    END
END
"""

def logo_runner(program: str, turtle: Turtle, n_repeat: int = 1):
    lines = program.strip().split("\n")
    for r in range(n_repeat):
        for i in range(len(lines)):
            line = lines[i]
            tokens = line.strip().split()
            cmd = tokens[0]
            if cmd == "DOWN" or cmd == "D":
                turtle.down()
            elif cmd == "UP" or cmd == "U":
                turtle.up()
            elif cmd == "LEFT" or cmd == "L":
                turtle.left(float(tokens[1]))
            elif cmd == "RIGHT" or cmd == "R":
                turtle.right(float(tokens[1]))
            elif cmd == "FORWARD" or cmd == "F":
                turtle.forward(float(tokens[1]))
            elif cmd == "END": pass
            elif cmd == "REPEAT":
                loop_cnt = 1
                count = int(tokens[1])
                loop_cmds = []
                while cmd != "END" or loop_cnt != 0:
                    i = i + 1
                    line = lines[i]
                    tokens = line.strip().split()
                    cmd = tokens[0]
                    if cmd == "REPEAT": loop_cnt += 1
                    if cmd == "END": loop_cnt -= 1
                    loop_cmds.append(line)
                loop_code = "\n".join(loop_cmds)
                print(f"PETLA:\n>>{loop_code}<<")
                logo_runner(loop_code, turtle, count)
            else:
                print("Nieznana komenda:", tokens)


if __name__ == "__main__":
    turtle = Turtle()
    logo_runner(square_prog, turtle)
    turtle.show()
