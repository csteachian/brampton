# Pizza manager
# Ian Simpson
# 12th January 2018

nullPtr = -1

class order:
    def __init__(self):
        self.no = 0
        self.base = ""
        self.topping = []


# LINKED LIST NODE SETUP
class node:
    def __init__(self):
        self.dataitem = order()
        self.pointer = nullPtr


def addNode():
    global startPtr
    if startPtr == -1:
        startPtr = 0
    if Choice.upper() == "T":
        pizzaorders[noOrders].dataitem.base = "Thin"
    elif Choice.upper() == "P":
        pizzaorders[noOrders].dataitem.base = "Pan"
    pizzaorders[noOrders].dataitem.no = noOrders + 1
    pizzaorders[noOrders].dataitem.topping = [-1,-1,-1,-1,-1]

def displayOrder(id):
    print(pizzaorders[id].dataitem.no)
    print(pizzaorders[id].dataitem.base)
    for Index in range(0, 4):
        if pizzaorders[id].dataitem.topping[Index] != -1:
            print(toppings[0][pizzaorders[id].dataitem.topping[Index]])

    #print(pizzaorders[id].pointer) # <-- good to see pointer for debug

Choice = ""
Again = ""
TopCount = 0
Index = 0
ShopOpen = True
EndOrder = False
noOrders = 0

toppings = [['' for x in range(0,10)] for y in range(0,2)]

pizzaorders = [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()]

startPtr = nullPtr

toppings[0][0] = "Cheese"
toppings[0][1] = "Ham"
toppings[0][2] = "Pepperoni"
toppings[0][3] = "Pineapple"
toppings[0][4] = "Mushroom"
toppings[0][5] = "Cherry Tomatoes"
toppings[0][6] = "Chicken"
toppings[0][7] = "Peppers"
toppings[0][8] = "Olives"
toppings[0][9] = "Jalapenos"
toppings[1][0] = "10"
toppings[1][1] = "10"
toppings[1][2] = "10"
toppings[1][3] = "10"
toppings[1][4] = "10"
toppings[1][5] = "10"
toppings[1][6] = "10"
toppings[1][7] = "10"
toppings[1][8] = "10"
toppings[1][9] = "10"

while (noOrders <= 9) and (ShopOpen == True):
    EndOrder = False
    TopCount = 0

    for Index in range(0,9):
        print(str(Index) + " " + toppings[0][Index] + " " + toppings[1][Index])


    Choice = input("Enter type of base (T)hin or (P)an")
    while Choice.upper() != "T" and Choice.upper() != "P":
        print("Error. Not a valid choice")
        Choice = input("Enter type of base (T)hin or (P)an")

    addNode()

    while (TopCount <= 5) and (EndOrder == False):


        Choice = int(input("Enter the topping number (0 to 9)"))
        while Choice < 0 or Choice > 9:
            print("Error. Not a valid choice")
            Choice = int(input("Enter the topping number (0 to 9)"))

        if int(toppings[1][Choice]) > 0:
            pizzaorders[noOrders].dataitem.topping[TopCount] = Choice
            TopCount += 1
            toppings[1][Choice] = str(int(toppings[1][Choice]) - 1)

        Again = input("Want to add another topping?")
        if Again.upper() == "N":
            EndOrder = True

    displayOrder(noOrders)

    Again = input("Want to order another pizza?")
    if Again.upper() == "N":
        ShopOpen = False
    else:
        pizzaorders[noOrders].pointer = noOrders + 1
        noOrders += 1

pizzaorders[noOrders].pointer = nullPtr

print("ALL ORDERS")

Index = startPtr
while (Index != nullPtr):
    displayOrder(Index)
    print("------")
    Index = pizzaorders[Index].pointer