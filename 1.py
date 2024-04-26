import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Game")
wn.setup(width=600, height=600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 260)
ball.dx = 2
ball.dy = -2

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.speed(0)
paddle.goto(0, -250)

# Functions to move the paddle left and right
def paddle_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

def paddle_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Bounce off the paddle
    if (
        ball.ycor() < -240
        and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50
    ):
        ball.dy *= -1

    # Check if the ball fell off the screen
    if ball.ycor() < -290:
        # Reset the ball position
        ball.goto(0, 260)
        ball.dy = -2

    # Update the screen
    wn.update()
