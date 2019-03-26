# Ordered linked list
# By Ian Simpson @familysimpson

# Set up linked list node structure
class Node():
    def __init__(self):
        self.Data = 0
        self.Pointer = -1

# Set up linked list of nodes
List = [Node(),Node(),Node(),Node(),Node()]
# Set up initial data and pointer values
List[0].Data = 3
List[0].Pointer = 1
List[1].Data = 7
List[1].Pointer = 2
List[2].Data = 11
List[2].Pointer = -1
FreeListPtr = 3
StartPointer = 0
NullPointer = -1

# This procedure displays the contents of the linked list (not in 'correct' order)
def printList():
    for index in range(0,4):
        print("Data:",List[index].Data,"Ptr:",List[index].Pointer)


# Implementation of pseudocode from CIE book
def InsertNode(NewItem):
    global FreeListPtr, StartPointer, NullPointer # imports variables from main
    if FreeListPtr != NullPointer: # If there are any free nodes in linked list
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        # find insertion point
        ThisNodePtr = StartPointer
        while (ThisNodePtr != NullPointer) and (List[ThisNodePtr].Data < NewItem):
            PreviousNodePtr = ThisNodePtr
            ThisNodePtr = List[ThisNodePtr].Pointer
        if PreviousNodePtr == StartPointer: # This is special case, adding to start of list
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else: # Otherwise just change pointers to link to new list item
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr

# Main program
printList() # Display initialised linked list
InsertNode(9) # Add new item to ordered linked list
print() # A space
printList() # Display new linked list
            
