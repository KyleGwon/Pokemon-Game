from graphics import *
import time
import random

class player:
	def __init__(self,pieces,win,name,color):
		#pieces contains a list of the remaining pieces
		self.pieces = pieces
		self.win = win
		self.name = name
		self.nameText = None
		self.color = color
	def displayName(self, pos):
		x1 = pos[0]
		x2 = pos[1]
		y1 = pos[2]
		y2 = pos[3]
		increment = (x2-x1)/22
		p1 = Point(x1 + (x2-x1)/2, y1 + increment)
		name = Text(p1,self.name)
		name.setTextColor(self.color)
		name.draw(self.win)
		self.nameText = name
	def undrawName(self):
		self.nameText.undraw()
	def displayPieces(self, pos):
		#x and y coordinates correspond to
		#the space that the display covers
		x1 = pos[0]
		x2 = pos[1]
		y1 = pos[2]
		y2 = pos[3]
		increment = (x2-x1)/22
		startCorner = Point(x1 + increment, y1 + 3*increment)
		corner = Point(startCorner.getX(),startCorner.getY())
		rowEndX = startCorner.getX()
		listOfRowHeights = [0]
		#rowEndX represents the x-coord if the piece is on that row
		counter = 0
		for i in range(len(self.pieces)):
			rowEndX += ((self.pieces[i].getWidth()+1)*increment)
			if rowEndX > x2-increment:
				rowEndX = startCorner.getX() + ((self.pieces[i].getWidth()+1)*increment)
				corner = Point(startCorner.getX(), corner.getY() + (max(listOfRowHeights)+1)*increment)
				self.pieces[i].drawPiece(increment,corner,self.color,self.win)
				listOfRowHeights = [0]
			else:
				if i == 0:
					corner = Point(corner.getX(), corner.getY())
				else:
					corner = Point(corner.getX() + (self.pieces[i-1].getWidth()+1) * increment, corner.getY())
				self.pieces[i].drawPiece(increment,corner,self.color,self.win)
				listOfRowHeights.append(self.pieces[i].getHeight())
	def getPieces(self):
		return self.pieces
	def undrawPieces(self):
		for i in self.pieces:
			i.undrawPiece()

