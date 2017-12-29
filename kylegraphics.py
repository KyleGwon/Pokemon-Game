from graphics import *
import time
import random

class Greg:
	def __init__(self, win, width, height):
		self.win = win
		self.width = width
		self.height = height
		p1 = Point(random.randint(0,self.width), random.randint(0,self.height))
		p2 = Point(random.randint(p1.getX(),self.width), random.randint(p1.getY(), self.height))
		colors = ["red", "blue", "yellow"]
		rectangle = Rectangle(p1,p2)
		rectangle.setFill(random.choice(colors))
		rectangle.draw(self.win)
		self.shapes = []
		self.shapes.append(rectangle)
	def addShape(self, shape):
		self.shapes.append(shape)
	def getShapes(self):
		return self.shapes

def main():
	height = 300
	width = 800
	win = GraphWin("kyle learning", width, height)

	p1 = Point(0, 200)
	p2 = Point(200, 0)

	# p1xcord = p1.getX()
	# print (p1)


	#rectangle = Rectangle(p1, p2)

	#rectangle.setFill("green")
	#rectangle.setOutline("black")
	#rectangle.draw(win)

	# pX = (p1.getX() + p2.getX()) / 2
	# pY = (p1.getY() + p2.getY()) / 2
	# p = Point(pX, pY)
	# nametext = Text(p, "Bobby Squarey")
	# nametext.draw(win)




	# p = Point(500, 600)
	# textbox = Text(p, "Greg")
	# textbox.draw(win)

	while True:
		key = win.getKey()
		if key == "Right":
			for i in greg.getShapes():
				i.move(10, 0)
		elif key == "Left":
			for i in greg.getShapes():
				i.move(-10, 0)
		elif key == "Up":
			for i in greg.getShapes():
				i.move(0, -10)
		elif key == "Down":
			for i in greg.getShapes():
				i.move(0, 10)
		elif key == "g":
			greg = Greg(win,width,height)
			sqaure = Rectangle(Point(200,250),Point(250,300))
			sqaure.setFill("red")
			sqaure.draw(win)
			greg.addShape(sqaure)
		elif key == "Escape":
			win.close()
		else:
			p = Point(400, 150)
			textbox = Text(p, key + " couldn't move the rectangle, but instead created this text!")
			textbox.draw(win)
			time.sleep(2)
			textbox.undraw()
	return



main()