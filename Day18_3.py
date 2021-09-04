import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270]

tim.pensize(10)

tim.speed("fast")

for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))



