#mini-calculator

zahl1 = input("Geben Sie die erste Zahl ein:\n")
zahl2 = input("Geben Sie die zweite Zahl ein:\n")

rechenoperation = input("Geben Sie die Rechenoperation ein: +,-,*,/\n")


if(rechenoperation == "+"):
    print(float(zahl1) + float(zahl2))
elif(rechenoperation == "-"):
    print(float(zahl1) - float(zahl2))
elif(rechenoperation == "*"):
    print(float(zahl1) * float(zahl2))
else: #try/except (dividieren durch 0)
    try:
        print(float(zahl1) / float(zahl2))
    except Exception as e:
        print("Fehler: ",e)