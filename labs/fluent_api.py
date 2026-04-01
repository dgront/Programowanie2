# In this exercise you learn how to implement fluent API

# 1. Implement Axes object using the fluent API
#    so the code below works properly
class Axes: pass
axes = (
    Axes(150, 50, 550, 250)
        .bottom(0.0, 6.28)
        .left(-1.0, 1.0)
        .top(0.0, 6.28)
        .with_stroke("black")
        .with_stroke_width(1.5)
        .right(-1.0, 1.0).end()
)

# 2. Modify your Plot class to make a scatterplot nicely
import math
x = [i/100.0 for i in range(0,360)]
y = [math.sin(xi*3.14159/180.0) for xi in x]
class Plot: pass
pl = Plot(axes)
pl.scatter(x, y)