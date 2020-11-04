print("Wilkommen zum Konversionstool")

while True:
    print("Bitte geben Sie einen Euro-Betrag ein, den Sie in Deutsche Mark umrechnen moechten.")

    euro = input("Betrag Euro: ")

    euro = float(euro.replace(",", "."))

    euro = round(euro ,2)

    dm = round(euro * 1.95583 ,2)

    print("{0:.2f} Euro entsprechen {1:.2f} DM".format(euro, dm))

    abfrage = str(input("Moechten Sie eine weitere Umrechnung durchfuehren lassen? (j/n): "))

    if abfrage.lower() != "j" and abfrage.lower != "ja":
        break