import turtle
t = turtle.Turtle()

n = int(input("Kolika úhleník chceš namalovat? "))


if n > 2:
    t.shape("turtle")
    t.color("green")
    t.speed(1)
    for _ in range(n):                        
        t.forward(500/n)
        t.left(360/n)
    t.screen.mainloop()
else:
    print("Chybný vstup")
