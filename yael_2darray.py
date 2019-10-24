grid = [["*" for col in range(0,3)] for row in range(0,3)]
def showGrid():
	for row in range(0,3):
		output = ""
		for col in range(0,3):
			output = output + " " + grid[row][col]
		print(output)
	print()

def playMove(row,col,player):
	if grid[row][col] == "*":
		grid[row][col] = player
		global counter
		counter = counter + 1
	else:
		print("Not a valid move")
		print()
	showGrid()

counter = 1
print("")
showGrid()
while True:
	xuinput = int(input("Left->right where do you place it(1-3): "))
	yuinput = int(input("Up->down where do you place it?(1-3): "))
	xuinput = xuinput - 1
	yuinput = yuinput - 1
	if xuinput > -1 and xuinput < 3 and yuinput > -1 and yuinput < 3:
		if counter % 2 == 1:
			print("")
			playMove(yuinput,xuinput,"O")
		elif counter % 2 == 0:
			print("")
			playMove(yuinput,xuinput,"X")
		else:
			print("What?")
	else:
		print()
		print("Out of range.")
		print()
