import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Animation")

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 200)

# Set the ball's initial speed and direction
ball.dx = 2
ball.dy = -2

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Update the screen
    wn.update()
