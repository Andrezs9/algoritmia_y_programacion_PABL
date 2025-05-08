import turtle

espiral = turtle.Turtle()
turtle.bgcolor("black")  
espiral.pensize(1)  
espiral.speed(0)
espiral.color("red")

for i in range(10, 600, 2):
    for _ in range(3):
        espiral.forward(i)
        espiral.left(120)
    espiral.right(10)

#p 
t=turtle.Turtle()
t.speed(3)
t.shape("triangle")
t.color("#8A2BE2")
t.pensize(10)
t.penup()
t.goto(-529,-100)
t.pendown()
t.lt(90)
t.fd(140)
t.penup()
t.goto(-450,20)
t.pendown()
t.circle(40)

# a
t.color("#8B008B")
t.penup()
t.goto(-380,-60)
t.pendown()
t.circle(40)
t.down()
t.lt(180)
t.pendown()
t.fd(45)

# u
t.color("#4B0082")
t.penup()
t.goto(-360,-25)
t.pendown()
t.fd(65)
t.left(30)
t.circle(30, 120)
t.left(30)
t.fd(65)

#l
t.color("#6A5ACD")
t.penup()
t.goto(-270,20)
t.left(180)
t.pendown()
t.fd(125)

# o
t.color("#483D8B")
t.penup()
t.goto(-250,-65)
t.pendown()
t.circle(40)

t.color("#FFE4C4")
t.penup()
t.goto(300,30)
t.pendown()
t.fd(30)

t.penup()
t.goto(260,30)
t.pendown()
t.fd(30)

t.penup()
t.goto(250,-20)
t.pendown()
t.circle(30, 180)

t.penup()
t.goto(600,-30)


turtle.done()