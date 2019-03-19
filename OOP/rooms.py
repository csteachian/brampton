class Room():
    def __init__(self):
        self.roomNumber = 0
        self.price = 0.0
        self.beds = 0
        self.empty = True

    def setRoom(num):
        self.roomNumber = num

    def setPrice(this):
        self.price = this

    def setBeds(this):
        self.beds = this

    def setEmpty(value):
        self.empty = value

    def getRoom():
        return self.roomNumber
    
    def getPrice():
        return self.price
    
    def getBeds():
        return self.beds
    
    def getEmpty():
        return self.empty
# -- end of class

def allocateRoom(roomNumber):
    isSuccess = False
    currentRoom = allRooms[roomNumber]
    if currentRoom.getEmpty == True:
        currentRoom.setEmpty(False)
        isSuccess = True
    return isSuccess


# main program
allRooms = []
for num in range(1,101):
    newRoom = Room()
    newRoom.setRoom(num)
    newRoom.setBeds(random.randInt(1,4))
    newRoom.setPrice(39.99)
    newRoom.setEmpty = True
    allRooms.append(newRoom)
