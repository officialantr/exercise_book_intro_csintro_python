from graphics import *

# pending 3 - 11


def circle_program():
    win = GraphWin()
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()


def square_program():
    win = GraphWin()
    square = Rectangle(Point(50, 50), Point(90, 90))
    square.setOutline("red")
    square.setFill("red")
    square.draw(win)
    c = square.getCenter()
    for i in range(10):
        p = win.getMouse()
        new_square = square.clone()
        new_square.move(p.getX() - c.getX(), p.getY() - c.getX())
        new_square.draw(win)
    text = Text(Point(100, 30), "Click again to quit")
    text.draw(win)
    win.getMouse()
    win.close()


def archery_program():
    """
    This program draws an archery target.
    """
    initial_radius = eval(input("Enter the radius of the yellow circle: "))

    circles = ["white", "black", "blue", "red", "yellow"]
    len_circles = len(circles)

    radius = initial_radius * len_circles

    win = GraphWin()
    for color in circles:

        circle = Circle(Point(100, 90), radius)
        circle.setOutline(color)
        circle.setFill(color)
        circle.draw(win)

        radius = radius - initial_radius

    text = Text(Point(100, 180), "Click again to quit")
    text.draw(win)
    win.getMouse()
    win.close()


def main():
    options = {1: circle_program,
               2: square_program,
               3: archery_program}

    menu = """ Menu:
               Press 1 to execute "Circle Program"
               Press 2 to execute "Square Program"
               Press 3 to execute "Archery Program"
               """
    print(menu)
    option = eval(input())
    options[option]()


main()
