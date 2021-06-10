import turtle
import random
import winsound

p = 0
pz = 0


# April - 2020(PANDEMIC BEGINS)
# FIRST YEAR OF B.TECH(2ND SEMESTER)

def sound():
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


####Window####
win = turtle.Screen()
win.title('PING PONG  - BY ATHARV')
win.setup(height=800, width=800)
win.bgcolor('black')
win.tracer(0)

####Paddle A####
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

####Paddle B####
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

####Ball####
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 1.3
ball.dy = 1.3

####Line Up####
lineup = turtle.Turtle()
lineup.shape('square')
lineup.color('white')
lineup.shapesize(stretch_len=350, stretch_wid=0.5)
lineup.penup()
lineup.goto(0, 270)

####Line Down####
linedown = turtle.Turtle()
linedown.shape('square')
linedown.color('white')
linedown.shapesize(stretch_len=350, stretch_wid=0.5)
linedown.penup()
linedown.goto(0, -260)
player1 = 0
player2 = 0

####Score Board####
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('white')
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 350)
pen1.write('Player A          Player B', align='center', font=('Courier', 30, 'bold'))

upperlimit = 254
rightlimit = 403  # y=104.0000000000004
leftlimit = -410  # y=81.20000000000007
lowerlimit = -246

####Pen A####
pena = turtle.Turtle()
pena.speed(0)
pena.color('white')
pena.penup()
pena.hideturtle()
pena.goto(0, 300)
pena.write(str(str(player1) + '                   '), align='center', font=('Courier', 30, 'bold'))

####Pen B####
penb = turtle.Turtle()
penb.speed(0)
penb.color('white')
penb.penup()
penb.hideturtle()
penb.goto(0, 300)
penb.write('                 ' + str(str(player2)), align='center', font=('Courier', 30, 'bold'))


def adv():
    finish1 = turtle.Turtle()
    finish1.color('white')
    finish1.penup()
    finish1.speed(0)
    finish1.goto(0, -200)
    finish1.hideturtle()
    finish1.write('Created by:Atharv Karbhari(B.Tech First Year)', align='center', font=('Courier', 20, 'bold'))


def paddle_aup():
    y = paddle_a.ycor()
    if y < 151:
        y += 50
    paddle_a.sety(y)


def paddle_adown():
    y = paddle_a.ycor()
    if y > -151:
        y -= 50
    paddle_a.sety(y)


def paddle_bup():
    y = paddle_b.ycor()
    if y < 151:
        y += 50
    paddle_b.sety(y)


def paddle_bdown():
    y = paddle_b.ycor()
    if y > -151:
        y -= 50
    paddle_b.sety(y)


####Keyboard Bindings####
win.listen()
win.onkeypress(paddle_aup, 'w')
win.onkeypress(paddle_adown, 's')
win.onkeypress(paddle_bup, 'Up')
win.onkeypress(paddle_bdown, 'Down')


def finish():
    finish1 = turtle.Turtle()
    finish1.color('white')
    finish1.penup()
    finish1.speed(0)
    finish1.goto(0, 130)
    finish1.hideturtle()
    finish1.write('GAME OVER', align='center', font=('Courier', 80, 'bold'))
    paddle_a.goto(350, 0)
    paddle_b.goto(-350, 0)
    win.listen(False)
    adv()


def result(player):
    rdisplay = turtle.Turtle()
    rdisplay.penup()
    rdisplay.hideturtle()
    rdisplay.speed(0)
    rdisplay.color('white')
    rdisplay.goto(0, 60)
    rdisplay.write(str('Player ' + str(player) + ' has Won!'), align='center', font=('Courier', 40, 'bold'))


while True:
    if pz % 2 == 0:
        win.update()
        if player2 == 10 or player1 == 10:
            if player2 > player1:
                ball.hideturtle()
                ball.goto(0, 0)
                finish()
                result('B')
            else:
                ball.hideturtle()
                ball.goto(0, 0)
                finish()
                result('A')
        ####Moving the ball
        if p == 0:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
        elif p == 1:
            ball.setx(ball.xcor() - ball.dx)
            ball.sety(ball.ycor() - ball.dy)
        elif p == 2:
            ball.setx(ball.xcor() - ball.dx)
            ball.sety(ball.ycor() + ball.dy)
        elif p == 3:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() - ball.dy)

        ######Ball Hitting Above or Below#######
        if ball.ycor() > upperlimit or ball.ycor() < lowerlimit:
            ball.dy *= -1
            sound()

        ######Ball leaving from left or right######
        if ball.xcor() > rightlimit:
            pena.clear()
            player1 += 1
            pena.penup()
            pena.hideturtle()
            pena.goto(0, 300)
            pena.write(str(str(player1) + '                   '), align='center', font=('Courier', 30, 'bold'))
            p = random.randint(0, 3)
            ball.goto(0, 0)
        if ball.xcor() < leftlimit:
            penb.clear()
            player2 += 1
            penb.penup()
            penb.hideturtle()
            penb.goto(0, 300)
            penb.write('                 ' + str(str(player2)), align='center', font=('Courier', 30, 'bold'))
            p = random.randint(0, 3)
            ball.goto(0, 0)

        ####Paddle and Ball####s
        if ball.xcor() > 330 and ball.xcor() < 351 and ball.ycor() <= paddle_b.ycor() + 50 and ball.ycor() >= paddle_b.ycor() - 50:
            ball.setx(330)
            ball.dx *= -1

        if ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() <= paddle_a.ycor() + 50 and ball.ycor() >= paddle_a.ycor() - 50:
            ball.setx(-330)
            ball.dx *= -1
    else:
        continue
