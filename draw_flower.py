import turtle

#background color for screen
window = turtle.Screen()
window.bgcolor("black")

#shape of turtle, color for turtle and lines
frank = turtle.Turtle()
frank.shape("arrow")
frank.color("blue")
frank.speed(5)


#drawing a triangle
def draw_isosceles():
	frank.forward(100) #leg
	frank.left(150) #30 degrees
	frank.forward(100) #leg
	frank.left(105) #75 degrees
	frank.forward(52) #base

#drawing a flower
def draw_flower():
	for petal in range(36):
		draw_isosceles()
		frank.right(5)

#drawing the stem
	frank.right(90)
	frank.forward(200)


	window.exitonclick()

draw_flower()