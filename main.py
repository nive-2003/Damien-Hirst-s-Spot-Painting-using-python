import random
import turtle as t
import colorgram
t.speed("fastest")
t.penup()
t.hideturtle()
# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r,g,b)
#     rgb_colors.append(rgb_color)
rgb_colors = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31),
              (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

t.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)
for count_of_dots in range(1,101):
    t.dot(20,random.choice(rgb_colors))
    t.forward(50)
    if count_of_dots % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


my_screen = t.Screen()
my_screen.exitonclick()