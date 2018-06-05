#from PIL import Image, ImageTk
#from tkinter import *

from random import choice, shuffle, randrange


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
    # On place la carte sur le dessus du tapis
    cartes_tapis.insert(0, carte)
    # Pour définir la couleur actuelle, on lit le paramètre "couleur" de cette carte
    # Ici il faut utiliser le mot-clef "global" car on change la valeur de ce paramètre défini ailleurs
    definir_couleur_actuelle(carte["couleur"])


def definir_couleur_actuelle(couleur):
    global couleur_actuelle
    couleur_actuelle = couleur


# Distribution de 7 cartes à chaque joueur
def distribuer_les_cartes():
    global cartes_joueur1, cartes_joueur2
    for i in range(7):
        cartes_joueur1.append(piocher_une_carte())
        cartes_joueur2.append(piocher_une_carte())
    print("Joueur 1: ", afficher_liste_cartes(cartes_joueur1))
    print("Joueur 2: ", afficher_liste_cartes(cartes_joueur2))


# On tire au sort quel joueur commence
def tirer_au_sort_un_joueur():
    return choice(["Joueur1", "Joueur2"])


def changer_de_joueur():
    global joueur_ayant_la_main
    if joueur_ayant_la_main == "Joueur1":
        joueur_ayant_la_main = "Joueur2"
    else:
        joueur_ayant_la_main = "Joueur1"
    print(joueur_ayant_la_main, "prend la main")


def appliquer_cartes_speciales():
    # On regarde quelle est la carte sur le dessus du tapis
    carte_actuelle = cartes_tapis[0]
    if carte_actuelle["symbole"] == "+2":
        piocher_N_cartes_pour_joueur_ayant_la_main(2)
    elif carte_actuelle["symbole"] == "+4":
        piocher_N_cartes_pour_joueur_ayant_la_main(4)
    elif carte_actuelle["symbole"] == "changement de sens" or carte_actuelle["symbole"] == "passe":
        changer_de_joueur()


def carte_est_valide(carte):
    premiere_carte = cartes_tapis[0]
    if carte["couleur"] == "speciale":
        return True
    elif carte["couleur"] == premiere_carte["couleur"]:
        return True
    elif carte["symbole"] == premiere_carte["symbole"]:
        return True
    else:
        return False


def faire_jouer_joueur2():
    global couleur_actuelle
    cartes_valides = []
    for carte in cartes_joueur2:
        if carte_est_valide(carte):
            cartes_valides.append(carte)
    if len(cartes_valides) == 0:
        print("Joueur2 n'a aucune carte valide et doit piocher")
        piocher_N_cartes_pour_joueur_ayant_la_main(1)
        changer_de_joueur()
        return
    else:
        # On choisit aléatoirement une carte parmis les cartes valides:
        index = randrange(len(cartes_valides))
        carte_choisie = cartes_valides.pop(index)
        print("{} joue la carte {} (carte {}) sur le tapis".format(joueur_ayant_la_main, carte_choisie["symbole"], carte_choisie["couleur"]))
        poser_une_carte_sur_le_tapis(carte_choisie)
        if len(cartes_joueur2) == 0:
            print("Joueur2 a gagné!!")
            return
        else:
            appliquer_cartes_speciales()
            if carte_choisie["symbole"] == "changement de couleur" or carte_choisie["symbole"] == "+4":
                nouvelle_couleur = choice(['bleu', 'rouge', 'jaune', 'vert'])
                print("Couleur actuelle:", nouvelle_couleur)
                definir_couleur_actuelle (nouvelle_couleur)
            changer_de_joueur()
            return 


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

joueur_ayant_la_main = tirer_au_sort_un_joueur()
print("{} commence la partie\n".format(joueur_ayant_la_main))

# On lit la première carte de la pioche. C'est elle qui détermine ce qui peut être posé par le premier joueur
carte = piocher_une_carte()
print("Carte de départ: {} (carte {})\n".format(carte["symbole"], carte["couleur"]))
poser_une_carte_sur_le_tapis(carte)

appliquer_cartes_speciales()

if joueur_ayant_la_main == "Joueur2":
    faire_jouer_joueur2()