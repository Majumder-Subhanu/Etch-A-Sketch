import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def move_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()
