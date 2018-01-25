# Linked List - display all nodes

class node:
    def __init__(self):
        # declare item : string
        # declare pointer : integer
        item = ""
        pointer = -1

# declare groceryorder : array[0..5] of node
groceryorder = [node(),node(),node(),node(),node(),node()]
# declare startPtr : integer
startPtr = 5

def displayItems():
    # declare index : integer
    index = startPtr
    while (index != -1):
        print(groceryorder[index].item)
        index = groceryorder[index].pointer

# set up linked list values
groceryorder[0].item = "cheese"
groceryorder[0].pointer = 1
groceryorder[1].item = "butter"
groceryorder[1].pointer = 4
groceryorder[2].item = "milk"
groceryorder[2].pointer = 5
groceryorder[3].item = "shoe polish"
groceryorder[3].pointer = 1
groceryorder[4].item = "cola"
groceryorder[4].pointer = -1
groceryorder[5].item = "bagels"
groceryorder[5].pointer = 0

# display all nodes in order
displayItems()

