import colorgram
import random
import turtle as t

# use turtle module to make a painting of 10 x 10 dots of random colors
# import the turtle module as 't' so you can set the colormode to 255 (which allows (r,g,b) to work).
tt = t.Turtle()
t.colormode(255)
tt.hideturtle()
tt.speed('fastest')

# Penup so that there is no line drawn. Set the inital heading so that the whole piece is easily visible in the window.
tt.penup()
tt.setheading(225)
tt.forward(300)
tt.setheading(0)

# color list extracted from dhirst.jpg using colorgram module (see below).
color_list = [(148, 78, 56), (162, 53, 74), (205, 153, 106),
              (141, 27, 46), (64, 26, 36), (237, 214, 187)]


def poop_dots():
    """
    Turtle poops a randomly colored dot and then paces forward 50 steps.
    """
    for i in range(10):
        tt.dot(20, random.choice(color_list))
        tt.forward(50)


def set_headings():
    """
    Reorients the turtle after each line is pooped.
    """
    tt.setheading(90)
    tt.forward(50)
    tt.setheading(180)
    tt.forward(500)
    tt.setheading(0)


# call functions to poop a line of 10 dots and then reposition the turtle a total of 10 times.
for i in range(10):
    poop_dots()
    set_headings()


screen = t.Screen()
screen.exitonclick()


# Extract the 6 most common colors of dhirst.jpg

# When reading files, make sure to copy/paste the entire path (relative or absolute, whichever -- just 'dhirst.jpg' isnt enough,
# even if it's in the same directory)
colors = colorgram.extract(
    'Day 18 - Turtle and the GUI/Hirst Painting Project/dhirst.jpg', 6)

# Add an (r,g,b) tuple to the list of colors.
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)
# print(colors)
