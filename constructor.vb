Module module1

    Class Human
        Public Name As String
        Public Age As Integer
        Public Home_Address As String

        Sub display()
            Console.WriteLine("Human")
            Console.WriteLine(Name & Age & Home_Address)
        End Sub

        Sub vbset()
        End Sub

        Sub New()
            Name = "Ricky"
            Age = 15
            Home_Address = "1 Shah Street"

        End Sub
    End Class

    Class Student
        Inherits Human
        Private Student_ID As Integer

        Sub display()
            Console.WriteLine("Student " & Student_ID)
            Console.WriteLine(Name & Age & Home_Address) ' Information from the superclass
        End Sub

        Sub vbset()
        End Sub

        Sub New()
            Student_ID = 3

        End Sub
    End Class

    Class Teacher
        Inherits Human
        Private Employee_ID As Integer
        Private Subject_Specialism As String

        Sub vbset()
        End Sub

        Sub display()
            Console.WriteLine("Teacher " & Employee_ID)
            Console.WriteLine(Name & Age & Home_Address) ' Information from the superclass
            Console.WriteLine(Subject_Specialism)
        End Sub

        Sub New()
            Employee_ID = 66
            Subject_Specialism = "Computer Science"

        End Sub
    End Class

    Sub main()
        Dim a As New Teacher ' You can change this to Human, Student or Teacher and run it to see the different values
        a.display()
        Console.ReadLine()
    End Sub

End Module
