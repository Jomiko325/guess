print("Wilkommen zum Konversionstool")

while True:
    print("Bitte geben Sie einen Euro-Betrag ein, den Sie in Deutsche Mark umrechnen möchten.")

    euro = input("Betrag: €")

    euro = float(euro.replace(",", "."))

    euro = round(euro ,2)

    dm = round(euro * 1.95583 ,2)

    print("{0:.2f} € entsprechen {1} DM".format(euro, dm))

    abfrage = str(input("Möchten Sie eine weitere Umrechnung durchführen lassen? (j/n): "))

    if abfrage.lower() != "j" and abfrage.lower != "ja":
        break