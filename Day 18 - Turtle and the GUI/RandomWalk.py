from turtle import *
import random

tt = Turtle()
tt.shape()

colors = ['red', 'orange', 'gold1', 'green',
          'blue', 'indigo', 'violet', 'black']

while True:

    # set turtle to move forward a radnom number fo steps
    # set turtle to turn either right or left (at random) a radnom number fo degrees and move forward
    # with a random color
tt.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
