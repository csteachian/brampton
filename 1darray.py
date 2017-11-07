# 1D array
# 7/11/17

# DECLARE ages : ARRAY[0..9] OF INTEGER
# ages = [9,15,6,88,34,65,74,15,8,9]
ages = []
for index in range(0,10):
    num = input("Enter an age (0-10)")
    while num < 0 or num > 10:
        print("Error. Try again.")
        num = input("Enter an age (0-10)")
    ages.append(num) # I didn't tell you this

for index in range(0,10):
    print(ages[index])

for y in range(0,10):
    for x in range(0,9):
        if ages[x] > ages[x+1]:
            temp = ages[x]
            ages[x] = ages[x+1]
            ages[x+1] = temp

print()

for index in range(0,10):
    print(ages[index])