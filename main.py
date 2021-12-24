import turtle
import random

web_based = True

if web_based:
    i_scale = 1.5
    snow_size = 4
    snow_speed = 3
    draw_speed = 10
    rate_of_snow_balls = 9
else:
    i_scale = 1
    snow_size = 7
    snow_speed = 2
    draw_speed = 10
    rate_of_snow_balls = 2

width = 600 / i_scale
height = 600 / i_scale

screen = turtle.Screen()
if not web_based:
    screen.setup(width, height)
    screen.title("Merry Christmas from Vin Busquet")


def make_triangle(x, y, size, outline, triangle):
    triangle.hideturtle()
    triangle.penup()
    triangle.setposition(x, y)
    triangle.pensize(3)
    if outline:
        triangle.pendown()
    if not outline:
        triangle.fillcolor("forest green")
        triangle.begin_fill()
    triangle.setposition(x + size, y - size)
    triangle.setposition(x - size, y - size)
    triangle.setposition(x, y)
    if not outline:
        triangle.end_fill()

def make_star():
  pass
def make_ball(x, y, size, colour, ball):
    ball.hideturtle()
    ball.penup()
    ball.setposition(x, y)
    ball.color(colour)
    ball.dot(size)


def move_snow(snow):
    position = snow.position()
    snow.clear()
    make_ball(position[0], position[1] - snow_speed, snow_size, "white", snow)


def snow_fall():
    rand_make_snow = random.randint(0, rate_of_snow_balls)
    if rand_make_snow == 0:
        snow = turtle.Turtle()
        snow.hideturtle()
        snow.penup()
        list_of_snow.append(snow)
        make_ball(random.randint(-width / 2, width / 2), width / 2, snow_size,
                  "white", snow)
    for snow in list_of_snow:
        move_snow(snow)
        if snow.position()[1] <= -width / 2:
            snow.clear()
            list_of_snow.remove(snow)
            del snow
    screen.update()


# Make tree (main part)
triangle_1 = turtle.Turtle()
triangle_1.speed(draw_speed)
outline = True
for repeat in range(2):
    make_triangle(0, width / 3, width / 6, outline, triangle_1)
    make_triangle(0, width / 4, width / 4, outline, triangle_1)
    make_triangle(0, width / 8, width / 3, outline, triangle_1)
    outline = False

screen.tracer(0)
stem = turtle.Turtle()
# Snow ground
stem.penup()
stem.hideturtle()
stem.setposition(-width, -width / 3)
stem.color("white")
stem.begin_fill()
stem.setposition(width, -width / 3)
stem.setposition(width, -width / 2)
stem.setposition(-width, -width / 2)
stem.end_fill()
screen.update()

# tree stem
stem.color("brown")
stem.setposition(-width / 30, -width / 4.8)
screen.tracer(1)
stem.pendown()
stem.begin_fill()
stem.setposition(width / 30, -width / 4.8)
stem.setposition(width / 30, -3 * width / 8)
stem.setposition(-width / 30, -3 * width / 8)
stem.setposition(-width / 30, -width / 4.8)
stem.end_fill()

screen.bgcolor("sky blue")

# Decorations: balls
screen.tracer(2)
# All available ball colors
ball_colours = ["orange", "blue", "red", "gold", "violet", "white"]
ball_positions = [(-width / 30, width / 4), (3 * width / 40, width / 5),
                  (-width / 20, width / 6), (width / 30, width / 9),
                  (-width / 12, width / 30), (width / 12, width / 24),
                  (-width / 9, -width / 20), (width / 8, -width / 15),
                  (0, -width / 6), (-width / 6, -width / 6),
                  (width / 5, -width / 7.5)
                  ]
for position in ball_positions:
    make_ball(position[0], position[1], 20 / i_scale,
              random.choice(ball_colours),
              turtle.Turtle())
    screen.update()
    
# Create a star a top of tree
stem.speed(2)
stem.penup()
stem.color('yellow')
stem.goto(-width/20, width/2.6)
stem.begin_fill()
stem.pendown()
for i in range(5):
    stem.forward(40)
    stem.right(144)
stem.end_fill()

# snow is falling…
list_of_snow = []

screen.tracer(0)
for _ in range(50):
    snow_fall()

text_1 = turtle.Turtle()
text_1.hideturtle()
text_1.penup()
text_1.setposition(0, width / 2.4)
text_1.color("red")
text_1.write("Merry Christmas",
             font=("Apple Chancery", max(int(30 / i_scale), 15), "bold"),
             align="center")

for _ in range(25):
    snow_fall()

text_1.setposition(0, -width / 2.4)
text_1.color("black")

text_1.write("from",
             font=("Apple Chancery", max(int(20 / i_scale), 10), "normal"),
             align="center")
if web_based:
    text_1.setposition(0, -width / 2.05)
else:
    text_1.setposition(0, -width / 2.05)

text_1.color("#2ca8ff")
text_1.write("</> | VIN BUSQUET", font=("Arial", max(int(25 / i_scale), 15), "normal"),
             align="center")

if web_based:
    for _ in range(10000):
        snow_fall()
else:
    while True:
        snow_fall()

turtle.done()