from turtle import *
# tt for Timmy the Turtle
tt = Turtle()
tt.shape()

# for i in range(20):
#     tt.pencolor("red")
#     tt.forward(10)
#     tt.penup()
#     tt.forward(10)
#     tt.pendown()

for i in range(3):
    tt.pencolor('red')
    tt.forward(100)
    tt.right(120)
for i in range(4):
    tt.pencolor('orange')
    tt.forward(100)
    tt.right(90)
for i in range(5):
    tt.pencolor('gold1')
    tt.forward(100)
    tt.right(72)
for i in range(6):
    tt.pencolor('green')
    tt.forward(100)
    tt.right(60)
for i in range(7):
    tt.pencolor('blue')
    tt.forward(100)
    tt.right(51)
for i in range(8):
    tt.pencolor('indigo')
    tt.forward(100)
    tt.right(45)
for i in range(9):
    tt.pencolor('violet')
    tt.forward(100)
    tt.right(40)
for i in range(10):
    tt.pencolor('black')
    tt.forward(100)
    tt.right(36)


# Screen must happen at the end, after we have programmed Turtle
screen = Screen()
screen.exitonclick()
