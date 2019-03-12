# Read StudentFile.Dat
# Prep work for CIE 9608 Binary File Pseudocode example
# By Ian Simpson (@familysimpson)
import datetime

# Code to define Student record
class Student:
    def __init__(self):
        self.Surname = "" # DECLARE Surname : STRING
        self.Firstname = "" # DECLARE Firstname : STRING
        self.DateOfBirth = datetime.date(1900,1,1) # DECLARE DateOfBirth :
        self.YearGroup = 0 # DECLARE YearGroup : INTEGER
        self.FormGroup = "" # DECLARE FormGroup : CHAR

# DECLARE record_size : INTEGER
record_size = 25 # Each record is 25 bytes
# DECLARE Position : INTEGER
Position = 0
# DECLARE Students : ARRAY[0..20] of Student
Students = []

def display_pupil(ThisPupil):
    print(ThisPupil.Surname,
          ThisPupil.Firstname,
          str(ThisPupil.DateOfBirth.toordinal()),
          str(ThisPupil.YearGroup),
          ThisPupil.FormGroup)
    print("=============")

def GetRecord(bytestream):
    ReturnStudent = Student()
    print(len(bytestream),bytestream) # This shows record in bytes
    
    # Each record is 25 bytes
    # Surname is 10 bytes
    ReturnStudent.Surname = (bytestream[:10]).decode("UTF-8").strip()
    # Firstname is 10 bytes
    ReturnStudent.Firstname = (bytestream[10:20]).decode("UTF-8").strip()
    # DateOfBirth is 3 bytes
    ReturnStudent.DateOfBirth = datetime.date.fromordinal(int.from_bytes(bytestream[20:23],byteorder="big"))
    # YearGroup is 1 byte    
    ReturnStudent.YearGroup = int.from_bytes(bytestream[23:24], byteorder="big")
    # FormGroup is 1 byte
    ReturnStudent.FormGroup = (bytestream[24:]).decode("UTF-8")
    return ReturnStudent
    

#OPENFILE StudentFile.Dat FOR RANDOM
binary_file = open("StudentFile.Dat", "rb")
print("Open file")
# FOR Position = 0 TO 20
for Position in range(0,21):
    # DECLARE Pupil : Student
    Pupil = Student()

#   SEEK StudentFile.Dat, Position (* size of record)
    binary_file.seek(Position*record_size)
#   GETRECORD StudentFile.Dat, Pupil
    Pupil = GetRecord(binary_file.read(25))

    Students.append(Pupil)
    display_pupil(Pupil)
# ENDFOR
#CLOSEFILE StudentFile.Dat
print("Close file")
binary_file.close()
