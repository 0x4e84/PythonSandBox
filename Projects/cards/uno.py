from tkinter import *

from random import choice, shuffle


# On crée la carte avec le symbole désiré pour les 4 différentes couleurs dans une liste
def creer_cartes_couleurs(symbole):
    # Variante courte, appelée "list comprehension":
    #return [{"couleur": couleur, "symbole": symbole} for couleur in ['bleu', 'rouge', 'jaune', 'vert']]

    # Variante classique:
    cartes = []
    for couleur in ['bleu', 'rouge', 'jaune', 'vert']:
        cartes += [{"couleur": couleur, "symbole": symbole}]
    return cartes


# On crée la carte avec le symbole désiré pour les 4 différentes couleurs dans une liste
def creer_4_cartes_speciales(symbole):
    return [{"couleur": "spéciale", "symbole": symbole} for i in range(4)]


# On affiche la liste des cartes
def afficher_liste_cartes(pile):
    liste = "{} cartes: \n".format(len(pile))
    for carte in pile:
        liste += "  {} ({})\n".format(carte["symbole"], carte["couleur"])
    return liste


# On retire la première carte de la pioche
def piocher_une_carte():
    return cartes_pioche.pop(0)


# Initialisation des variables
cartes_joueur1 = []
cartes_joueur2 = []
cartes_pioche = []
cartes_tapis = []
couleur_actuelle = "indéfini"
joueur_ayant_la_main = "indéfini"


# On crée toutes les cartes du jeu et on les rajoute dans la pile de la pioche
# La carte "0": 1x pour chaque couleur
cartes_pioche += creer_cartes_couleurs("0")

# Il y a deux cartes de chacune des cartes suivantes
for i in range(2):
    # Les cartes de "1" à "9"
    for j in range(1, 10):
        # La variable "j" prend toutes les valeurs de 1 à 9, on l'utilise pour définir le symbole de la carte
        symbole = str(j)
        cartes_pioche += creer_cartes_couleurs(symbole)

    # Les cartes "+2", "changement de sens", "passe"
    cartes_pioche += creer_cartes_couleurs("+2")
    cartes_pioche += creer_cartes_couleurs("changement de sens")
    cartes_pioche += creer_cartes_couleurs("passe")

# Les cartes spéciales
cartes_pioche += creer_4_cartes_speciales("+4")
cartes_pioche += creer_4_cartes_speciales("changement de couleur")

print("Pioche: ", afficher_liste_cartes(cartes_pioche))

# Mélange des cartes
shuffle(cartes_pioche)

# Distribution de 7 cartes à chaque joueur
for i in range(7):
    cartes_joueur1.append(piocher_une_carte())
    cartes_joueur2.append(piocher_une_carte())

print("Joueur 1: ", afficher_liste_cartes(cartes_joueur1))
print("Joueur 2: ", afficher_liste_cartes(cartes_joueur2))

# On tire au sort quel joueur commence
joueur_ayant_la_main = choice(["Joueur1", "Joueur2"])
print("{} commence la partie".format(joueur_ayant_la_main))

# On lit la première carte de la pioche. C'est elle qui détermine ce qui peut être posé par le premier joueur
premiere_carte = cartes_pioche[0]
# Pour définir la couleur actuelle, on lit le paramètre "couleur" de cette carte
couleur_actuelle = premiere_carte["couleur"]
print("Première carte: {} ({})".format(premiere_carte["symbole"], premiere_carte["couleur"]))
