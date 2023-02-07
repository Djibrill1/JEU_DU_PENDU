import random

# Choisi un mot
mots = []
with open("book_of_rhymes.txt") as fl:
    for l in fl:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)

# Variable cle
book_of_rhymes = []
échoué = 0
mots = False
corps_complet = ["O", "/", "|", "\\", "/", "\\"]
corps = [" ", " ", " ", " ", " ", " "]

while not mots:
    mots = True
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(corps[0]))
    print(" |  {}{}{}".format(corps[1], corps[2], corps[3]))
    print(" |  {} {}".format(corps[4], corps[5]))
    print("_|_")
    print("| |")
    for l in mot:
        if l in book_of_rhymes:
            print(l, end=" ")
        else:
            mots = False
            print("_", end=" ")
    print()
    print("book_of_rhymes utilisees - ", end="")
    for l in book_of_rhymes:
        print(l, end=" | ")
    print()

    if échoué > 5:
        print("Shiiiitt , va écouter <<LOSE YOURSELF>> D'EMINEM!")
        print("Mot - {} -".format(mot))
        break
    
    if mots:
        print("Tu as gagné ,bravo mais va quand écouter <<Till'i collapse>> d'Eminem!")
        break

    lettre = input("Entez une lettre: ")
    book_of_rhymes.append(lettre)

    if lettre not in mot:
        corps[échoué] = corps_complet[échoué]
        échoué += 1