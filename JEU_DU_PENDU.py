# TP JEU DU PENDU BIEN PENDU


# Cette commande permet d'importer
#une variable et de choisir des choses au hazard
import random
# On crée une  variable qui est une liste des mots,
book_of_rhymes=[]
# Elle permets de stocker la liste des mots dans la variable crée
#A travers le fichier texte
with open("book_of_rhymes.txt") as fl:
#Elle permets ajouter chaque mot à la suite du prédédent
#en revenant à la ligne , c'est pour cela que j'utilise la boucle for.
    for l in fl:
        book_of_rhymes.append(l.rsplit("\n"))
#On utilise la fonction random.choice pour prendre des élements au hazard
mot = random.choice(book_of_rhymes)
# On crée une ensembles de variables importantes
#pour le reste de la procédure qu'on va appeler "variables clés"
# Variables clés
lettres = []
échoué = 0
mots = False
corps_complet =["O","/"," | ","\\", "/", "\\"]
corps = [" ", " ", " ", " ", " ", " "]
#On a créé la boucle "while"
#Elle permet de déssiner le part du pendu 
#à chaque fois, que le joueur échoue
while not mots:
    #On affiche que  le mots est vrai si respecte la condition if 
    # qui est dans la première condition if de la boucle for
    mots = True
    # Cette partie de prints permet d'afficher le pendu
    # au fur et à mesure que le joueur perd
    print(" +----+")
    print(" |    |")
    print(" |    {}".format(corps[0]))
    print(" |  {}{}{}".format(corps[1], corps[2], corps[3]))
    print(" |   {} {}".format(corps[4], corps[5]))
    print("_|_")
    print("| |")
    #On crée la boucle for pour les essaies de joueur
    for l in mot:
        #Si le joueur mots à deviner, on l'affiche la lettre et l'espace pour la lettre suivante
        if l in lettres:
            print(l, end=" ")
        #Sinon , on affiche rien 
        else:
            mots = False
            print("_", end=" ")
    print()
    print("Lettres utilisées - ", end="")
    for l in lettres:
        print(l, end=" | ")
    print()
    # Dans ce 2ème if , si le joueur a échoué 6fois
    # La boucle se casse, et il recommance une nouvelle partie

    if échoué > 5: 
      print("Shiiiitt , va écouter <<LOSE YOURSELF>> D'EMINEM!")
      print("Mot - {} -".format(mot))
      break
    # Dans ce 3ème if , si le joueur a réussit , la boucle s'arrête 
    # et on affiche la phrase dans le print.
    if mots:
        print("Tu as gagné ,bravo mais va quand écouter <<Till'i collapse>> d'Eminem")
        break
    # On a crée une variable lettre , qui possède la commande input permettant
    # d'insérer une lettre dans celle-ci .
    # Et la fonction lettre.append(lettre) permet de transférer la lettre trouvé dans
    # la variable lettres
    lettre = input("Entrez une lettre: ") 
    lettres.append(lettre)
    
    #  Ici , on créé une condition qui permet d'ajouter 1
    # sur le compteur sur la variable "échoué" à chaque fois                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    # que le joueur échoue à un essaie
    
    if lettre not in mot:
        corps[échoué] = corps_complet[échoué]
        échoué += 1

    # Une lettre
    # Mot?
    # Gagne/perdu/continue












































































