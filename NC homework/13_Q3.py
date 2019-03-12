"""
3.The data structure used to hold the three letter sequences is a list named Airport. This list can hold 2000 elements.
In Python create a procedure to add each three letter sequence to the appropriate index in the list.
"""
#DECLARE Airport: ARRAY [0:1999] OF CHAR
Airport = [""] * 2000

def HashAlgorithm(charF,charM,charL):
    Charactersum = ord(charF) + ord(charM) + ord(charL) #Add up ascii values of characters
    HashValue = Charactersum % 12 #hashing algorithm
    return HashValue

def InsertintoHashTable (charF,charM,charL):
    index = HashAlgorithm(charF,charM,charL)
    if Airport[index] == "":
        Airport[index] = charF + charM + charL
    else:
        print("ERROR!Hash overflow!")

# Main program
while True: # This repeats forever so you can test multiple hashes
    charF = input("Enter character")
    charM = input("Enter middle character")
    charL = input("Enter Last character")

    print(HashAlgorithm(charF, charM, charL))

    InsertintoHashTable(charF, charM, charL) # you just forgot this
    for index in range(0,2000): # display all non null values in Airport list
        if Airport[index] != "":
            print(index,Airport[index])
            
    """ Notice when you run the program that there are limited values possible using the
    HashAlgorithm function. Because you MOD 12 there are only possible index values
    between 0 and 11. To increase the efficiency of the program you can either reduce
    the size of the Airport list to 12 items (0-11) OR MOD 2000.
    """
