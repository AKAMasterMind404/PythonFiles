import turtle

win=turtle.Screen()
win.title('Chain Reaction')
win.bgcolor('black')
win.setup(1000,1000)

def ball(x,y):
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shapesize(stretch_len=1.5,stretch_wid=1.5)
    ball.shape('circle')
    ball.color('red')
    ball.penup()
    ball.goto(x,y)

def ballinsert(y,x,wanted):
    fixed=-370
    a=None
    b=None
    c=None
    if wanted>0:
        a=ball(fixed+80*x,-(fixed+80*y))
    if wanted>1:
        b=ball((fixed+20)+80*x,-(fixed+80*y))
    if wanted>2:
        c=ball((fixed+10)+80*x,-((fixed+20)+80*y))

####GRID####
x=-400
for i in range(0,11):
    ##vertical lines
    linea=turtle.Turtle()
    linea.speed(0)
    linea.penup()
    linea.shape('square')
    linea.color('white')
    linea.shapesize(stretch_wid=40.1,stretch_len=0.2)
    linea.goto(x,0)

    ##horizontal lines
    lineb = turtle.Turtle()
    lineb.speed(0)
    lineb.penup()
    lineb.shape('square')
    lineb.color('white')
    lineb.shapesize(stretch_wid=0.2, stretch_len=40.1)
    lineb.goto(0,x)

    x +=80

######Key Bindings#########

##########GRID COMPLETE#################
win.listen()
ballinsert(2,2, 3)
while True:
    win.update()
