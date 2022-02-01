from turtle import *
import random

tt = Turtle()
tt.shape('turtle')
tt.pensize(7)
tt.speed('slow')

colors = ['red', 'orange', 'gold1', 'green',
          'blue', 'indigo', 'violet', 'black']
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(200):
    tt.color(random_color())
    tt.forward(30)
    tt.setheading(random.choice(directions))

# while True:
#     # with a random color
#     tt.color(random_color())
#     # set turtle to move forward a radnom number fo steps
#     # tt.forward(30) for hardcoded distance
#     tt.forward(random.randint(1, 100))
#     # set turtle to turn either right or left (at random) a radnom number fo degrees and move forward
#     tt.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
