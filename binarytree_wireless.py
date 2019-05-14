class node:
    def _init_ (self):
        self.__data = none
        self.__lp = none
        self.__rp = none

    def setData(self,data):
        self.__data = data

    def getData(self):
        return self.__data

    def setLP(self, leftpointer):
        self.__leftpointer = leftpointer

    def getLP(self):
        return self.__leftpointer

    def setRP(self,Rightpointer):
        self.__RightPointer = Rightpointer

    def getRP(self):
        return self.__RightPointer

WirelessBTS =[node(),node(),node(),node(),node(),node(),node(),node(),node(),node(),node()]

WirelessBTS[0].setData("Drake")
WirelessBTS[0].setRP(1)
WirelessBTS[0].setLP(3)

WirelessBTS[1].setData("Nicki")
WirelessBTS[1].setRP(2)
WirelessBTS[1].setLP(6)

WirelessBTS[2].setData("PND")
WirelessBTS[2].setRP(4)
WirelessBTS[2].setLP(-1)

WirelessBTS[3].setData("Chris")
WirelessBTS[3].setRP(-1)
WirelessBTS[3].setLP(5)

WirelessBTS[4].setData("Tory")
WirelessBTS[4].setRP(-1)
WirelessBTS[4].setLP(9)

WirelessBTS[5].setData("August")
WirelessBTS[5].setRP(7)
WirelessBTS[5].setLP(-1)

WirelessBTS[6].setData("Lil")
WirelessBTS[6].setRP(-1)
WirelessBTS[6].setLP(8)

WirelessBTS[7].setData("BabyFace")
WirelessBTS[7].setRP(-1)
WirelessBTS[7].setLP(-1)

WirelessBTS[8].setData("Jon")
WirelessBTS[8].setRP(-1)
WirelessBTS[8].setLP(-1)

WirelessBTS[9].setData("Skepta")
WirelessBTS[9].setRP(-1)
WirelessBTS[9].setLP(-1)

FreePointer = 10
RootPointer = 0 # at least one node
#NewItem = "Travis"
def insertNewItem(NewItem):
    global RootPointer, FreePointer
    
    if FreePointer != -1:
    #Then there is space in the list
    #slot data into free pointer spot
        NewNode= FreePointer
        WirelessBTS[NewNode].setData(NewItem)
        WirelessBTS[NewNode].setLP(-1)
        WirelessBTS[NewNode].setRP(-1)
    #CHECK IF THERE IS IN ANY NODES IN LIST
    if RootPointer == -1:
        RootPointer = 0 ## THIS IS NEW
        #Insert new item at start of the binary tree
        RootPointer = FreePointer
        FreePointer = FreePointer + 1
    else:
        NextPtr = RootPointer
        while NextPtr != -1:
            # look at each node data
            CurrentPtr = NextPtr
            CurrentNodeData = WirelessBTS[CurrentPtr].getData()
            # comparing the string
            PrevPtr = CurrentPtr
            if CurrentNodeData < NewItem:
                NextPtr = WirelessBTS[CurrentPtr].getRP()
                TurnLeft = False
            else:
                NextPtr = WirelessBTS[CurrentPtr].getLP()
                TurnLeft = True
        #end while    
        
        if TurnLeft:
            WirelessBTS[PrevPtr].setLP(FreePointer)
        else:
            WirelessBTS[PrevPtr].setRP(FreePointer)
        #find insertion point
        #PreviousPtr = RootPointer
        #ThisPtr = WirelessBTS[RootPointer]
        FreePointer = FreePointer + 1

insertNewItem("Travis")
for x in range(0,11):
    print(x)
    print("LP is: ",WirelessBTS[x].getLP())
    print("Artist is: ",WirelessBTS[x].getData())
    print("RP is: ",WirelessBTS[x].getRP())
    print('----')

