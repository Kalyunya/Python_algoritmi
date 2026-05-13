import turtle


def koch_curve(t, order, size):

    # Базовий випадок
    if order == 0:
        t.forward(size)

    else:

        size /= 3

        koch_curve(t, order - 1, size)

        t.left(60)

        koch_curve(t, order - 1, size)

        t.right(120)

        koch_curve(t, order - 1, size)

        t.left(60)

        koch_curve(t, order - 1, size)


def draw_koch_snowflake(order, size):

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    # Позиція старту
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо 3 сторони
    for _ in range(3):

        koch_curve(t, order, size)

        t.right(120)

    turtle.done()


# Рівень рекурсії від користувача
level = int(input("Введіть рівень рекурсії: "))

draw_koch_snowflake(level, 300)