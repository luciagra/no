# Author: Lucia Grasso
# date 9/10/25
# assignment: discussion 3 emoji

import turtle

### write all new functions here ###



def draw_emoji(t):
    """
    Write a function to draw an emoji.
    """

    t.speed(5)
    t.pensize(3)

    t.penup()
    t.goto(0,-100)
    t.pendown()
    t.color("#FF0000")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-30,20)
    t.pendown()
    t.color("#000000")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(30,20)
    t.pendown()
    t.color("#000000")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(-50, -40)
    t.pendown()
    t.pensize(10)
    t.color("black")
    t.forward(100)

    t.penup()
    t.goto(20, 50)
    t.pendown()
    t.left(45)
    t.pensize(10)
    t.color("black")
    t.forward(35)

    t.penup()
    t.goto(-20, 50)
    t.pendown()
    t.left(90)
    t.pensize(10)
    t.color("black")
    t.forward(35)

    

def main():
    """

    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """

    screen = turtle.Screen()
    screen.title("Emoji Drawing with Turtle")
    screen.bgcolor()

    t = turtle.Turtle()
    draw_emoji(t)

    screen.exitonclick()

if __name__ == '__main__':
    main()


