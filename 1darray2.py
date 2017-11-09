# DECLARE ages : ARRAY[0..9] OF INTEGER
# DECLARE temp : INTEGER
#ages = [43,65,34,63,13,78,64,26,9,4]

def output_array_contents():
    # DECLARE index : INTEGER
    fh = open("num.txt","w")
    for index in range(0,10):
        fh.write(str(ages[index]))
        #print(ages[index])
    fh.close()

def bubble_sort():
    for passes in range(0, 9):
        for index in range(0, 9):
            if ages[index] > ages[index + 1]:
                temp = ages[index]
                ages[index] = ages[index + 1]
                ages[index + 1] = temp

def get_valid_age(): # RETURNS integer
    temp = int(input("Enter age (0-99)"))
    while temp < 0 or temp > 99:
        print("Error.")
        temp = int(input("Enter age (0-99)"))
    return temp

ages = []
for index in range(0,10):
    ages.append(get_valid_age())
output_array_contents()
bubble_sort()
output_array_contents()
