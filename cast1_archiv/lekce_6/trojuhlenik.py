import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(1)

for _ in range(3):
    t.forward(100)
    t.left(120)

t.screen.mainloop()
