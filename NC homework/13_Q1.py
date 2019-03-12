"""1. In Python create a hashing function that takes in a three letter sequence, and calculates the hash value
using the following formula:
Hash value = sum of ASCII values for each character % (mod) 12.
The hash value should then be returned to the calling function.
"""
charF = input("Enter character")
charM = input("Enter middle character")
charL = input("Enter Last character")

def HashAlgorithm(charF,charM,charL):
    Charactersum = ord(charF) + ord(charM) + ord(charL) #Add up ascii values of characters
    HashValue = Charactersum % 12 #hashing algorithm
    return HashValue

print(HashAlgorithm(charF, charM, charL)) # you just forgot this
