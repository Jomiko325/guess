# bestehende Programme nutzen, connecten
# random zufallsgenerator
# libraries (fertig entwickelte Datenpakete/Programme)
import random

secret_number = random.randint(1,30) #random integer zahl zwischen 1 und 30

print(secret_number)

while True:
    guess_number = input("geben Sie eine Zahl ein:\n")
    if(int(guess_number) > secret_number):
        print("falsch, Zahl leider zu groß")
    elif(int(guess_number) < secret_number):
        print("falsch, Zahl leider zu klein")
    elif(int(guess_number) == secret_number):
        print("korrekt")
        break

