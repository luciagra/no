5# Your name: Lucia Grasso
# Your student id: 21450074
# Your email: luciagra@umich.edu
# Asked genAI hints for debugging and suggesting the general structure of the code

import turtle

def draw_fishbody(t, color, x, y):
    t.speed(5)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(50)  # radius 30
    t.end_fill()

def draw_fishtail(t, color, x, y):
    t.speed(5)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.right(90)
    for i in range(3):
        t.left(120)
        t.forward(50)
    t.end_fill()

def draw_fisheye(t, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(10)  # radius 30
    t.end_fill()

def draw_rectangle(t, color, x, y):
    t.speed(5)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):  # loop for rectangle
        t.forward(800)
        t.left(90)
        t.forward(500)
        t.left(90)
    t.end_fill()

def draw_triangle(t, color, x, y):
    t.speed(10)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):  # loop for triangle
        t.forward(60)
        t.left(120)
    t.end_fill()

def draw_treasurechest(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#A52A2A")
    t.begin_fill()
    for _ in range(2):  # loop for rectangle
        t.forward(150)
        t.left(90)
        t.forward(70)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x, y + 70)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(2):  # loop for rectangle
        t.forward(150)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

def draw_star(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("yellow")
    t.pensize(9)
    for _ in range(5):
        t.forward(80)
        t.right(144)
    t.end_fill()


def draw_l(t, color, x, y):
    t.speed(1)
    t.pensize(5)

    t.penup()
    t.goto(x, y)   # start top of L
    t.pendown()
    t.pencolor(color)

    # Draw vertical line
    t.setheading(-90)  # face down
    t.forward(60)

    # Draw horizontal base
    t.setheading(0)  # face right
    t.forward(40)


def draw_g(t, color, x, y):
    t.speed(1)
    t.pensize(5)

    t.penup()
    t.goto(x, y)   # start top-left of G
    t.pendown()
    t.pencolor(color)
    t.left(180)
    # Draw a square-like C
    for _ in range(3):
        t.forward(50)
        t.left(90)

    # Move into middle and draw small horizontal line (the "bar" of G)
    t.forward(25)
    t.left(90)
    t.forward(25)


# 2. Aquarium scene
def draw_aquarium(t):
    # Background rectangle for aquarium tank
    draw_rectangle(t, "blue", -425, -200)
    
    # Fish made of circles
    draw_fishbody(t, "orange", -200, 0)
    draw_fishbody(t, "red", 0, 100)
   
    draw_fishtail(t, "orange", -150, 25)
    t.left(90)
    draw_fishtail(t, "red", 50, 125)

    draw_fisheye(t, "black", -220, 60)
    draw_fisheye(t, "black", -27, 165)


    # Plants made of triangles
    t.left(90)
    draw_triangle(t, "green", -400, -200)
    draw_triangle(t, "green", -350, -200)
    draw_triangle(t, "green", -300, -200)
    draw_triangle(t, "green", -250, -200)
    draw_triangle(t, "green", -200, -200)
    draw_triangle(t, "green", -150, -200)
    draw_triangle(t, "green", -100, -200)
    draw_triangle(t, "green", -50, -200)
    draw_triangle(t, "green", 0, -200)
    draw_triangle(t, "green", 50, -200)
    draw_triangle(t, "green", 100, -200)
    draw_triangle(t, "green", 150, -200)
    draw_triangle(t, "green", 200, -200)
    draw_triangle(t, "green", 250, -200)
    draw_triangle(t, "green", 300, -200)
    
    draw_treasurechest(t, 200, -150)

    draw_star(t, -160, -130)

    #draw initials
    draw_l(t, "black", 200, -250)
    draw_g(t, "black", 300, -250)


# 4. Main function
def main():
    screen = turtle.Screen()
    screen.bgcolor("#ADD8E6")
    t = turtle.Turtle()
    t.speed(5)

    draw_aquarium(t)

    screen.exitonclick()

# Run the program
if __name__ == "__main__":
    main()
