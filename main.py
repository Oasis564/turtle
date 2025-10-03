import turtle

t = turtle.Turtle()

# def triangle():
#     t.color("blue")
#     for i in range(0,3):
#         t.forward(180)
#         t.left(120)
        
# triangle()
    
# t.left(180)
# t.penup()
# t.forward(180)
# t.pendown()

# def square():
#     t.color("red")
#     for i in range(0,4):
#         t.forward(180)
#         t.left(90)

# for s in range(0,100):      
#     square()
#     t.right(10)

t.pendown()

def circle():
    t.color("blue")
    for d in range(0,360):
        t.forward(1)
        t.right(1)
    
circle()

input()