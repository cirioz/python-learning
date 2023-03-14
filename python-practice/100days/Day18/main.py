from turtle import Turtle, Screen
import random
import turtle as t

# tim = Turtle()
# tom = Turtle()
# jack = Turtle()



timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("yellow green")

tim = t.Turtle()

colors = ["medium aquamarine", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
dirrection = [23, 5, 100, 44, -55, 90, 15,-6, 60, 39, -12, 30, -19]

def draw_shape(num_sides):
    angle = (random.choice(dirrection)) 
    
    tim.forward(15)
    tim.right(angle)

for shape_side_n in range(1,1000):
    tim.color(random.choice(colors))
    tim.width(width=8)
    draw_shape(shape_side_n)
    

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     # timmy_the_turtle.dot()
#     timmy_the_turtle
#     # timmy_the_turtle.left(90)


# tim = t.Turtle()

# for _ in range(1):
#     timmy_the_turtle.left(-60)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(-60)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(-150)
#     timmy_the_turtle.forward(100)
    

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)



#! --------------

# from turtle import *
# from random import *

# forward(100)


# choice([1,2,3])





import heroes













screen = Screen()
screen.exitonclick()