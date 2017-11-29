startPos = 0
endPos = -1
thequeue = []

def enqueue(thequeue, item): # puts an item into the queue
    global endPos
    endPos = endPos + 1
    thequeue.append(item)
    # thequeue[endPos] = item

def dequeue(thequeue): # takes the first item of the queue
    # DECLARE output : CHAR
    global startPos, endPos
    if startPos == endPos + 1:
        output = 'END OF QUEUE'
    else:
        output = thequeue[startPos]
        startPos = startPos + 1
    return output

def processqueue(character, thequeue): # display the first item in the queue in lower case
    enqueue(thequeue, character) #NOT SURE WHAT TO DO HERE - i had dequeue but didnt make sense
    print(character.lower)

def queueempty(): #tests to see if the queue is empty
    global startPos, endPos, Flag
    if startPos == endPos + 1 :
        Flag = True
    else:
        Flag = False
    return Flag