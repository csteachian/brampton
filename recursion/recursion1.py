# Recursion example
# Summing a list of numbers
# Ian Simpson @familysimpson

# Inspired by https://www.cs.utah.edu/~germain/PPS/Topics/recursion.html

def rest(thislist):
    # returns list minus the first element
    newlist = []
    for index in range(1,len(thislist)): #skip item 0
        newlist.append(thislist[index])
    return newlist  

def listsum(thislist, thislistlength):
    print("LISTSUM:",thislist)
    if (thislistlength == 0):
        print("RETURN 0")
        return 0
    print("CALL ",thislist[0],"+LISTSUM(",rest(thislist),",",thislistlength-1,")")
    newvalue = thislist[0] + listsum(rest(thislist),thislistlength -1)
    print("RETURN",newvalue)
    return newvalue

#main program
print("Recursion example")
thislist = [1,2,3,4,5,6,7,8,9]
print("Creating sum of",thislist)
print(listsum(thislist,len(thislist)))
