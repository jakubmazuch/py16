import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(1)

for _ in range(4):
    t.forward(100)
    t.left(90)

t.screen.mainloop()
