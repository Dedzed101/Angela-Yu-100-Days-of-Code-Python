from turtle import Turtle, Screen


tt = Turtle()
screen = Screen()


def move_forwards():
    tt.forward(50)


screen.listen()
# * Good example of passing a function into another function
# * Better to use keyword arguments rather than positional arguments when using a function that you didnt write yourself (such as below -- onkey).
# TODO write a comment
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()
# asdfasddfbd

# * A higher order function is a function that can work with other functions
