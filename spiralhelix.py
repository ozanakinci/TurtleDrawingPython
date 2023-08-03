import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("SpiralHelix Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed(0)

turtle_colors = ["red", "purple", "blue", "green", "yellow"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
turtle.done()