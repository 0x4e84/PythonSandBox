#from PIL import Image, ImageTk
#from tkinter import *

from random import choice, shuffle, randrange


# Affichage d'une carte sous forme de texte
def afficher_carte_comme_texte(carte):
    if carte["couleur"] == "spéciale":
        return "\"{}\"".format(carte["symbole"])
    else:
        return "\"{}\" ({})".format(carte["symbole"], carte["couleur"])


# Affichage de la liste des cartes dans une pile
def afficher_liste_cartes(pile):
    liste = "{} cartes: \n".format(len(pile))
    index = 1
    for carte in pile:
        liste += str(index) + ": " + afficher_carte_comme_texte(carte) + "\n"
        index += 1
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
    print("Les cartes sont mélangées\n")
    shuffle(cartes_pioche)


# On retire la première carte de la pioche
def piocher_une_carte():
    return cartes_pioche.pop(0)


def piocher_N_cartes_pour_joueur_ayant_la_main(N):
    print(joueur_ayant_la_main, "pioche", N, "carte(s)!")
    for i in range (N):
        carte = piocher_une_carte()
        if joueur_ayant_la_main == "Joueur1":
            cartes_joueur1.append(carte)
        else:
            cartes_joueur2.append(carte)


# On retire la première carte de la pioche
def poser_une_carte_sur_le_tapis(carte):
    global carte_tapis
    # S'il y a déjà une carte sur le tapis, on la met dans la pioche
    if carte_tapis != {}:
        cartes_pioche.append(carte_tapis)
    # On place la carte sur le tapis
    carte_tapis = carte
    # Pour définir la couleur actuelle, on lit le paramètre "couleur" de cette carte
    nouvelle_couleur = carte["couleur"]
    definir_couleur_actuelle(nouvelle_couleur)


def definir_couleur_actuelle(nouvelle_couleur):
    # Ici il faut utiliser le mot-clef "global" car on change la valeur de ce paramètre défini ailleurs
    global couleur_actuelle
    if nouvelle_couleur == "spéciale":
        if joueur_ayant_la_main == "Joueur1":
            while nouvelle_couleur not in ['bleu', 'rouge', 'jaune', 'vert']:
                nouvelle_couleur = input("Joueur1, choisissez une nouvelle couleur parmi 'bleu', 'rouge', 'jaune', 'vert'")
        else:
            nouvelle_couleur = choice(['bleu', 'rouge', 'jaune', 'vert'])
    print("Nouvelle couleur actuelle:", nouvelle_couleur)
    couleur_actuelle = nouvelle_couleur


# Distribution de 7 cartes à chaque joueur
def distribuer_les_cartes():
    global cartes_joueur1, cartes_joueur2
    for i in range(7):
        cartes_joueur1.append(piocher_une_carte())
        cartes_joueur2.append(piocher_une_carte())
    print("Joueur 1:", afficher_liste_cartes(cartes_joueur1))
    print("Joueur 2:", afficher_liste_cartes(cartes_joueur2))


# On tire au sort quel joueur commence
def tirer_au_sort_un_joueur():
    return choice(["Joueur1", "Joueur2"])


def changer_de_joueur():
    global joueur_ayant_la_main, cartes_joueur1, cartes_joueur2
    if joueur_ayant_la_main == "Joueur1":
        joueur_ayant_la_main = "Joueur2"
        nombre_cartes = len(cartes_joueur2)
    else:
        joueur_ayant_la_main = "Joueur1"
        nombre_cartes = len(cartes_joueur1)
    print(joueur_ayant_la_main, "a", nombre_cartes, "cartes et prend la main\n")


def appliquer_cartes_speciales():
    # On regarde quelle est la carte sur le dessus du tapis
    if carte_tapis["symbole"] == "+2":
        piocher_N_cartes_pour_joueur_ayant_la_main(2)
    elif carte_tapis["symbole"] == "+4":
        piocher_N_cartes_pour_joueur_ayant_la_main(4)
    elif carte_tapis["symbole"] == "changement de sens" or carte_tapis["symbole"] == "passe":
        changer_de_joueur()


