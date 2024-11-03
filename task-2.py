import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=400):
    window = turtle.Screen()

    t = turtle.Turtle()
    t.speed(3)
    t.penup()
    t.goto(-size / 2, 100)
    t.pendown()

    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.exitonclick()


if __name__ == "__main__":
    while True:
        try:
            order = int(input("Please input recursion number: "))
            if order < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    draw_koch_curve(order)
