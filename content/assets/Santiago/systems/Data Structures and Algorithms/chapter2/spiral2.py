import turtle
import math
import sys
import threading


def drawSpiral(t, centerX, centerY, radius, angle):
    if radius <= 0:
        return

    radians = math.radians(angle)
    x = centerX + radius * math.cos(radians)
    y = centerY + radius * math.sin(radians)

    t.goto(x, y)

    drawSpiral(t, centerX, centerY, radius - 0.04, angle + 5)


def drawSpiralSetup(t, centerX, centerY):
    startRadius = 200
    startAngle = 0

    radians = math.radians(startAngle)
    startX = centerX + startRadius * math.cos(radians)
    startY = centerY + startRadius * math.sin(radians)

    t.penup()
    t.goto(startX, startY)
    t.pendown()

    drawSpiral(t, centerX, centerY, startRadius, startAngle)


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("black")
    t.pensize(2)

    drawSpiralSetup(t, 0, 0)

    screen.exitonclick()


def run():
    # Raise Python's own recursion limit.
    sys.setrecursionlimit(10000)
    main()


if __name__ == "__main__":
    # Run in a new thread with a much larger C stack (default is often
    # only ~8MB, which is nowhere near enough for 5000+ nested calls
    # once tkinter's internal call frames are factored in).
    threading.stack_size(64 * 1024 * 1024)  # 64 MB stack
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()