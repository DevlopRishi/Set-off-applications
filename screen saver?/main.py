import turtle
import random

# Initialize turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Random Things")

pen = turtle.Turtle()
pen.speed(0)  # Maximum speed
pen.width(2)

# Color palette
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "white"]

# Random shape generator function
def draw_random_shape():
    sides = random.randint(3, 10)  # Random polygon sides (3-10)
    size = random.randint(20, 100)  # Random size of the shape
    angle = 360 / sides
    pen.color(random.choice(colors))
    for _ in range(sides):
        pen.forward(size)
        pen.right(angle)

# Goofy pattern generator
def generate_pattern():
    for _ in range(50):  # Number of shapes
        pen.penup()
        pen.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
        pen.pendown()
        draw_random_shape()
        pen.right(random.randint(0, 360))  # Random orientation

# Start generating the pattern
generate_pattern()

# Close the turtle graphics window on click
screen.mainloop()