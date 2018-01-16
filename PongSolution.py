#This file will have the solution

from graphics import *
import random
import time


class Paddle:
	def __init__(self, p1, p2, win, color):
		self.p1 = p1
		self.p2 = p2
		self.win = win
		self.paddle = Rectangle(self.p1, self.p2)
		self.paddle.setFill(color)
		self.paddle.draw(self.win)
	def getP1(self):
		return self.paddle.getP1()
	def getP2(self):
		return self.paddle.getP2()
	def moveUp(self, moveAmount):
		self.paddle.move(0,-moveAmount)
	def moveDown(self, moveAmount):
		self.paddle.move(0,moveAmount)
class Ball:
	def __init__(self, center, radius, win, color):
		self.center = center
		self.radius = radius
		self.win = win
		self.color = color
		self.ball = Circle(center, radius)
		self.ball.setFill(color)
		self.ball.draw(self.win)
	def moveBall(self, speedx, speedy):
		self.ball.move(speedx,speedy)
	def getCenter(self):
		return self.ball.getCenter()
	def getTop(self):
		return self.ball.getCenter().getY() - self.ball.radius
	def getBottom(self):
		return self.ball.getCenter().getY() + self.ball.radius
	def getLeft(self):
		return self.ball.getCenter().getX() - self.ball.radius
	def getRight(self):
		return self.ball.getCenter().getX() + self.ball.radius

