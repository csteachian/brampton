# Ian Simpson
# CompA2/a
# 9th November 2017

# DECLARE counter : INTEGER
counter = 0
# DECLARE teamname : STRING
teamname = "Zeus"
# DECLARE playerhits : INTEGER
playerhits = 0
# DECLARE totalhits : INTEGER
totalhits = 0
# DECLARE averagehits : REAL
averagehits = 0.0
# DECLARE pointsearned : INTEGER
pointsearned = 0

def get_details():
    global teamname, playerhits, totalhits
    teamname = input("Enter team name")

    for counter in range(1,7):
        playerhits = int(input("Enter player hits"))

        totalhits = totalhits + playerhits


get_details()

averagehits = totalhits/6

if totalhits > 50:
    pointsearned = 1

if averagehits >= 10:
    pointsearned = pointsearned + 1

print(teamname," has scored ",pointsearned)