class Quadrant:
	def __init__(self,x1,x2,y1,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.player = None
	def coordinates(self):
		return[self.x1,self.x2,self.y1,self.y2]
	def addPlayer(self,player):
		self.player = player
	def getPlayer(self):
		return self.player
			
class piece:
	def __init__(self,coordinates,width,height,pieceCount,win):
		self.coordinates = coordinates
		self.width = width
		self.height = height
		self.polygon = []
		self.win = win
		self.startpos = None
		self.increment = None
	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
	def rotateRight(self):
		newcord = self.coordinates[:]
		i = max[self.width,self.height]
		for j in range(i):
			for k in range(i):
				self.coordinates[j][k] = newcord[k][i-1-j]
		return self.coordinates
	def rotateLeft(self):
		newcord = self.coordinates[:]
		i = max[self.width,self.height]
		for j in range(i):
			for k in range(i):
				self.coordinates[j][k] = newcoord[j][i-1-k]
		return self.coordinates
	def drawPiece(self, increment, startpos, color, win):
		#startpos is the point of the upper left corner of where you want to start
		self.startpos = startpos
		self.increment = increment
		for x in range(len(self.coordinates)):
			for y in range(len(self.coordinates[x])):
				ul = Point(self.startpos.getX() + (x*increment), self.startpos.getY() + (y*increment))
				lr = Point(ul.getX() + increment, ul.getY() + increment)
				if self.coordinates[x][y] == 1:
					square = Rectangle(ul,lr)
					self.polygon.append(square)
		for i in self.polygon:
			i.setOutline("black")
			i.setFill(color)
			i.draw(self.win)
	def undrawPiece(self):
		for i in self.polygon:
			i.undraw()
		self.polygon = []
	def getDimensions():
		x1 = self.startpos.getX()
		x2 = x1 + self.width*self.increment
		y1 = self.startPos.getY()
		y2 = y1 + self.height*self.increment
		return [x1,x2,y1,y2]
		
class board:
	def __init__(self,board):
		self.board = board
	def rotateBoard():
		newBoard = [][]
		for i in range(20):
			for j in range(20):
				
	def hoverPiece():
	def addPiece():


class square:
	def __init__(self,coordinates,occupied,win):
		#coordinates is a list of four items
		#[x1,x2,y1,y2]
		#occupied is a bool
		self.x1 = coordinates[0]
		self.x2 = coordinates[1]
		self.y1 = coordinates[2]
		self.y2 = coordinates[3]
		self.occupied = occupied
		self.win = win
		self.owner = None
		self.s1 = None
		self.color = None
	def colorSquare(self,color):
		self.color = color
		p1 = Point(self.x1,self.y1)
		p2 = Point(self.x2,self.y2)
		s1 = Rectangle(p1,p2)
		self.s1.setFill(self.color)
		self.s1.setOutline("black")
		self.s1.draw(self.win)
		return 0
	def occupy(self):
		self.occupied = true
	def getOccupied(self):
		return occupied
	def setOwner(self, player):
		self.owner = player
	def getColor(self):
		return self.color
	def getOwner(self):
		return self.owner
	def getCoordinates(self):
		return [self.x1,self.x2,self.y1,self.y2]

def boardSetup(win,width,height):
	#boardUL = Point(width-height-(width-height)/2, 5)
	#boardLR = Point(width-((width-height)/2),height-5)
	#board = Rectangle(boardUL,boardLR)
	#board.draw(win)
	boardList = []
	widthInc = height/20
	heightInc = (height-10)/20
	x1 = -widthInc+width-height-(width-height)/2
	x2 = -widthInc+width-height-(width-height)/2 + (height)/20
	y1 = -heightInc+5
	y2 = -heightInc+5 + (height-10)/20
	for x in range(0,20):
		column = []
		boardList.append(column)
		x1 += widthInc
		x2 += widthInc
		y1 = ((height-10)/-20)+5
		y2 = ((height-10)/-20)+5 + (height-10)/20
		for y in range(0,20):
			y1 += heightInc
			y2 += heightInc
			l1 = [x1,x2,y1,y2]
			s1 = square(l1,False,win)
			column.append(s1)
			s1.colorSquare("white")
	return boardList

def rotateDisplay(quads):
	quad1player = quads[0].getPlayer()
	for i in range(4):
		quads[i].getPlayer().undrawPieces()
		quads[i].getPlayer().undrawName()
	quads[3].getPlayer().displayPieces(quads[0].coordinates())
	quads[3].getPlayer().displayName(quads[0].coordinates())
	quads[0].addPlayer(quads[3].getPlayer())
	quads[2].getPlayer().displayPieces(quads[3].coordinates())
	quads[2].getPlayer().displayName(quads[3].coordinates())
	quads[3].addPlayer(quads[2].getPlayer())
	quads[1].getPlayer().displayPieces(quads[2].coordinates())
	quads[1].getPlayer().displayName(quads[2].coordinates())
	quads[2].addPlayer(quads[1].getPlayer())
	quad1player.displayPieces(quads[1].coordinates())
	quad1player.displayName(quads[1].coordinates())
	quads[1].addPlayer(quad1player)

def piecesSetup(win):
	pieces = []
	#1 five piece
	coordinates = [[0 for x in range(5)] for y in range(5)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	coordinates[3][0] = 1
	coordinates[4][0] = 1
	i5 = piece(coordinates,5,1,5,win)
	pieces.append(i5)
	
	#4 4 pieces
	coordinates = [[0 for x in range(4)]for y in range(4)]
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	coordinates[2][0] = 1
	coordinates[3][0] = 1
	n = piece(coordinates,4,2,5,win)
	pieces.append(n)

	coordinates = [[0 for x in range(4)]for y in range(4)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	coordinates[3][0] = 1
	l5 = piece(coordinates,4,2,5,win)
	pieces.append(l5)

	coordinates = [[0 for x in range(4)]for y in range(4)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	coordinates[2][1] = 1
	coordinates[3][0] = 1
	y2 = piece(coordinates,4,2,5,win)
	pieces.append(y2)

	coordinates = [[0 for x in range(4)]for y in range(4)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	coordinates[3][0] = 1
	i4 = piece(coordinates,4,1,4,win)
	pieces.append(i4)

	#12 3x3 pieces
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[0][2] = 1
	coordinates[1][2] = 1
	coordinates[2][2] = 1
	v5 = piece(coordinates,3,3,5,win)
	pieces.append(v5)

	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][2] = 1
	coordinates[1][2] = 1
	coordinates[2][2] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	t5 = piece(coordinates,3,3,5,win)
	pieces.append(t5)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	coordinates[2][1] = 1
	u = piece(coordinates,3,2,5,win)
	pieces.append(u)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][1] = 1
	coordinates[2][1] = 1
	coordinates[2][2] = 1
	z5 = piece(coordinates,3,3,5,win)
	pieces.append(z5)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][1] = 1
	coordinates[1][2] = 1
	coordinates[2][2] = 1
	w = piece(coordinates,3,3,5,win)
	pieces.append(w)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[0][2] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	p = piece(coordinates,2,3,5,win)
	pieces.append(p)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	coordinates[1][2] = 1
	coordinates[2][1] = 1
	x = piece(coordinates,3,3,5,win)
	pieces.append(x)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][1] = 1
	coordinates[0][2] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	coordinates[2][1] = 1
	f = piece(coordinates,3,3,5,win)
	pieces.append(f)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][1] = 1
	coordinates[2][1] = 1
	l4 = piece(coordinates,3,2,4,win)
	pieces.append(l4)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	coordinates[2][1] = 1
	t4 = piece(coordinates,3,2,4,win)
	pieces.append(t4)
	
	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	coordinates[2][0] = 1
	i3 = piece(coordinates,3,1,3,win)
	pieces.append(i3)

	coordinates = [[0 for x in range(3)]for y in range(3)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][1] = 1
	coordinates[1][2] = 1
	z4 = piece(coordinates,2,3,4,win)
	pieces.append(z4)

	#3 2x2 pieces
	coordinates = [[0 for x in range(2)]for y in range(2)]
	coordinates[0][0] = 1
	coordinates[0][1] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	o = piece(coordinates,2,2,4,win)
	pieces.append(o)

	coordinates = [[0 for x in range(2)]for y in range(2)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	coordinates[1][1] = 1
	v3 = piece(coordinates,2,2,3,win)
	pieces.append(v3)

	coordinates = [[0 for x in range(2)]for y in range(2)]
	coordinates[0][0] = 1
	coordinates[1][0] = 1
	k2 = piece(coordinates,2,1,2,win)
	pieces.append(k2)
	#1 1x1 piece
	coordinates = [[0 for x in range(1)]for y in range(1)]
	coordinates[0][0] = 1
	k1 = piece(coordinates,1,1,1,win)
	pieces.append(k1)
	
	return pieces

def main():
	width = 1250
	height = 600
	win=GraphWin("Blokus",width, height)
	board = boardSetup(win,width,height)
	#pos consists of a list of [x1,x2,y1,y2]
	quad1 = Quadrant(0,width-height-(width-height)/2,0,height/2)
	quad2 = Quadrant(width-((width-height)/2),width,0,height/2)
	quad3 = Quadrant(width-((width-height)/2),width,height/2,height)
	quad4 = Quadrant(0,width-height-(width-height)/2,height/2,height)
	quads = [quad1,quad2,quad3,quad4]
	
	player1 = player(piecesSetup(win),win,"Kenny","blue")
	player1.displayPieces(quad1.coordinates())
	player1.displayName(quad1.coordinates())
	quad1.addPlayer(player1)
	player2 = player(piecesSetup(win),win,"Carter","red")
	player2.displayPieces(quad2.coordinates())
	player2.displayName(quad2.coordinates())
	quad2.addPlayer(player2)
	player3 = player(piecesSetup(win),win,"Kyle","green")
	player3.displayPieces(quad3.coordinates())
	player3.displayName(quad3.coordinates())
	quad3.addPlayer(player3)
	player4 = player(piecesSetup(win),win,"Greg","brown")
	player4.displayPieces(quad4.coordinates())
	player4.displayName(quad4.coordinates())
	quad4.addPlayer(player4)

	while True:
		key = win.getKey()
		if key == "r":
			rotateDisplay(quads)
		if key == "q":
			win.close()



	click = win.getMouse()
	xclick = click.getX()
	yclick = click.getY()
	if pos1[0] < x < pos1[1]:
		if pos1[2] < y < pos1[3]:
			return


	win.getMouse()
	win.close()
	return 0

main()