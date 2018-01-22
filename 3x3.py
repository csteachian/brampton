# 3x3
# Ian Simpson
# 22nd January 2018
import random

# DECLARE index : INTEGER
grid = [[0 for col in range(0,3)]for row in range(0,3)]

for num in range(1,10):
    added = False
    while added != True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if grid[row][col] == 0:
            grid[row][col]  = num
            added = True

for index in range(0,3):
    print(grid[index])




