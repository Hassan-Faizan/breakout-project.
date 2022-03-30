import random
import turtle
from random import randint

S_HEIGHT = 550
S_WIDTH = 800

# Screen
s = turtle.Screen()
s.title('breakout')
s.setup(S_WIDTH, S_HEIGHT)
s.tracer(0)

# paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.goto(0, (S_HEIGHT/2 - 20) * -1)
paddle.shape('square')
paddle.shapesize(1, 8)

# ball
ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.goto(0, -(S_HEIGHT/2 - 100))
ball.dx = random.choice([-3, -2, -1, 1, 2, 3])
ball.dy = 2
ball.score = 0

# score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.goto(0, S_HEIGHT/2-50)
pen.write(f'Score: {ball.score}', align='center', font=('Arial', 25, 'normal'))

# bricks
y_cor = S_HEIGHT / 2 - 50
brick_no = -1
bricks = []
for n in range(4):
    x_cor = -(S_WIDTH / 2 - 50)
    y_cor -= 50
    for i in range(int(S_WIDTH/90)):
        x_cor += 80
        brick_no += 1
        new_brick = 'brick' + str(brick_no)
        bricks.append(new_brick)
        bricks[brick_no] = turtle.Turtle()
        bricks[brick_no].penup()
        bricks[brick_no].shape('square')
        bricks[brick_no].shapesize(1.5, 3)
        bricks[brick_no].color('black', 'grey')
        bricks[brick_no].goto((x_cor, y_cor))


# paddles
def paddle_right():
    if paddle.xcor() > 300:
        return
    new_x = paddle.xcor() + 20
    paddle.setx(new_x)


def paddle_left():
    if paddle.xcor() < -300:
        return
    
    new_x = paddle.xcor() - 20
    paddle.setx(new_x)


s.listen()
s.onkeypress(paddle_right, 'Right')
s.onkeypress(paddle_left, 'Left')

# Start
game_is_on = True
while game_is_on:
    s.update()
    # time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colliding with walls
    if ball.ycor() >= S_HEIGHT/2-10:
        ball.dy *= -1
    elif ball.xcor() >= S_WIDTH/2-10:
        ball.dx *= -1
    elif ball.xcor() <= -(S_WIDTH/2-10):
        ball.dx *= -1
    elif ball.ycor() < -(S_HEIGHT/2):
        game_is_on = False
        pen.clear()
        pen.goto(0, 0)
        pen.write(f'Score: {ball.score}', align='center', font=('Arial', 85, 'normal'))

    # paddle collision
    elif paddle.ycor()+10 <= ball.ycor() <= paddle.ycor()+20 and paddle.xcor()-80 <= ball.xcor() <= paddle.xcor()+80:
        ball.dy *= -1

    # collision with bricks
    else:
        for brick in bricks:
            if brick.ycor()+15 >= ball.ycor() >= brick.ycor()-20 and (brick.pos()[0] - 30) < ball.xcor() < brick.xcor() + 30:
                ball.dy *= -1
                brick.goto(1000, 1000)
                bricks.remove(brick)
                ball.score += 1
                pen.clear()
                pen.write(f'Score: {ball.score}', align='center', font=('Arial', 25, 'normal'))


s.exitonclick()
