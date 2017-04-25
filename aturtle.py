import turtle
import random
from pprint import pprint

def draw_square():
    window = turtle.Screen()
    window.colormode(255)
    brad = turtle.Turtle()
           
    for j in range(37):
        brad.setheading((j-1)*10)
        brad.speed(0)
        brad.pensize(random.randrange(0,6))
        brad.shape(random.choice(["arrow","turtle","circle","square","triangle","classic"]))
        brad.fillcolor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        brad.pencolor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        for i in range(4):
            brad.forward(120)
            brad.right(90)
            if i == 1:
                brad.penup()
                oldheading=brad.heading()
                aheading=brad.heading() +90
                brad.setheading(aheading)
                brad.forward(30)
                brad.stamp()
                brad.backward(30)
                brad.setheading(oldheading)
                brad.pendown()
                brad.circle(30)
        #pprint (vars(brad))
    #brad.getscreen().getcanvas().postscript(file="/User/sarasubbanna/udacity/fullStackNanoDegree/turtle.ps")
    
    window.exitonclick()


draw_square()
