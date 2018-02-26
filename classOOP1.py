# OOP 1
class person:
    #PRIVATE name : STRING
    #PRIVATE age : INTEGER
    #PRIVATE address : STRING

    def display(self):
        print("Person")
        print(self.name)
        print(self.age)
        print(self.address)

    def __init__(self):
        self.name = "Mr X"
        self.age = 15
        self.address = "1 High Street"

class student(person):
    #PRIVATE studentID : STRING

    def display(self):
        print(self.studentID)
        print(self.name)
        print(self.age)
        print(self.address)

    def __init__(self):
        print("Student")
        self.studentID = "S001"
        super().__init__()

class teacher(person):
    # PRIVATE teacherID : STRING
    # PRIVATE specialism : STRING

    def display(self):
        print(self.teacherID)
        print(self.specialism)
        print(self.name)
        print(self.age)
        print(self.address)


    def __init__(self):
        super().__init__()
        print("Teacher")
        self.teacherID = "T001"
        self.specialism = "Computer Science"


a = person() # Can change this to student, teacher or person
a.display()