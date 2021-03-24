import turtle

# Screen
wn = turtle.Screen()
wn.title("Turtle by Yuriy Hrabovenskyi")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

# My cute turtle
my_cute_turtle = turtle.Turtle()
my_cute_turtle.color("black")
my_cute_turtle.shape("turtle")
my_cute_turtle.penup()
my_cute_turtle.goto(0, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("My cute turtle", align="center", font=("Courier", 24, "normal"))

DELTA = 5

# Functions
def my_cute_turtle_up():
    y = my_cute_turtle.ycor()
    y += DELTA
    if y < 300:
        my_cute_turtle.sety(y)
    else:
        my_cute_turtle.sety(-300)
    my_cute_turtle.setheading(90)
    turtle.ontimer(my_cute_turtle_up(), 10)


def my_cute_turtle_down():
    y = my_cute_turtle.ycor()
    y -= DELTA
    if y > -300:
        my_cute_turtle.sety(y)
    else:
        my_cute_turtle.sety(300)
    my_cute_turtle.setheading(270)
    turtle.ontimer(my_cute_turtle_down(), 10)


def my_cute_turtle_left():
    x = my_cute_turtle.xcor()
    x -= DELTA
    if x < 0:
        my_cute_turtle.color("brown")
    if x > -400:
        my_cute_turtle.setx(x)
    else:
        my_cute_turtle.setx(400)
        my_cute_turtle.color("green")
    my_cute_turtle.setheading(180)
    turtle.ontimer(my_cute_turtle_left(), 10)


def my_cute_turtle_right():
    x = my_cute_turtle.xcor()
    x += DELTA
    if x > 0:
        my_cute_turtle.color("green")
    if x < 400:
        my_cute_turtle.setx(x)
    else:
        my_cute_turtle.setx(-400)
        my_cute_turtle.color("brown")
    my_cute_turtle.setheading(0)
    turtle.ontimer(my_cute_turtle_right(), 10)


wn.listen()
wn.onkey(my_cute_turtle_up, 'Up')
wn.onkey(my_cute_turtle_left, 'Left')
wn.onkey(my_cute_turtle_right, 'Right')
wn.onkey(my_cute_turtle_down, 'Down')

wn.mainloop()
