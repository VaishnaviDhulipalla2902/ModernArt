from turtle import *
from random import *
colormode(255)
speed(0)

def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)
def randomplace():
    penup()
    x = randint(-400,400)
    y = randint(-400,400)
    goto(x,y)
    pendown() 
def randomheading():
    heading = randint(0, 360)
    setheading(heading)
def drawrectangle():
    randomcolour()
    randomplace()
    length = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill() 
def drawcircle():
    radius = randint(5, 100)
    randomcolour()
    randomplace()
    dot(radius)   
def drawstar():
    randomcolour()
    randomplace()
    randomheading()
    begin_fill()
    size = randint(20, 100)
    for side in range(5):
      left(144)
      forward(size)
    end_fill()

def drawturtle():
    shape("turtle")
    randomcolour()
    randomplace()
    randomheading()
    stamp()
print "1.Rectangle"
print "2.Circle"
print "3.Turtle"
print "4.Star"
print "5.Mixed"
mode = raw_input("Enter a type:")

if mode == "1" or mode[0] == "R":
    for i in range(randint(10,100)):
        drawrectangle()
if mode == "2" or mode[0] == "C": 
    for i in range(randint(10,100)): 
         drawcircle()  
if mode == "3" or mode[0] == "T":
    for i in range(randint(10,100)):
         drawturtle()  
if mode == "4" or mode[0] == "S":
    for i in range(randint(10,100)):
        drawstar() 
if mode == "5" or mode[0] == "M":   
    for i in range(randint(10,50)):                   
        drawcircle()
        drawrectangle()
        drawstar()
        drawturtle() 


setheading(0)
filename = raw_input("How would u like to save it?  ")
getcanvas().postscript(file = filename + ".eps")  



     
           
       
