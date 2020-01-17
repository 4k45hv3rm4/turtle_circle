# turtle_circle
A flower like circle using turtle library in python
Above file contains the code for drawing a flower shape circle in `python` language using `turtle` library  
```python
#import library
import turtle


#make a function to draw square
def draw_square(some_turtle):
    for i in range(4):
        some_turtle.right(90)
        some_turtle.forward(100)
        
#make a function to draw circle 
def draw_circle(t):
    t.circle(100)

#Initialize a window screen 
window = turtle.Screen()

#add color to the screen 
window.bgcolor("red")

#Initialize turtle with name b
b = turtle.Turtle()
b.color('maroon')
b.shape("turtle")
b.speed(80)
for i in range(39):
    draw_circle(b)
    b.right(10)
    
#Initialize turtle with name brad
brad = turtle.Turtle()
brad.color('maroon')
brad.shape("turtle")
brad.speed(80)
for i in range(36):
    draw_square(brad)
    brad.right(10)

#Exit window screem when done 
window.exitonclick()

```
