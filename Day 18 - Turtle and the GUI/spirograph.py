from turtle import *
import turtle as t
import random

tt = t.Turtle()
t.colormode(255)
tt.speed('fastest')


def random_color():
    """
    Generate a random color
    Returns a tuple holding (r, g, b) values
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    """[summary]

    Args:
        size_of_gap ([type]): [description]
    """
    for i in range(int(360 / size_of_gap)):
        tt.color(random_color())
        tt.circle(100)
        tt.setheading(tt.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
