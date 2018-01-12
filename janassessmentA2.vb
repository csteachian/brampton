Module Module1
    ' Pizza manager
    ' Ian Simpson
    ' 12th January 2018

    Dim Choice As String = ""
    Dim Again As String = ""
    Dim TopCount As Integer = 0
    Dim Index As Integer = 0
    Dim ShopOpen As Boolean = True
    Dim EndOrder As Boolean = False
    Dim noOrders As Integer = 0

    Dim toppings(1, 9) As String

    Structure order
        Dim no As Integer
        Dim base As String
        Dim topping() As String
    End Structure

    ' LINKED LIST NODE SETUP
    Structure node
        Dim dataitem As order
        Dim pointer As Integer
    End Structure

    Dim pizzaorders(10) As node
    Const nullPtr = -1
    Dim startPtr = nullPtr

    Sub Main()
        toppings(0, 0) = "Cheese"
        toppings(0, 1) = "Ham"
        toppings(0, 2) = "Pepperoni"
        toppings(0, 3) = "Pineapple"
        toppings(0, 4) = "Mushroom"
        toppings(0, 5) = "Cherry Tomatoes"
        toppings(0, 6) = "Chicken"
        toppings(0, 7) = "Peppers"
        toppings(0, 8) = "Olives"
        toppings(0, 9) = "Jalapenos"
        toppings(1, 0) = "10"
        toppings(1, 1) = "10"
        toppings(1, 2) = "10"
        toppings(1, 3) = "10"
        toppings(1, 4) = "10"
        toppings(1, 5) = "10"
        toppings(1, 6) = "10"
        toppings(1, 7) = "10"
        toppings(1, 8) = "10"
        toppings(1, 9) = "10"

        While (noOrders <= 9) And (ShopOpen = True)
            EndOrder = False
            TopCount = 0

            For Index = 0 To 9
                Console.WriteLine(Index & " " & toppings(0, Index) & " " & toppings(1, Index))
            Next Index

            Console.WriteLine("Enter type of base (T)hin or (P)an")
            Choice = Console.ReadLine()
            While Choice.ToUpper() <> "T" And Choice.ToUpper() <> "P"
                Console.WriteLine("Error. Not a valid choice")
                Console.WriteLine("Enter type of base (T)hin or (P)an")
                Choice = Console.ReadLine()
            End While

            Call addNode()


            While (TopCount <= 5) And (EndOrder = False)

                Console.WriteLine("Enter the topping number (0 to 9)")
                Choice = Console.ReadLine()
                While Int(Choice) < 0 Or Int(Choice) > 9
                    Console.WriteLine("Error. Not a valid choice")
                    Console.WriteLine("Enter the topping number (0 to 9)")
                    Choice = Console.ReadLine()
                End While

                If Int(toppings(1, Choice)) > 0 Then
                    pizzaorders(noOrders).dataitem.topping(TopCount) = Choice
                    TopCount += 1
                    toppings(1, Choice) = Str(Int(toppings(1, Choice)) - 1)
                End If

                Console.WriteLine("Want to add another topping?")
                Again = Console.ReadLine()
                If Again.ToUpper() = "N" Then
                    EndOrder = True
                End If

            End While

            Console.WriteLine(pizzaorders(noOrders).dataitem.no)
            Console.WriteLine(pizzaorders(noOrders).dataitem.base)
            For Index = 0 To 4
                If pizzaorders(noOrders).dataitem.topping(Index) <> -1 Then
                    Console.WriteLine(toppings(0, pizzaorders(noOrders).dataitem.topping(Index)))
                End If
            Next Index

            pizzaorders(noOrders).pointer = noOrders + 1



            Console.WriteLine("Want to order another pizza?")
            Again = Console.ReadLine()
            If Again.ToUpper() = "N" Then
                ShopOpen = False
            Else
                noOrders += 1
            End If

        End While

        pizzaorders(noOrders).pointer = nullPtr

        Console.WriteLine("ALL ORDERS")

        Index = startPtr
        While (Index <> nullPtr)
            Console.WriteLine(pizzaorders(Index).dataitem.no)
            Console.WriteLine(pizzaorders(Index).dataitem.base)
            For i = 0 To 4
                If pizzaorders(Index).dataitem.topping(i) <> -1 Then
                    Console.WriteLine(toppings(0, pizzaorders(Index).dataitem.topping(i)))
                End If
            Next i
            Console.WriteLine("------")
            Index = pizzaorders(Index).pointer
        End While


        Console.ReadLine()
    End Sub

    Sub addNode()
        If startPtr = -1 Then
            startPtr = 0
        End If
        pizzaorders(noOrders).dataitem.base = Choice
        pizzaorders(noOrders).dataitem.no = noOrders + 1
        ReDim pizzaorders(noOrders).dataitem.topping(4)
        pizzaorders(noOrders).dataitem.topping = {-1, -1, -1, -1, -1}
    End Sub

End Module
