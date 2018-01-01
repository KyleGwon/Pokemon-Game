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
	def upperXCord(self):
		return self.rShapes[0].getP1().getX()
	def lowerYCord(self):
		return self.rShapes[0].getP2().getY()
	def lowerXCord(self):
		return self.rShapes[0].getP2().getX()
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
# class HealthBar:
# 	def __init__(self, size, location, points, win)
# 	self.size = size
# 	self.loc = location
# 	self.pointX = points[0]
# 	self.pointY = points[1]
# 	self.win = win
# 	HealthBar = Rectangle(self.pointX, self.pointX)
# 	HealthBar.draw(self.win)
def main():
	width = 1000
	height = 500
	win = GraphWin("Red vs. Blue Tank Battle", width, height)
	rX = Point(width/2-50, 0)
	rY1 = Point(width/2-50+100*(1), 25)
	rY2 = Point(width/2-50+100*(2/3), 25)
	rY3 = Point(width/2-50+100*(1/3), 25)
	bX = Point(width/2-50, height-25)
	bY1 = Point(width/2-50+100*(1), height)
	bY2 = Point(width/2-50+100*(2/3), height)
	bY3 = Point(width/2-50+100*(1/3), height)
	rHealthBar1 = Rectangle(rX, rY1)
	rHealthBar2 = Rectangle(rX, rY2)
	rHealthBar3 = Rectangle(rX, rY3)
	bHealthBar1 = Rectangle(bX, bY1)
	bHealthBar2 = Rectangle(bX, bY2)
	bHealthBar3 = Rectangle(bX, bY3)
	rHealthBar1.setFill("red")
	rHealthBar2.setFill("red")
	rHealthBar3.setFill("red")
	bHealthBar1.setFill("blue")
	bHealthBar2.setFill("blue")
	bHealthBar3.setFill("blue")

	dimensions = [height/15, height/15]
	rTank = RedTank(win, dimensions)
	bTank = BlueTank(win, dimensions)
	rHealthBar1.draw(win)
	bHealthBar1.draw(win)
	rText = "Red has won!"
	bText = "Blue has won!"
	pX = (width/2)
	pY = (height/2)
	p = Point(pX, pY)
	moveDistance = height/20
	bulletSpeed = height/ 20
	redBullets = []
	blueBullets = []
	rPop = []
	bPop = []
	rHealth = 3
	bHealth = 3
	rScore = 0
	bScore = 0
	rScoreText = "Red's score is: "
	bScoreText = "Blue's score: "
	while rHealth > 0 and bHealth > 0:
		for i in range(len(redBullets)):
			if redBullets[i].getCenterX() + redBullets[i].getRadius() + bulletSpeed < width:
				redBullets[i].moveBullet()
				time.sleep(.02/(len(redBullets)+len(blueBullets)))
				if redBullets[i].bulletRight() > bTank.upperXCord():
					if redBullets[i].bulletTop() > bTank.upperYCord():
						if redBullets[i].bulletTop() < bTank.lowerYCord():
							if redBullets[i].bulletRight() < bTank.lowerXCord():
								redBullets[i].undrawBullet()
								rPop.append(i)
								if bHealth == 1:
									bHealthBar3.undraw()
									bHealthBar1.draw(win)
									bHealth = 3
									distToLeft = -rTank.upperXCord()
									rScore += 1
									for i in range(len(redBullets)):
										redBullets[i].undrawBullet()
									redBullets.pop()
									rPop.pop()
									break
									if rScore >= 5:
										bHealth = 0 
									for shape in rTank.getRShapes():
										shape.move(distToLeft, 0)
									distToBottom = height - rTank.lowerYCord()
									for shape in rTank.getRShapes():
										shape.move(0, distToBottom)


								elif bHealth == 2:
									bHealthBar2.undraw()
									bHealthBar3.draw(win)
									bHealth -= 1
								elif bHealth == 3:
									bHealthBar1.undraw()
									bHealthBar2.draw(win)
									bHealth -= 1
					elif redBullets[i].bulletBottom() < bTank.lowerYCord():
						if redBullets[i].bulletBottom() > bTank.upperYCord():
							if redBullets[i].bulletRight() < bTank.lowerXCord():
								if bHealth == 1:
									bHealthBar3.undraw()
									rWinner = Text(p, rText)
									rWinner.draw(win)
									bHealth -= 1
								elif bHealth == 2:
									bHealthBar2.undraw()
									bHealthBar3.draw(win)
									bHealth -= 1
								elif bHealth == 3:
									bHealthBar1.undraw()
									bHealthBar2.draw(win)
									bHealth -= 1
			else:
				redBullets[i].undrawBullet()
		for i in range(len(blueBullets)):
			if blueBullets[i].getCenterX() - blueBullets[i].getRadius() - bulletSpeed > 0:
				blueBullets[i].moveBullet()
				time.sleep(.02/(len(blueBullets)+len(redBullets)))
				if blueBullets[i].bulletLeft() < rTank.lowerXCord():
					if blueBullets[i].bulletTop() > rTank.upperYCord():
						if blueBullets[i].bulletTop() < rTank.lowerYCord():
							if blueBullets[i].bulletLeft() > rTank.upperXCord():
								if rHealth == 1:
									rHealthBar3.undraw()
									bWinner = Text(p, bText)
									bWinner.draw(win)
									rHealth -= 1
								elif rHealth == 2:
									rHealthBar2.undraw()
									rHealthBar3.draw(win)
									rHealth -= 1
								elif rHealth == 3:
									rHealthBar1.undraw()
									rHealthBar2.draw(win)
									rHealth -= 1
					elif blueBullets[i].bulletBottom() < rTank.lowerYCord():
						if blueBullets[i].bulletTop() > rTank.upperYCord():
							if blueBullets[i].bulletLeft() > redTank.upperXCord():
								if rHealth == 1:
									rHealthBar3.undraw()
									bWinner = Text(p, bText)
									bWinner.draw(win)
									rHealth -= 1
								elif rHealth == 2:
									rHealthBar2.undraw()
									rHealthBar3.draw(win)
									rHealth -= 1
								elif rHealth == 3:
									rHealthBar1.undraw()
									rHealthBar2.draw(win)
									rHealth -= 1
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
		elif key == "a":
			if rTank.upperXCord() - moveDistance > 0:
				for shape in rTank.getRShapes():
					shape.move(-moveDistance,0)
			else:
				distToLeft = -rTank.upperXCord()
				for shape in rTank.getRShapes():
					shape.move(distToLeft, 0)
		elif key == "d":
			if rTank.lowerXCord() + moveDistance < width:
				for shape in rTank.getRShapes():
					shape.move(moveDistance, 0)
			else:
				distToRight = width - rTank.lowerXCord()
				for shape in rTank.getRShapes():
					shape.move(distToRight, 0)
		if key == "q":
			if len(redBullets) < 11:
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
		elif key == "Left":
			if bTank.upperXCord() - moveDistance > 0:
				for shape in bTank.getBShapes():
					shape.move(-moveDistance,0)
			else:
				distToLeft = -bTank.upperXCord()
				for shape in bTank.getBShapes():
					shape.move(distToLeft, 0)
		elif key == "Right":
			if bTank.lowerXCord() + moveDistance < width:
				for shape in bTank.getBShapes():
					shape.move(moveDistance, 0)
			else:
				distToRight = width - bTank.lowerXCord()
				for shape in bTank.getBShapes():
					shape.move(distToRight, 0)
		if key == "slash":
			if len(blueBullets) < 11:
				bBullet = Bullet(-bulletSpeed, bTank.upperCannonXCord(), (bTank.upperCannonYCord() + bTank.lowerCannonYCord())/2, bTank.lowerCannonYCord() - bTank.upperCannonYCord(), win)
				blueBullets.append(bBullet)
	win.getMouse()
	win.close()
	return
main()

# make it so that once you get hit, the bullet stops
# create a sword function to wack ppl (make it do some like 360 spinning thing idk)