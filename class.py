class Point:
    def __init__(self, x, y):
        self.x = x #self references to the current object
        self.y = y

    def move(self):
        print("nove")

    def draw(self):
        print("draw")


point1 = Point(10, 20) #10 refers to x and 20 refers to y respectively

#point1.x = 10 #create attribute (can set anywhere in the program)
#point1.y = 20 #create attribute (can set anywhere in the program)
point1.draw()
print(point1.x)