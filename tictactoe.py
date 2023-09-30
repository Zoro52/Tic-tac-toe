import random

# initialize board
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]
currentPlayer = "X"
winner = None
gameRunning = True

#create function to display board
def displayBoard(board):
	print(board[0] + " | " + board[1] + " | " + board[2])
	print("----------")
	print(board[3] + " | " + board[4] + " | " + board[5])
	print("----------")
	print(board[6] + " | " + board[7] + " | " + board[8])
displayBoard(board)

#take player input
def playerInput(board):
	inp = int(input("Enter a number 1 - 9 : "))
	if inp >= 1 and inp <= 9 and board[inp-1] == "_":
		board[inp-1] = currentPlayer
	else:
		print("Oops! player already in that spot")

#check for win or tie
def checkHorizontal(board):
	global winner
	if board[0] == board[1] == board[2] and board[0] != "_":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[3] != "_":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[6] != "_":
		winner = board[6]
		return True

def checkVertical(board):
	global winner
	if board[0] == board[3] == board[6] and board[0] != "_":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] != "_":
		winner = board[1]
		return True
	elif board[2] == board[5] == board[8] and board[2] != "_":
		winner = board[2]
		return True

def checkDiagonal(board):
	global winner
	if board[0] == board[4] == board[8] and board[0] != "_":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] != "_":
		winner = board[1]
		return True

def checkTie(board):
	global gameRunning
	if "_" not in board:
		displayBoard(board)
		print("It is a tie!")
		gameRunning = False

def checkWin():
	if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
		print(f"The winner is {winner}")


# switch the player
def switchPlayer():
	global currentPlayer
	if currentPlayer == "X":
		currentPlayer = "O"
	else:
		currentPlayer = "X"

# computer
def computer(board):
	while currentPlayer == "O":
		position = random.randint(0, 8)
		if board[position] == "_":
			board[position] = "O"
			switchPlayer()


# check for win or tie

while gameRunning:
	displayBoard(board)
	playerInput(board)
	checkWin()
	checkTie(board)
	switchPlayer()
	computer(board)
	checkWin()
	checkTie(board)



























