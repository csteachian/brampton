# DECLARE entry, middle, top, bottom : INTEGER
# DECLARE testscore : ARRAY[0:6] OF INTEGER
testscore = [5,12,24,43,48,58,76]
entry = int(input("Enter ")) # IS changed input.. to int(input..)
n = len(testscore) -1 # IS added -1 to ensure index out of range error did not occur
top = n
bottom = 0
index = -1 # IS added

while (index == -1) and (bottom <= top): # IS added
    middle = (bottom + top) // 2 # IS changed divide / to floor //
    #print(bottom,top,middle,index,entry) # uncomment this line to see program trace
    if entry == testscore[middle]:
        index = middle # IS added
    elif entry < testscore[middle]:
        top = middle - 1
    else: # IS added
        bottom = middle + 1
    
if index != -1: # IS added
    print("Value at", index) # IS changed middle to index
else: # IS added
    print("Not in list")
