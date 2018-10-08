import random
import turtle

def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    drunkard = turtle.Turtle()
    for i in range(n):
        step = random.randint(0, 3)
        if step == 0:
            x += 1
            drunkard.seth(0)
        elif step == 1:
            x -= 1
            drunkard.seth(180)
        elif step == 2:
            y += 1
            drunkard.seth(90)
        else:
            y -= 1
            drunkard.seth(270)
        drunkard.fd(10)

    return abs(x) + abs(y)




x = 0
y = 0
n = 10
print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x, y, n)
print("After", n, "intersections, he's",
      distance, "blocks from where he started.")

turtle.mainloop()
