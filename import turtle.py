import turtle
t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')
def heart(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        heart(3*i/4)
        t.right(60)
        heart(3*i/4)
        t.left(30)
        t.backward(i)

heart(100)
turtle.done()        