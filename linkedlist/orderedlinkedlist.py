# Ordered linked list
class Node():
    def __init__(self):
        self.Data = 0
        self.Pointer = -1

# Set up linked list of nodes
List = [Node() for i in range(0,9)]
# Set up initial data and pointer values
List[0].Data = 3
List[0].Pointer = 1
List[1].Data = 7
List[1].Pointer = 2
List[2].Data = 11
List[2].Pointer = -1
FreeListPtr = 3

# new addition to ensure that free list pointer works
totalListSize = len(List)
for index in range (FreeListPtr,totalListSize-1):
    List[index].Pointer = index+1
List[totalListSize-1].Pointer = -1

StartPointer = 0
NullPointer = -1
PreviousNodePtr = StartPointer # new addition to ensure that insertion at start of list works

# This procedure displays the contents of the linked list
# This has been adapted to display linked list in correct order
def printList():
    print("Start pointer:",StartPointer)
    index = StartPointer
    while index != NullPointer:
        print("Item:",index,"Data:",List[index].Data,"Ptr:",List[index].Pointer)
        index = List[index].Pointer
    print("FreeListPtr:",FreeListPtr)


# Implementation of pseudocode from CIE book
def InsertNode(NewItem):
    global FreeListPtr, StartPointer, NullPointer # imports variables from main
    global PreviousNodePtr # new addition to ensure that insertion at start of list works
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
            # ->> CHANGE FROM CIE CODE
            if (List[PreviousNodePtr].Data < NewItem):
                # Insert second in list
                List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
                List[PreviousNodePtr].Pointer = NewNodePtr
            else:
                # Insert at start of list
                List[NewNodePtr].Pointer = StartPointer
                StartPointer = NewNodePtr
            # <<- END OF CHANGE FROM CIE CODE
        else: # Otherwise just change pointers to link to new list item
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr

# Main program
printList() # Display initialised linked list
goAgain = input("Do you want to add an item? (Y/N)")
while (goAgain.upper() =="Y") and (FreeListPtr != NullPointer):
    # ask for an item to be added
    newItem = int(input("Enter number to be added to linked list"))
    while newItem < 0 or newItem > 100:
        print("Error. Try a number 0..100")
    InsertNode(newItem) # Add new item to ordered linked list
    print() # A space
    printList() # Display new linked list
    PreviousNodePtr = StartPointer
    if FreeListPtr == NullPointer:
        print("Linked list is full")
    else:
        goAgain = input("Do you want to add an item? (Y/N)")
            