def resetSpeed(originalSpeed):
	ballspeedx = random.randrange(originalSpeed//2, 2*originalSpeed//3) * random.choice([-1,1])
	ballspeedy = (originalSpeed - abs(ballspeedx)) * random.choice([-1,1])
	return [ballspeedx, ballspeedy]

def main():
	width = 1200
	height = 600
	win = GraphWin("Pong Solution", width, height)
	paddleHeight = height/5
	paddleWidth = width/40

	rPadPt1 = Point(paddleWidth, (height/2) - (paddleHeight/2))
	rPadPt2 = Point(2*paddleWidth, (height/2) + (paddleHeight/2))
	redPaddle = Paddle(rPadPt1, rPadPt2, win, "red")

	bPadPt1 = Point(width - (2*paddleWidth), (height/2) - (paddleHeight/2))
	bPadPt2 = Point(width - paddleWidth, (height/2) + (paddleHeight/2))
	bluePaddle = Paddle(bPadPt1, bPadPt2, win, "blue")

	moveAmount = height/20

	ballCenter = Point(width/2, height/2)
	ballRadius = height/20
	ball = Ball(ballCenter, ballRadius, win, "purple")
	originalSpeed = 25
	ballspeed = originalSpeed
	ballspeedx = random.randrange(ballspeed//2, 2*ballspeed//3) * random.choice([-1,1])
	ballspeedy = (ballspeed - abs(ballspeedx)) * random.choice([-1,1])

	redScore = 0
	blueScore = 0
	redText = Text(Point(2*width/5, height/8), str(blueScore))
	redText.setSize(36)
	redText.setStyle("bold")
	redText.setTextColor("red")
	redText.draw(win)
	blueText = Text(Point(3*width/5, height/8), str(blueScore))
	blueText.setSize(36)
	blueText.setStyle("bold")
	blueText.setTextColor("blue")
	blueText.draw(win)

	numOfHits = 0
	gameEnd = False
	while not gameEnd:
		if ball.getLeft() < redPaddle.getP2().getX():
			blueScore += 1
			blueText.setText(blueScore)
			key = ""
			while key != "space":
				if key == "Escape":
					win.close()
					return
				key = win.getKey()
			speed = resetSpeed(originalSpeed)
			ballspeedx = abs(speed[0])
			ballspeedy = speed[1]
			numOfHits = 0
			while ball.getLeft() < redPaddle.getP2().getX():
				ball.moveBall(ballspeedx, ballspeedy)
				time.sleep(.05)
		if ball.getRight() > bluePaddle.getP1().getX():
			redScore += 1
			redText.setText(redScore)
			key = ""
			while key != "space":
				if key == "Escape":
					win.close()
					return
				key = win.getKey()
			speed = resetSpeed(originalSpeed)
			ballspeedx = -abs(speed[0])
			ballspeedy = speed[1]
			numOfHits = 0
			while ball.getRight() > bluePaddle.getP1().getX():
				ball.moveBall(ballspeedx, ballspeedy)
				time.sleep(.05)
		if ball.getLeft() + ballspeedx <= redPaddle.getP2().getX():
			if ball.getCenter().getY() > redPaddle.getP1().getY():
				if ball.getCenter().getY() < redPaddle.getP2().getY():
					numOfHits += 1
					if numOfHits%3 == 0:
						ballspeedx = 1.5 * ballspeedx
						ballspeedy = 1.5 * ballspeedy
					if ball.getTop() + ballspeedy < 0:
						ball.moveBall(redPaddle.getP2().getX()-ball.getLeft() + -(ballspeedx-(redPaddle.getP2().getX()-ball.getLeft())), - ball.getTop() + -ballspeedy-ball.getTop())
						ballspeedy = -ballspeedy
						ballspeedx = -ballspeedx
					if ball.getBottom() + ballspeedy > height:
						ball.moveBall(redPaddle.getP2().getX()-ball.getLeft() + -(ballspeedx-(redPaddle.getP2().getX()-ball.getLeft())), (height - ball.getBottom()) - (ballspeedy+ball.getBottom()-height))
						ballspeedy = -ballspeedy
						ballspeedx = -ballspeedx
					else:
						ball.moveBall(redPaddle.getP2().getX()-ball.getLeft() + -(ballspeedx-(redPaddle.getP2().getX()-ball.getLeft())), ballspeedy)
						ballspeedx = -ballspeedx
				else:
					ball.moveBall(ballspeedx, ballspeedy)
			else:
				ball.moveBall(ballspeedx, ballspeedy)

		elif ball.getRight() + ballspeedx >= bluePaddle.getP1().getX():
			if ball.getCenter().getY() > bluePaddle.getP1().getY():
				if ball.getCenter().getY() < bluePaddle.getP2().getY():
					numOfHits += 1
					if numOfHits%3 == 0:
						ballspeedx = 1.5 * ballspeedx
						ballspeedy = 1.5 * ballspeedy
					if ball.getTop() + ballspeedy < 0:
						ball.moveBall(bluePaddle.getP1().getX()-ball.getRight() - (ballspeed-(bluePaddle.getP1().getX()-ball.getRight())), - ball.getTop() + -ballspeedy-ball.getTop())
						ballspeedy = -ballspeedy
						ballspeedx = -ballspeedx
					if ball.getBottom() + ballspeedy > height:
						ball.moveBall(bluePaddle.getP1().getX()-ball.getRight() - (ballspeed-(bluePaddle.getP1().getX()-ball.getRight())), (height - ball.getBottom()) - (ballspeedy+ball.getBottom()-height))
						ballspeedy = -ballspeedy
						ballspeedx = -ballspeedx
					else:
						ball.moveBall(bluePaddle.getP1().getX()-ball.getRight() - (ballspeed-(bluePaddle.getP1().getX()-ball.getRight())), ballspeedy)
						ballspeedx = -ballspeedx
				else:
					ball.moveBall(ballspeedx, ballspeedy)
			else:
				ball.moveBall(ballspeedx, ballspeedy)


		elif ball.getTop() + ballspeedy < 0:
			ball.moveBall(ballspeedx, - ball.getTop() + -ballspeedy-ball.getTop())
			ballspeedy = -ballspeedy
		elif ball.getBottom() + ballspeedy > height:
			ball.moveBall(ballspeedx, (height - ball.getBottom()) - (ballspeedy+ball.getBottom()-height))
			ballspeedy = -ballspeedy
		else:
			ball.moveBall(ballspeedx, ballspeedy)
		time.sleep(.05)
		key = win.checkKey()
		if key == "w":
			distToTop = redPaddle.getP1().getY()
			if distToTop < moveAmount:
				redPaddle.moveUp(distToTop)
			else:
				redPaddle.moveUp(moveAmount)
		elif key == "s":
			distToBottom = height - redPaddle.getP2().getY()
			if distToBottom < moveAmount:
				redPaddle.moveDown(distToBottom)
			else:
				redPaddle.moveDown(moveAmount)
		elif key == "Up":
			distToTop = bluePaddle.getP1().getY()
			if distToTop < moveAmount:
				bluePaddle.moveUp(distToTop)
			else:
				bluePaddle.moveUp(moveAmount)
		elif key == "Down":
			distToBottom = height - bluePaddle.getP2().getY()
			if distToBottom < moveAmount:
				bluePaddle.moveDown(distToBottom)
			else:
				bluePaddle.moveDown(moveAmount)
		elif key == "Escape":
			win.close()
			break
	return 0
main()