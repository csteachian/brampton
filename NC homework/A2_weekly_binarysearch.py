# DECLARE entry, middle, top, bottom : INTEGER
# DECLARE testscore : ARRAY[0:6] OF INTEGER
testscore = [5,12,24,43,48,58,76]
entry = int(input("Enter ")) # changed input.. to int(input..)
n = len(testscore)
middle = round(n/2)
top = n
bottom = 0
if entry == testscore[middle]:
    print("Value at", middle)
elif entry > testscore[middle]:
    bottom = middle + 1
    middle = (bottom + top) / 2
    if entry == testscore[bottom]: # changed elif to IF
        print(bottom)
    elif entry == testscore[top]:
        print(top)
    else:
        print("not in list")
elif entry < testscore[middle]:
    top = middle - 1
    middle = (top + bottom) / 2
    if entry == testscore[top]:
        print(top)
    elif entry == testscore[bottom]:
        print(bottom)
    else:
        print("Not in list")
