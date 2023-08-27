from turtle import Turtle, Screen
tim = Turtle()


def intro():
    tim.shape("turtle")
    tim.color("green")
    tim.down()

def reset():
    tim.reset()
    intro()


def step_forward():
    tim.forward(20)

def step_backward():
    tim.backward(20)

def turn_left():
    tim.left(30)

def turn_right():
    tim.right(30)

def stop_drawing():
    tim.up()

def resume_drawing():
    tim.down()
intro()
my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=step_forward)
my_screen.onkey(key="s", fun=step_backward)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="f", fun=stop_drawing)
my_screen.onkey(key="r", fun=resume_drawing)
my_screen.onkey(key="c", fun=reset)
my_screen.exitonclick()