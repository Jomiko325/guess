print("Willkommen beim FizzBuzz Game")

while True:

    grenzzahl = input("Gib eine Zahl zwischen 1 und 100 ein: ")

    grenzzahl = int(grenzzahl)

    for zahl in range(1, grenzzahl+1):
        if zahl % 3 == 0 and zahl % 5 == 0:
            print("FizzBuzz")
        elif zahl % 3 == 0:
            print("Fizz")
        elif zahl % 5 == 0:
            print("Buzz")
        else:
            print(zahl)

    abfrage = str(input("Moechtest du eine weitere Runde spielen? (j/n): "))

    if abfrage.lower() != "j" and abfrage.lower != "ja":
        break