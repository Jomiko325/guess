with open("names.csv", "r") as names_file:
    names = names_file.read().splitlines()

    for reihe in names:
        reihe_inhalt = reihe.split(",")
        print("{0} ist {1} Jahre alt und {2}".format(reihe_inhalt[0], reihe_inhalt[1], reihe_inhalt[2]))