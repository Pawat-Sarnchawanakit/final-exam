"""
This module draws beautiful art!
"""
import turtle
import random


class Polygon:
    """
    Helper Class to easily build and draw polygons.
    """

    def __init__(self):
        self.__angle = 0
        self.__col = (0, 0, 0)
        self.__thickness = 1
        self.__start_angle = 0
        self.__length = 0
        self.__pos = (0, 0)

    def internal_angle(self, angle):
        """
        Sets one of the internal angle.
        """
        self.__angle = angle
        return self

    def num_sides(self, num_sides):
        """
        Sets the number of sides of the polygon.
        """
        self.__angle = 360 // num_sides
        return self

    def random_color(self):
        """
        Sets the color of the polygon to be a random rgb color.
        """
        return self.color((random.randint(0, 255), random.randint(0, 255),
                           random.randint(0, 255)))

    def color(self, col):
        """
        Sets the color of the polgyon to be a color `col`
        """
        self.__col = col
        return self

    def thickness(self, thickness):
        """
        Sets the thickness of the line of the polygon.
        """
        self.__thickness = thickness
        return self

    def orientation(self, angle):
        """
        Sets the starting angle of which the polygon is drawn.
        """
        self.__start_angle = angle
        return self

    def length(self, length):
        """
        Sets the length of a side of a polygon.
        """
        self.__length = length
        return self

    def pos(self, x, y):
        """
        Sets the starting pos where the polygon is drawn. (Not the middle position)
        """
        self.__pos = (x, y)
        return self

    def draw(self, count=1, reduction_ratio=0.618):
        """
        Draws the polygon.

        Arguments:
        count: int, number of times to draw.
        reduction_ratio: how the length is mutated, 
            > 1 means it gets bigger, 
            < 1 means it gets smaller.
        """
        for i in range(count):
            turtle.penup()
            turtle.goto(*self.__pos)
            turtle.setheading(self.__start_angle)
            turtle.color(self.__col)
            turtle.pensize(self.__thickness)
            turtle.pendown()
            for _ in range(360 // self.__angle):
                turtle.forward(self.__length)
                turtle.left(self.__angle)
            turtle.penup()
            if i + 1 == count:
                break
            turtle.penup()
            turtle.forward(self.__length * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.__length * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.__length = 0.618 * self.__length
            self.__pos = (turtle.pos()[0], turtle.pos()[1])


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# Main part
art_num = input(
    "Which art do you want to generate? Enter a number between 1 to 8, inclusive: "
)
if art_num == '1':
    for _ in range(25):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(120) \
            .length(random.randint(50, 150)) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .draw()
elif art_num == '2':
    for _ in range(25):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(90) \
            .length(random.randint(50, 150)) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .draw()
elif art_num == '3':
    for _ in range(25):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(72) \
            .length(random.randint(50, 150)) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .draw()
elif art_num == '4':
    for _ in range(25):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .num_sides(random.randint(3, 5)) \
            .length(random.randint(50, 150)) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .draw()
elif art_num == '5':
    for _ in range(20):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(120) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .length(random.randint(50, 150)) \
            .draw(3)
elif art_num == '6':
    for _ in range(20):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(90) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .length(random.randint(50, 150)) \
            .draw(3)
elif art_num == '7':
    for _ in range(20):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(72) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .length(random.randint(50, 150)) \
            .draw(3)
elif art_num == '8':
    for _ in range(20):
        Polygon().random_color() \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .num_sides(random.randint(3, 5)) \
            .pos(random.randint(-300, 300), random.randint(-200, 200)) \
            .length(random.randint(50, 150)) \
            .draw(3)
else:
    print("Invalid choice.")
turtle.done()
