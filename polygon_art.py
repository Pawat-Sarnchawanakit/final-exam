import turtle
import random

class Color:
    def random():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Polygon:
    def internal_angle(self, angle):
        self.__angle = angle;
        return self;
    def color(self, col):
        self.__col = col;
        return self;
    def thickness(self, thickness):
        self.__thickness = thickness;
        return self;
    def orientation(self, angle):
        self.__start_angle = angle;
        return self;
    def length(self, length):
        self.__length = length;
        return self;
    def draw(self, x, y):
        turtle.penup();
        turtle.goto(x, y)
        turtle.setheading(self.__start_angle)
        turtle.color(self.__col)
        turtle.pensize(self.__thickness)
        turtle.pendown()
        for _ in range(360//self.__angle):
            turtle.forward(self.__length)
            turtle.left(self.__angle)
        turtle.penup()

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618

# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# # adjust the size according to the reduction ratio
# size *= reduction_ratio

# # draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# # hold the window; close it by clicking the window close 'x' mark

art_num = input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: ")
if art_num == '1':
    for _ in range(25):
        Polygon().color(Color.random()) \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(120) \
            .length(random.randint(50, 150)) \
            .draw(random.randint(-300, 300), random.randint(-200, 200));
elif art_num == '2':
    for _ in range(25):
        Polygon().color(Color.random()) \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(90) \
            .length(random.randint(50, 150)) \
            .draw(random.randint(-300, 300), random.randint(-200, 200));
elif art_num == '3':
    for _ in range(25):
        Polygon().color(Color.random()) \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(72) \
            .length(random.randint(50, 150)) \
            .draw(random.randint(-300, 300), random.randint(-200, 200));
elif art_num == '4':
    for _ in range(25):
        Polygon().color(Color.random()) \
            .thickness(random.randint(1, 10)) \
            .orientation(random.randint(0, 90)) \
            .internal_angle(360//random.randint(3, 5)) \
            .length(random.randint(50, 150)) \
            .draw(random.randint(-300, 300), random.randint(-200, 200));
elif art_num == '5':
    for _ in range(20):
        polygon = Polygon().color(Color.random()) \
                .thickness(random.randint(1, 10)) \
                .orientation(random.randint(0, 90)) \
                .internal_angle(360//random.randint(3, 5));
        x, y = random.randint(-300, 300), random.randint(-200, 200)
        length = random.randint(50, 150);
        for _ in range(3):
                polygon.length(length) \
                    .draw(x, y);
                length *= 0.618;
turtle.done()

