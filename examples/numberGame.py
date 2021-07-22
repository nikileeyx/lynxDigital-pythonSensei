# --- By @ryantwt07 --- #

from random import randint

counter = 0
guessed = False
inputSuccess = False

while not inputSuccess:
    user = int(input("Enter Number Between 1 and 100: "))
    if 0 < user < 101:
        inputSuccess = True
    else:
        inputSuccess = False


while counter < 100 and not guessed:
    counter += 1
    comp = randint(1, 100)
    if comp == user:
        print("The computer chose " + str(comp) + ".")
        print("The system took " + str(counter) + " tries to guess your number!")
        guessed = True
    else:
        print("The computer chose " + str(comp) + ".")
else:
    if guessed:
        pass
    else:
        print("The computer ran out of tries!")
