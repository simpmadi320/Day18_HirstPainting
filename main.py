from turtle import Turtle, Screen
import random
import colorgram


screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(0)

# Only used once to extract the colour gram colours
"""
colours = colorgram.extract('image.jpg', 26)
rgb_colours = []
print(colours)
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)
"""

colour_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
               (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
               (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
               (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
               (150, 115, 120)]

timmy_the_turtle.penup()
for y in range(10):
    timmy_the_turtle.setpos(-225, -225 + y*50)
    for x in range(10):
        timmy_the_turtle.dot(20, random.choice(colour_list))
        timmy_the_turtle.forward(50)


screen.exitonclick()
