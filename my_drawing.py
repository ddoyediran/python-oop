from shapes import Paper, Triangle, Rectangle, Oval

# Instance of paper
paper = Paper()

# instance of the rectangle
rect1 = Rectangle()
rect2 = Rectangle()
oval1 = Oval()
triangle = Triangle(0,0,20,0,40,40,color="black")

# Attributes
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")


rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")

oval1.randomize(smallest=20, largest=200)

# setting the position of the rect1
rect2.set_y(100)
rect2.set_x(100)


# draw the rectangle on paper
rect1.draw()
rect2.draw()
oval1.draw()
triangle.draw()

# to display the shape on the paper
paper.display()
