import turtle
import random


def drawLeaf(t):
    """Draw a little green square to represent a leaf.
    Returns the turtle to its original position and heading."""
    t.color("green")
    t.pendown()

    leaf_size = 5

    # Draw a small filled square
    t.begin_fill()
    for _ in range(4):
        t.forward(leaf_size)
        t.left(90)
    t.end_fill()

    # No net movement/turning happened above (the square brings the
    # turtle back to where it started, facing the same direction),
    # so nothing extra needs to be undone here.


def drawBranch(t, length, angle, branches):
    """Recursively draw a branch, its sub-branches, and leaves.

    t         - the turtle to draw with
    length    - length of the current branch
    angle     - angle (in degrees) to turn for each sub-branch
    branches  - how many more levels of branching to draw
    """

    # BASE CASE: no more branches to draw, so draw a leaf instead.
    if branches == 0:
        drawLeaf(t)
        return

    # Make bigger branches thicker, smaller branches thinner.
    t.pensize(branches)
    t.color("brown")

    # Draw this branch.
    t.pendown()
    t.forward(length)

    # --- Draw the right sub-branch ---
    t.right(angle)
    drawBranch(t, length * 0.7, angle, branches - 1)
    # After drawBranch returns, the turtle is back exactly where it was
    # right after turning right(angle) above (see hint below), so we
    # undo that turn to restore our heading.
    t.left(angle)

    # --- Draw the left sub-branch ---
    t.left(angle)
    drawBranch(t, length * 0.7, angle, branches - 1)
    t.right(angle)

    # Undo the forward movement of THIS branch so the turtle returns
    # to the exact position and heading it had when drawBranch was
    # first called. This is what lets the caller keep track of where
    # the turtle is without it ending up stranded on some leaf.
    t.penup()
    t.backward(length)
    t.pendown()


def drawTree(t):
    """Set up everything needed to draw a nice tree (except the turtle)."""
    t.speed(0)          # draw as fast as possible
    t.left(90)           # point the turtle straight up
    t.penup()
    t.goto(0, -250)       # move to the base of the trunk
    t.pendown()

    starting_length = 100
    starting_angle = 25
    num_branches = 10

    drawBranch(t, starting_length, starting_angle, num_branches)


def main():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.hideturtle()

    drawTree(t)

    screen.exitonclick()


if __name__ == "__main__":
    main()