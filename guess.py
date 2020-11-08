# bestehende Programme nutzen, connecten
# random zufallsgenerator
# libraries (fertig entwickelte Datenpakete/Programme)
import random

secret_number = random.randint(1,30) #random integer zahl zwischen 1 und 30
attempts = 0

with open("highscore.txt", "r") as highscore_file:
    highscore = int(highscore_file.read())
    print("Der Highscore liegt bei " + str(highscore))

while True:
    guess_number = input("Geben Sie eine Zahl zwischen 1 und 30 ein:\n")
    attempts += 1

    if(int(guess_number) > secret_number):
        print("Falsch, Zahl leider zu groß")
    elif(int(guess_number) < secret_number):
        print("Falsch, Zahl leider zu klein")
    elif(int(guess_number) == secret_number):
        if attempts < highscore:
            with open("highscore.txt" ,"w") as highscore_file:
                highscore_file.write(str(attempts))
        print("Korrekt, es ist die Nummmer " + str(secret_number))
        print("Benötigte Versuche: " + str(attempts))
        break

