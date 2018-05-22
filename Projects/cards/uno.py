from tkinter import *

from random import choice, shuffle


# Affichage de la liste des cartes dans une pile
def afficher_liste_cartes(pile):
    liste = "{} cartes: \n".format(len(pile))
    for carte in pile:
        liste += "  {} ({})\n".format(carte["symbole"], carte["couleur"])
    return liste


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


# On crée toutes les cartes dans une liste
def creer_toutes_les_cartes():
    cartes = []
    # La carte "0": 1x pour chaque couleur
    cartes += creer_cartes_couleurs("0")

    # Il y a deux cartes de chacune des cartes suivantes
    for i in range(2):
        # Les cartes de "1" à "9"
        for j in range(1, 10):
            # La variable "j" prend toutes les valeurs de 1 à 9, on l'utilise pour définir le symbole de la carte
            symbole = str(j)
            cartes += creer_cartes_couleurs(symbole)

        # Les cartes "+2", "changement de sens", "passe"
        cartes += creer_cartes_couleurs("+2")
        cartes += creer_cartes_couleurs("changement de sens")
        cartes += creer_cartes_couleurs("passe")

    # Les cartes spéciales
    cartes += creer_4_cartes_speciales("+4")
    cartes += creer_4_cartes_speciales("changement de couleur")
    return cartes


# Mélange des cartes
def melanger_la_pioche():
    shuffle(cartes_pioche)


# On retire la première carte de la pioche
def piocher_une_carte():
    return cartes_pioche.pop(0)


# On retire la première carte de la pioche
def piocher_une_carte_et_la_jouer_sur_le_tapis():
    carte = piocher_une_carte()
    cartes_tapis.append(carte)
    # Pour définir la couleur actuelle, on lit le paramètre "couleur" de cette carte
    # Ici il faut utiliser le mot-clef "global" car on change la valeur de ce paramètre défini ailleurs
    global couleur_actuelle
    couleur_actuelle = carte["couleur"]
    print("Première carte: {} ({})".format(carte["symbole"], carte["couleur"]))
    return carte


# Distribution de 7 cartes à chaque joueur
def distribuer_les_cartes():
    for i in range(7):
        cartes_joueur1.append(piocher_une_carte())
        cartes_joueur2.append(piocher_une_carte())
    print("Joueur 1: ", afficher_liste_cartes(cartes_joueur1))
    print("Joueur 2: ", afficher_liste_cartes(cartes_joueur2))


# On tire au sort quel joueur commence
def tirer_au_sort_un_joueur():
    return choice(["Joueur1", "Joueur2"])


# ----------------------------------------------------------------------------------------------------------------------
# Le programme commence à être exécuté ici
# ----------------------------------------------------------------------------------------------------------------------
#
# Initialisation des variables
# On crée toutes les cartes du jeu et on les place dans la pile de la pioche
cartes_pioche = creer_toutes_les_cartes()

# Tous les autres tas sont vides au départ
cartes_joueur1 = []
cartes_joueur2 = []
cartes_tapis = []

melanger_la_pioche()

distribuer_les_cartes()

# On lit la première carte de la pioche. C'est elle qui détermine ce qui peut être posé par le premier joueur
piocher_une_carte_et_la_jouer_sur_le_tapis()

joueur_ayant_la_main = tirer_au_sort_un_joueur()
print("{} commence la partie".format(joueur_ayant_la_main))

