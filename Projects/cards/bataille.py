from random import shuffle

print("Le jeu de bataille démarre...")

rangs = [1,2,3,4,5,6,7,8,9,10,"valet","dame","roi",]


# Fonction pour la création du jeu initial, apour une couleur donnée
def creation(couleur):
    return [(couleur, points+1, rangs[points]) for points in range(13)]


# On laisse au joueur1 le choix de la couleur
a = int(input("Joueur 1 choisissez; 1=trèfle 2=pique "))
if a == 1:
    Player1 = creation("trèfle")
    Player2 = creation("pique")
else:
    Player1 = creation("pique")
    Player2 = creation("trèfle")

# Pour mélanger les cartes des deux joueurs:
shuffle(Player1)
shuffle(Player2)

print("Joueur1", Player1)
print("Joueur2", Player2)