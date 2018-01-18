# 2D array helpme
# Ian Simpson
# 18th January 2018

# DECLARE timmeh : ARRAY[1..2, 1..6] OF CHAR
#timmeh = [['0' for r in range(1,3)]for c in range(1,6)]

timmeh = [['h','1'],['e','2'],['l','3'],['p','4'],['m','5'],['e','-1']]
print(timmeh)

index = 0
while index != -1:
    print(timmeh[index][0])
    index = int(timmeh[index][1])


