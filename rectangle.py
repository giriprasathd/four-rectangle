import turtle
import math
def drawRectangle(t, width, height, color):
	t.fillcolor(color)
	t.begin_fill()
	t.forward(width)
	t.left(90)
	t.forward(height)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.forward(height)
	t.left(90)
	t.end_fill()
screen = turtle.Screen ( )
screen.bgcolor("skyblue")
tip = turtle.Turtle()
tip.color ("black")
tip.shape ("turtle")
tip.speed (2)
drawRectangle(tip, 200, -100, "yellow")
drawRectangle(tip, 200, 100, "brown")
drawRectangle(tip, -200, -100, "violet")
drawRectangle(tip, -200, 100, "green")





