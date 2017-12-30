from graphics import *
import time
import random


class RedTank:
	def __init__(self, win, rTankDimensions, ):
		self.win = win
		self.rTankWidth = rTankDimensions[0]
		self.rTankHeight = rTankDimensions[1]
		self.rShapes = []
		rP1 = Point(0, self.win.getHeight() - self.rTankHeight)
		rP2 = Point(self.rTankWidth, self.win.getHeight())
		rRectangle = Rectangle(rP1, rP2)
		rRectangle.setFill("red")
		rRectangle.draw(win)
		self.rShapes.append(rRectangle)
		cP1 = Point(self.rTankWidth/2, rP1.getY() + self.rTankHeight/2 - self.rTankHeight/10)
		cP2 = Point(cP1.getX() + self.rTankWidth, cP1.getY() + self.rTankHeight/5)
		rCannon = Rectangle(cP1, cP2)
		rCannon.setFill("black")
		rCannon.draw(win)
		self.rShapes.append(rCannon)
	def getRShapes(self):
		return self.rShapes
	def upperYCord(self):
		return self.rShapes[0].getP1().getY()
	def lowerYCord(self):
		return self.rShapes[0].getP2().getY()
	def upperCannonXCord(self):
		return self.rShapes[1].getP1().getX()
	def upperCannonYCord(self):
		return self.rShapes[1].getP1().getY()
	def lowerCannonXCord(self):
		return self.rShapes[1].getP2().getX()
	def lowerCannonYCord(self):
		return self.rShapes[1].getP2().getY()
class BlueTank:
	def __init__(self, win, bTankDimensions):
		self.win = win
		self.bTankWidth = bTankDimensions[0]
		self.bTankHeight = bTankDimensions[1]
		self.bShapes = []
		bP1 = Point(self.win.getWidth() - self.bTankWidth, 0)
		bP2 = Point( self.win.getWidth(), self.bTankHeight)
		bRectangle = Rectangle(bP1, bP2)
		bRectangle.setFill("blue")
		bRectangle.draw(win)
		self.bShapes.append(bRectangle)
		cP2 = Point(self.win.getWidth() - self.bTankWidth/2, (3/5)*self.bTankHeight)
		cP1 = Point(cP2.getX() - self.bTankWidth, cP2.getY() - self.bTankHeight/5)
		bCannon = Rectangle(cP1, cP2)
		bCannon.setFill("black")
		bCannon.draw(win)
		self.bShapes.append(bCannon)
	def getBShapes(self):
		return self.bShapes
	def upperYCord(self):
		return self.bShapes[0].getP1().getY()
	def upperXCord(self):
		return self.bShapes[0].getP1().getX()
	def lowerYCord(self):
		return self.bShapes[0].getP2().getY()
	def lowerXCord(self):
		return self.bShapes[0].getP2().getX()
	def upperCannonXCord(self):
		return self.bShapes[1].getP1().getX()
	def upperCannonYCord(self):
		return self.bShapes[1].getP1().getY()
	def lowerCannonXCord(self):
		return self.bShapes[1].getP2().getX()
	def lowerCannonYCord(self):
		return self.bShapes[1].getP2().getY()
class Bullet:
	def __init__(self, speed, centerX, centerY, radius, window):
		self.speed = speed
		self.centerX = centerX
		self.centerY = centerY
		self.radius = radius
		self.window = window
		self.bullet = Circle(Point(self.centerX, self.centerY), self.radius)
		self.bullet.draw(self.window)
		self.bullet.setFill("Green")
	def moveBullet(self):
		self.bullet.move(self.speed, 0)
		self.centerX = self.bullet.getCenter().getX()
		self.centerY = self.bullet.getCenter().getY()
	def getCenterX(self):
		return self.centerX
	def getCenterY(self):
		return self.centerY
	def getRadius(self):
		return self.radius
	def undrawBullet(self):
		self.bullet.undraw()
	def bulletTop(self):
		return self.centerY - self.radius
	def bulletLeft(self):
		return self.centerX - self.radius
	def bulletBottom(self):
		return self.centerY + self.radius
	def bulletRight(self):
		return self.centerX + self.radius
def main():
	width = 1500
	height = 700
	win = GraphWin("Red vs. Blue Tank Battle", width, height)

	dimensions = [height/15, height/15]
	rTank = RedTank(win, dimensions)
	bTank = BlueTank(win, dimensions)
	moveDistance = height/20
	bulletSpeed = height/20
	redBullets = []
	blueBullets = []
	rPop = []
	bPop = []
	while True:
		for i in range(len(redBullets)):
			if redBullets[i].getCenterX() + redBullets[i].getRadius() + bulletSpeed < width:
				redBullets[i].moveBullet()
				time.sleep(.03/(len(redBullets)+len(blueBullets)))
				if redBullets[i].bulletRight() > bTank.upperXCord():
					if redBullets[i].bulletTop() > bTank.upperYCord():
						if redBullets[i].bulletTop() < bTank.lowerYCord():
							break
					elif redBullets[i].bulletBottom() < bTank.lowerYCord():
						if redBullets[i].bulletBottom() > bTank.upperYCord():
							break
			else:
				redBullets[i].undrawBullet()
				rPop.append(i)
		for i in rPop:
			redBullets.pop(i)
			rPop.pop(i)
		for i in range(len(blueBullets)):
			if blueBullets[i].getCenterX() - blueBullets[i].getRadius() - bulletSpeed > 0:
				blueBullets[i].moveBullet()
				time.sleep(.03/(len(blueBullets)+len(redBullets)))
			else:
				blueBullets[i].undrawBullet()
				bPop.append(i)
		for i in bPop:
			blueBullets.pop(i)
			bPop.pop(i)
		key = win.checkKey()
		if key == "Escape":
			win.close()
		if key == "w":
			if rTank.upperYCord() > moveDistance:
				for shape in rTank.getRShapes():
					shape.move(0, -moveDistance)
			else:
				distToTop = -rTank.upperYCord()
				for shape in rTank.getRShapes():
					shape.move(0, distToTop)
		elif key == "s":
			if height - rTank.lowerYCord() > moveDistance:
				for shape in rTank.getRShapes():
					shape.move(0, moveDistance)
			else:
				distToBottom = height - rTank.lowerYCord()
				for shape in rTank.getRShapes():
					shape.move(0, distToBottom)
		if key == "d":
			if len(redBullets) < 5:
				rBullet = Bullet(bulletSpeed, rTank.lowerCannonXCord(), (rTank.upperCannonYCord() + rTank.lowerCannonYCord())/2, rTank.lowerCannonYCord() - rTank.upperCannonYCord(), win)
				redBullets.append(rBullet)
		if key == "Up":
			if bTank.upperYCord() > moveDistance:
				for shape in bTank.getBShapes():
					shape.move(0, -moveDistance)
			else:
				distToTop = -bTank.upperYCord()
				for shape in bTank.getBShapes():
					shape.move(0, distToTop)
		elif key == "Down":
			if height - bTank.lowerYCord() > moveDistance:
				for shape in bTank.getBShapes():
					shape.move(0, moveDistance)
			else:
				distToBottom = height - bTank.lowerYCord()
				for shape in bTank.getBShapes():
					shape.move(0, distToBottom)
		if key == "Left":
			if len(blueBullets) < 5:
				bBullet = Bullet(-bulletSpeed, bTank.upperCannonXCord(), (bTank.upperCannonYCord() + bTank.lowerCannonYCord())/2, bTank.lowerCannonYCord() - bTank.upperCannonYCord(), win)
				blueBullets.append(bBullet)
	return
main()