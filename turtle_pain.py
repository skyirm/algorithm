from turtle import *

my_turtle = Turtle()
mywin = my_turtle.getscreen()


def draw_spiral(turtle, line_lenth):
    if line_lenth > 0:
        turtle.forward(line_lenth)
        turtle.right(90)
        draw_spiral(turtle, line_lenth-5)


def tree(branch_lenth, t):
    t.color='green'
    if branch_lenth > 5:
        t.forward(branch_lenth)
        t.right(20)
        tree(branch_lenth-15, t)
        t.left(40)
        tree(branch_lenth-10, t)
        t.right(20)
        t.backward(branch_lenth)


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ( (p1[0]+p2[0]) /2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
    'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                    degree-1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                    degree-1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                    degree-1, myTurtle)

myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-500, -250), (0, 500), (500, -250)]
sierpinski(myPoints, 5, myTurtle)
myWin.exitonclick()


