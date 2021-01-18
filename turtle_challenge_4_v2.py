import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# ########## Challenge 4 - Random Walk ########

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turn = [0, 90, 180, 270]
tim.pensize(5)
tim.speed('fastest')

for _ in range(200):
    tim.color(random_color())
    tim.left(random.choice(turn))
    tim.forward(30)
    tim.setheading(random.choice(turn))