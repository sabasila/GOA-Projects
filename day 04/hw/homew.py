import turtle


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("blue")
palace_turtle = turtle.Turtle()
palace_turtle.speed(3)


def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw the palace
def draw_palace():
    # Main building
    palace_turtle.penup()
    palace_turtle.goto(-100, -100)
    palace_turtle.pendown()
    draw_rectangle(palace_turtle, 200, 150, "lightgrey")

character_turtle = turtle.Turtle()
character_turtle.speed(3)


def draw_character(x, y, color):
    character_turtle.penup()
    character_turtle.goto(x, y)
    character_turtle.pendown()
    character_turtle.color(color)
    character_turtle.begin_fill()
    character_turtle.circle(20)
    character_turtle.end_fill()
    character_turtle.penup()
    character_turtle.goto(x, y - 20)
    character_turtle.pendown()
    character_turtle.right(90)
    character_turtle.forward(40)
    character_turtle.backward(20)
    character_turtle.left(45)
    character_turtle.forward(20)
    character_turtle.backward(20)
    character_turtle.right(90)
    character_turtle.forward(20)
    character_turtle.backward(20)
    character_turtle.left(45)
    character_turtle.forward(20)

# Create the turtle for drawing the flag
flag_turtle = turtle.Turtle()
flag_turtle.speed(3)

# Function to draw the flag
def draw_flag():
    flag_turtle.penup()
    flag_turtle.goto(125, 50)
    flag_turtle.pendown()
    flag_turtle.color("black")
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.right(90)
    flag_turtle.color("orange")
    flag_turtle.begin_fill()
    for _ in range(3):
        flag_turtle.forward(30)
        flag_turtle.right(120)
    flag_turtle.end_fill()

# Draw the palace, king, queen, and flag
draw_palace()
draw_character(-50, -100, "blue")  # King
draw_character(50, -100, "red")  # Queen
draw_flag()

# Hide turtles
palace_turtle.hideturtle()
character_turtle.hideturtle()
flag_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
