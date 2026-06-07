import turtle


def draw_tree(length, level):
    if level == 0:
        return
    t.forward(length)

    t.left(45)
    draw_tree(length * 0.7, level - 1)

    t.right(90)
    draw_tree(length * 0.7, level - 1)

    t.left(45)
    t.backward(length)



screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
level = int(input("Введіть рівень рекурсії: "))
t.left(90)
draw_tree(100, level)
screen.mainloop()



