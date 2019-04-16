# CIE 9608 Paper 42 2018 Q4

class member():
    # Private FirstName : STRING
    # Private LastName : STRING
    # Private DateOfBirth : DATE
    # Private Gender : STRING

    def __init__(self,fname,lname,dob,gen):
        self.__firstname = fname
        self.__lastname = lname
        self.__dateofbirth = dob
        self.__gender = gen

    def introduction(self):
        # output : STRING
        output = "Hello, I'm " + self.__firstname + " " + self.__lastname
        return output

    def displayfullnameanddateofbirth(self):
        # output : STRING
        output = self.__firstname + " " + self.__lastname + " " + str(self.__dateofbirth)
        print(output)

class competitor(member):
    # PRIVATE Sport : STRING

    def __init__(self,fname,lname,dob,gen,sport):
        member.__init__(self,fname,lname,dob,gen)
        self.__sport = sport
 how
    def introduction(self): # polymorphism
        # output : STRING
        output = member.introduction(self) + " and my sport is " + self.__sport
        return output

class official(member):
    # PRIVATE JobTitle : STRING
    # PRIVATE FirstAid : BOOLEAN

    def __init__(self,fname,lname,dob,gen,job,firstaid):
        member.__init__(self,fname,lname,dob,gen)
        self.__jobtitle = job
        self.__firstaid = firstaid

    def introduction(self): # polymorphism
        # output : STRING
        output = member.introduction(self) + " and my job title is " + self.__jobtitle
        return output

# Showing how containment can be implemented (this would have to be in another class)
teamlist = [member("Nadia","Abad","16/05/1995","F"),
            competitor("Nicole","Carrera","01/01/2000","F","Sprinter"),
            official("Ian","Simpson","01/01/0000","M","Tea-maker",False),
            member("Nate","Simpson","20/06/2009","M")]

for index in range(0,4):
    print(teamlist[index].introduction())
    # The advantage of OOP and polymorphism can be seen in the above line of code. You don't need to know what object type each element
    # in teamlist[] is, just that it has access to an introduction method.

# The lines below were used in tutorial to discuss how parameters can be used to create instances of objects quickly without set/get methods
#mem1 = member("Nadia","Abad","16/05/1995","F")
#mem1 = official("Nadia","Abad","16/05/1995","F","Starter", True)
#mem1 = official("Nadia","Abad","16/05/1995","F","Starter", True)
#mem1.introduction()
#mem1.displayfullnameanddateofbirth()
