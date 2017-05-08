import turtle

#background color for screen
window = turtle.Screen()
window.bgcolor("black")

#shape of turtle, color for turtle and lines
frank = turtle.Turtle()
frank.shape("turtle")
frank.color("red")
frank.speed(10)

#drawing a triangle
def draw_square():
	sides = 4
	for angle in range(sides):
		frank.forward(100)
		frank.right(90)

#drawing a flower
def draw_flower():
	for petal in range(36):
		draw_square()
		frank.right(10)

#drawing the stem
	frank.right(90)
	frank.forward(200)


	window.exitonclick()

draw_flower()