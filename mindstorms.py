import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.right(90)
        some_turtle.forward(100)

def draw_circle(t):
    t.circle(100)
window = turtle.Screen()
window.bgcolor("red")

b = turtle.Turtle()
b.color('maroon')
b.shape("turtle")
b.speed(80)
for i in range(39):
    draw_circle(b)
    b.right(10)

brad = turtle.Turtle()
brad.color('maroon')
brad.shape("turtle")
brad.speed(80)
for i in range(36):
    draw_square(brad)
    brad.right(10)


window.exitonclick()
