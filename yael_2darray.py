# 2D arrays example for Yael
# Ian Simpson
# 23rd January 2018

# DECLARE grid : ARRAY(0..2,0..2) OF STRING
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
    else:
        print("Not a valid move")
    showGrid()

showGrid()
playMove(1,1,"O")
playMove(0,2,"X")
playMove(1,2,"O")
playMove(1,0,"X")
playMove(0,0,"O")
playMove(2,2,"X")
playMove(2,1,"O")
playMove(1,2,"X")
playMove(0,1,"X")
playMove(2,0,"O")
