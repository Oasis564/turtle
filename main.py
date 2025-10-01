import turtle

t = turtle.Turtle()

def triangle():
    t.color("blue")
    for i in range(0,3):
        t.forward(180)
        t.left(120)
        
# triangle()
    
t.left(180)
t.penup()
t.forward(180)
t.pendown()

def square():
    t.color("red")
    for i in range(0,4):
        t.forward(180)
        t.right(90)

square()
t.penup()
t.back(180)
t.pendown()
square()


input()