def carte_est_valide(carte):
    global couleur_actuelle
    if carte["couleur"] == "spéciale":
        return True
    elif carte["couleur"] == couleur_actuelle:
        return True
    elif carte["symbole"] == carte_tapis["symbole"]:
        return True
    else:
        return False


def faire_jouer_joueur1():
    global couleur_actuelle, cartes_joueur1, partie_en_cours
    print("Joueur1 dispose des cartes suivantes:", afficher_liste_cartes(cartes_joueur1))
    en_attente = True
    while en_attente:
        print("Sur le tapis:" + afficher_carte_comme_texte(carte_tapis), ", couleur actuelle: ", couleur_actuelle)
        choix = int(input("=> Joueur1: choisissez le numéro de la carte à jouer ou \"0\" pour piocher: "))
        if 0 < choix <= len(cartes_joueur1):
            carte_choisie = cartes_joueur1[choix - 1]
            if carte_est_valide(carte_choisie):
                carte_jouee = cartes_joueur1.pop(choix - 1)
                print("Joueur1 joue la carte", afficher_carte_comme_texte(carte_choisie), "\n")
                poser_une_carte_sur_le_tapis(carte_jouee)
                if len(cartes_joueur1) == 0:
                    print("Joueur1 a gagné!!")
                    partie_en_cours = False
                    return

                changer_de_joueur()
                appliquer_cartes_speciales()
                en_attente = False
            else:
                print("Carte invalide, réessayez.")
        elif choix == 0:
            print("Joueur1 décide de piocher")
            piocher_N_cartes_pour_joueur_ayant_la_main(1)
            changer_de_joueur()
            en_attente = False


def faire_jouer_joueur2():
    global couleur_actuelle, partie_en_cours
    cartes_valides = []
    # On doit parcourir la liste de la fin vers le début, pour ne pas décaler des éléments qu'on n'a pas encore accédés
    for index in reversed(range(len(cartes_joueur2))):
        carte = cartes_joueur2[index]
        if carte_est_valide(carte):
            carte_valide = cartes_joueur2.pop(index)
            cartes_valides.append(carte_valide)
    if len(cartes_valides) == 0:
        print("Joueur2 n'a aucune carte valide et doit piocher")
        piocher_N_cartes_pour_joueur_ayant_la_main(1)
        changer_de_joueur()
    else:
        # On choisit aléatoirement une carte parmis les cartes valides:
        index = randrange(len(cartes_valides))
        carte_choisie = cartes_valides.pop(index)
        # On remet les autres cartes dans le jeu du joueur2:
        for index in range(len(cartes_valides)):
            carte = cartes_valides.pop(0)
            cartes_joueur2.append(carte)
        print("Joueur2 joue la carte", afficher_carte_comme_texte(carte_choisie) + "\n")
        poser_une_carte_sur_le_tapis(carte_choisie)
        if len(cartes_joueur2) == 0:
            print("Joueur2 a gagné!!")
            partie_en_cours = False
            return

        changer_de_joueur()
        appliquer_cartes_speciales()
        if carte_choisie["symbole"] == "changement de couleur" or carte_choisie["symbole"] == "+4":
            nouvelle_couleur = choice(['bleu', 'rouge', 'jaune', 'vert'])
            print("Couleur actuelle:", nouvelle_couleur)
            definir_couleur_actuelle (nouvelle_couleur)


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
carte_tapis = {}
partie_en_cours = True
couleur_actuelle = "indéfinie"

print("Début du jeu\n")
melanger_la_pioche()

distribuer_les_cartes()

joueur_ayant_la_main = tirer_au_sort_un_joueur()
print("{} commence la partie\n".format(joueur_ayant_la_main))

# On lit la première carte de la pioche. C'est elle qui détermine ce qui peut être posé par le premier joueur
carte = piocher_une_carte()
print("Carte de départ:", afficher_carte_comme_texte(carte) + "\n")
poser_une_carte_sur_le_tapis(carte)

appliquer_cartes_speciales()

while partie_en_cours:
    if joueur_ayant_la_main == "Joueur1":
        faire_jouer_joueur1()
    else:
        faire_jouer_joueur2()