# DECLARE ages : ARRAY[0..9] OF INTEGER
# DECLARE temp : INTEGER
#ages = [43,65,34,63,13,78,64,26,9,4]
ages = []
for index in range(0,10):
    temp = int(input("Enter age (0-99)"))
    while temp < 0 or temp > 99:
        print("Error.")
        temp = int(input("Enter age (0-99)"))
    ages.append(temp)

for index in range(0,10):
    print(ages[index])

for passes in range(0, 9):
    for index in range(0, 9):
        if ages[index] > ages[index+1]:
            temp = ages[index]
            ages[index] = ages[index+1]
            ages[index+1] = temp

for index in range(0, 10):
    print(ages[index])





                #ages.append(45)