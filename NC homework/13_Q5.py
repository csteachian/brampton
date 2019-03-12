"""
5.Alter the Python code you created in Q3 to resolve the hash overflow error
I have started with the same code as in Q3
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
        # Now need to look for next available free space, assume there is
        while (len(Airport[index]) != 0) and (Airport[index] != charF+charM+charL):
            index = index + 1
            if index > 1999: # loops around to start of list if end is reached
                index = 0
        Airport[index] = charF + charM + charL
        """ The above code will add the three character string to the next available
        empty space in the Airport list. Not the BEST solution to the problem but
        definitely the easiest to program / design in an exam. Also ensures that multiple
        copies of the same three character sequence are not added to the Airport list.
        """

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
