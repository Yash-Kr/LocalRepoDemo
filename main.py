from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()

my_turtle.shape("turtle")
colormode(255)


# colors = ["dodger blue", "lime", "orange red", "indigo", "spring green", "dim gray", "crimson","indian red","medium "
#                                                                                                             "slate "
#                                                                                                             "blue"]
#
def random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # create a tuple and then return it
    mytuple = (r, g, b)
    return mytuple


#
#
# directions = [0, 90, 180, 270]
#
# my_turtle.pensize(15)
my_turtle.speed("fastest")
#
# for i in range(200) :
#     my_turtle.color(random_color())
#     my_turtle.seth(random.choice(directions))
#     my_turtle.forward(30)

def print_spiro(gap_size):
    for _ in range(int(360/gap_size)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.seth(my_turtle.heading() + gap_size )

print_spiro(5)


screen = Screen()
screen.exitonclick()
