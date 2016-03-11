from __future__ import print_function

currentPlayer = 1

Matrix = [[-1 for x in range(3)] for x in range(3)] 

pieces = {}

pieces[1] = {}
pieces[2] = {}

pieces[1]['S'] = 2
pieces[1]['M'] = 2
pieces[1]['L'] = 2

pieces[2]['S'] = 2
pieces[2]['M'] = 2
pieces[2]['L'] = 2

def pieceType(x, y):
	value = Matrix[x][y] % 3
	if value == 0:
		return "S"
	elif value == 1:
		return "M"
	else:
		return "L"

def playerNumber(x, y):
	value = Matrix[x][y]
	if value == -1:
		return 0
	elif value <= 2:
		return 1
	else:
		return 2
		
def canDoMove(x, y, p, player = currentPlayer):
	if playerNumber(x, y) != 0:
		val = Matrix[x][y] % 3
		p_val = p % 3
		return p_val > val
	return True
	
def pieceVal(p_str):
	if p_str == "S":
		p_val = (currentPlayer - 1) * 3
	elif p_str == "M":
		p_val = (currentPlayer - 1) * 3 + 1
	elif p_str == "L":
		p_val = (currentPlayer - 1) * 3 + 2
	else:
		p_val = -1
	return p_val
	
def isAnyMovePossible():
	for i in range(3):
		for j in range(3):
			for p in pieces[1]:
				if pieces[1][p] > 0 and canDoMove(i, j, pieceVal(p), 1):
					return True
			for p in pieces[2]:
				if pieces[2][p] > 0 and canDoMove(i, j, pieceVal(p), 2):
					return True
	return False
	
def hasWinner():
	for i in range(3):
		if playerNumber(i, 0) != 0 and playerNumber(i, 0) == playerNumber(i, 1) and playerNumber(i, 1) == playerNumber(i, 2):
			return playerNumber(i, 0)
		if playerNumber(0, i) != 0 and playerNumber(0, i) == playerNumber(1, i) and playerNumber(1, i) == playerNumber(2, i):
			return playerNumber(0, i)
	if playerNumber(0, 0) != 0 and playerNumber(0, 0) == playerNumber(1, 1) and playerNumber(1, 1) == playerNumber(2, 2):
		return playerNumber(0, 0)
	if playerNumber(0, 2) != 0 and playerNumber(0, 2) == playerNumber(1, 1) and playerNumber(1, 1) == playerNumber(2, 0):
		return playerNumber(0, 2)
	return -1
	
def printBoard():
	print("=" * 12)
	for i in range(3):
		for j in range(3):
			val = Matrix[i][j]
			player = playerNumber(i, j)
			if player == 0:
				print ("|--|", end='', sep='')
				continue
			print ("|", player, pieceType(i, j), "|", end='', sep='')
		print('\n', "=" * 12, sep='')
		
while hasWinner() == -1:
	if isAnyMovePossible() == False:
		break
		
	print("-" * 50)
	print("Now playing: player #", currentPlayer, sep='')
	
	x = 0
	y = 0
	p = ""
	
	while x > 3 or x < 1:
		x = int(input("Enter x [1 - 3]: "))
		
	while y > 3 or y < 1:
		y = int(input("Enter y [1 - 3]: "))
	
	while p != "S" and p != "M" and p != "L":
		p = input("Enter input (\"S\", \"M\", \"L\"): ")
		if p in pieces[currentPlayer] and pieces[currentPlayer][p] == 0:
			print("This piece is not available! Try another.")
			p = ""
			continue
		
	x = x - 1
	y = y - 1
	
	p_val = pieceVal(p)
	if p_val == -1:
		continue
		
	if canDoMove(x, y, p_val) == True:
		pieces[currentPlayer][p] = pieces[currentPlayer][p] - 1
		Matrix[x][y] = p_val
		printBoard()
	else:
		print("This move is not allowed!")
		continue
		
	currentPlayer = ((currentPlayer + 1) % 3)
	if currentPlayer == 0:
		currentPlayer = 1
		
		
if hasWinner() != -1:
	print("We have a winner!")
	print("Player #", hasWinner(), " has won!", sep='')
else:
	print("No more moves are possible!")