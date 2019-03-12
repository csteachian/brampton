# Make StudentFile.Dat
# Prep work for CIE 9608 Pseudocode example
# By Ian Simpson (@familysimpson)
import datetime, random

# Code to define Student record
class Student:
    def __init__(self):
        self.Surname = "" # DECLARE Surname : STRING
        self.Firstname = "" # DECLARE Firstname : STRING
        self.DateOfBirth = datetime.date(1900,1,1) # DECLARE DateOfBirth :
        self.YearGroup = 0 # DECLARE YearGroup : INTEGER
        self.FormGroup = "" # DECLARE FormGroup : CHAR

# DECLARE NewPupil : Student
NewPupil = Student()
# DECLARE Position : INTEGER
Position = 0
# DECLARE Students : ARRAY[0..20] of Student
Students = []

# Set up source data for random name generator
Surnames = ["Simpson","Carrera","Thomas","Cornett","Turing"]
Firstnames = ["Ian","Nicole","Liam","Joel","Alan"]

def display_pupil(ThisPupil):
    print(ThisPupil.Surname,
          ThisPupil.Firstname,
          str(ThisPupil.DateOfBirth.toordinal()),
          str(ThisPupil.YearGroup),
          ThisPupil.FormGroup)
    print("=============")

for Position in range(0,21):
    # DECLARE NewPupil : Student
    NewPupil = Student()

    #NewPupil.Surname <-- "Johnson"
    NewPupil.Surname = random.choice(Surnames)
    #NewPupil.Firstname <-- "Leroy"
    NewPupil.Firstname = random.choice(Firstnames)
    #NewPupil.DateOfBirth <-- 02/01/2005
    NewPupil.DateOfBirth = datetime.date(random.randint(1900,2019),random.randint(1,12),random.randint(1,28))
    #NewPupil.YearGroup <-- 6
    NewPupil.YearGroup = random.randint(1,13)
    #NewPupil.FormGroup <-- "A"
    NewPupil.FormGroup = chr(random.randint(65,90))

    display_pupil(NewPupil)

    # Add NewPupil to Students array
    Students.append(NewPupil)

#OPENFILE StudentFile.Dat FOR RANDOM
binary_file = open("StudentFile.Dat", "wb")
# FOR Position = 0 TO 20
for Position in range(0,21):
    # Create the information from the current record to store
    output = bytes(Students[Position].Surname[:10],"utf-8")
    print(len(output), " after surname")
    len_diff = 10-len(output)
    print(len_diff)
    output += bytes("\0","utf-8") * len_diff # add padding to make exactly 10 bytes
    
    output += bytes(Students[Position].Firstname[:10],"utf-8")
    print(len(output), " after firstname")
    len_diff = 20-len(output)
    print(len_diff)
    output += bytes("\0","utf-8") * len_diff # add padding to make exactly 10 bytes
    
    
    x = Students[Position].DateOfBirth.toordinal()
    output += x.to_bytes((x.bit_length() + 7) // 8, 'big')
    print(len(output), " after DOB")
    
    x = Students[Position].YearGroup
    output += x.to_bytes((x.bit_length() + 7) // 8, 'big')
    print(len(output), " after yeargroup")
    
    output += bytes(Students[Position].FormGroup,"utf-8")
    print(len(output), " after formgroup")

    len_diff = 25-len(output)
    print(len_diff)
    output += bytes("\0","utf-8") * len_diff # add padding to make exactly 25 bytes
    
    num_bytes_written = binary_file.write(bytes(output))
    print("Bytes written for ",Position,": ",num_bytes_written)
# ENDFOR
#CLOSEFILE StudentFile.Dat
binary_file.close()
