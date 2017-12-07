# December programming challenge
# Ian Simpson
# 7th December 2017
import random

def getValidNumber(answer):
    noAttempts = 0
    guess = -1
    while guess != answer:
        guess = int(input("Enter a number between 1 and 10"))
        noAttempts += 1
        while guess < 1 or guess > 10:
            print("Not a valid number. Try again.")
            guess = int(input("Enter a number between 1 and 10"))
        if guess == answer:
            print("Correct!")
    return noAttempts

whatToDo = ""
teams = []
player = []
attempts = []
for index in range(1,5):
    teams.append(input(("Enter team name "+str(index))))

while whatToDo.lower() != "quit":
    player.clear()
    attempts.clear()

    for index in range(1,3):
        random.seed()
        num = random.randint(0,3)
        player.append(teams[num])
        print("Player "+str(index)+" is: ",player[index-1])

    for index in range(0,2):
        random.seed()
        answer = random.randint(1,10)
        attempts.append(getValidNumber(answer))
        print("Player "+str(index+1)+" [",player[index],"] took "+str(attempts[index])+" attempts.")

    if attempts[0] < attempts[1]:
        print(player[0]+" wins!")
    elif attempts[0] == attempts[1]:
        print("It's a draw.")
    else:
        print(player[1]+" wins!")

    whatToDo = input("Play again (Y) or (QUIT)?")