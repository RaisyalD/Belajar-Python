import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('#ffffff')
t.width(2)
t.speed(15)

col=('yellow','navy','black')

for i in range (300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
turtle.done()