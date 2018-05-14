from tkinter import*

from random import shuffle

rangs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]

global label_resultat
global player1
global player2


def creer_tas(couleur):
    return [(couleur, points+1, rangs[points]) for points in range(13)]


def distribuer_trefle_au_joueur_1():
    global player1
    global player2
    player1 = creer_tas("trèfle")
    player2 = creer_tas("pique")
    commencer_le_jeu()


def distribuer_pique_au_joueur_1():
    global player1
    global player2
    player1 = creer_tas("pique")
    player2 = creer_tas("trèfle")
    commencer_le_jeu()


def poser_une_carte():
    # On récupère la première carte de chaque joueur
    carte_1 = player1.pop(0)
    carte_2 = player2.pop(0)

    # Et on la pose sur le tapis, en dernière position
    tapis_joueur_1.append(carte_1)
    tapis_joueur_2.append(carte_2)


def donner_le_tapis_au_joueur_1():
    for carte in tapis_joueur_1:
        player1.append(carte)
    for carte in tapis_joueur_2:
        player1.append(carte)
    tapis_joueur_1.clear()
    tapis_joueur_2.clear()


def donner_le_tapis_au_joueur_2():
    for carte in tapis_joueur_1:
        player2.append(carte)
    for carte in tapis_joueur_2:
        player2.append(carte)
    tapis_joueur_1.clear()
    tapis_joueur_2.clear()


def demarrer_jeu():
    # On présente au joueur 1 le choix de la couleur
    label = Label(frame_choix_couleur, text="Joueur 1 choisit sa couleur: ")
    label.pack(side=LEFT, padx=3)

    # Suivant le bouton pressé, on distribue d'une façon ou d'une autre
    bouton_trefle = Button(frame_choix_couleur, text="Trèfle", command=distribuer_trefle_au_joueur_1)
    bouton_trefle.pack(side=LEFT, padx=3, pady=3)

    bouton_pique = Button(frame_choix_couleur, text="Pique", command=distribuer_pique_au_joueur_1)
    bouton_pique.pack(side=RIGHT, padx=3, pady=3)

    frame_choix_couleur.pack(side=TOP)


def commencer_le_jeu():
    # On efface le choix de couleur du joueur 1
    frame_choix_couleur.destroy()

    global label_resultat

    bouton_continuer = Button(frame_resultat, text="Continuer", command=continuer_jeu)
    bouton_continuer.pack(side=LEFT, padx=3, pady=3)
    label_resultat = Label(frame_resultat, text="")
    label_resultat.pack(padx=3, pady=3, expand=True)
    frame_resultat.pack(fill=X)

    # On mélange les deux jeux
    shuffle(player1)
    shuffle(player2)

    poser_une_carte()
    afficher_cartes()


def charger_image(carte):
    couleur, points, rang = carte
    nom_image = "Images/" + couleur + "_" + rang + ".png"
    return PhotoImage(file=nom_image)


def afficher_cartes():
    global player1
    global player2

    canvas.delete("all")

    #print("Joueur1: ", player1)
    print("Tapis Joueur1: ", tapis_joueur_1, " - Tapis Joueur2: ", tapis_joueur_2)

    # On affiche le nombre de cartes de chaque joueur
    canvas.create_text(20, 60,
                       font=("Arial", 14),
                       justify=LEFT,
                       text="Joueur 1: {} cartes".format(len(player1)+len(tapis_joueur_1)),
                       anchor="w")
    canvas.create_text(580, 60,
                       font=("Arial", 14),
                       justify=RIGHT,
                       text="Joueur 2: {} cartes".format(len(player2)+len(tapis_joueur_2)),
                       anchor="e")

    if len(player1) == 0:
        label_resultat.config(text="Joueur 2 a gagné!")
        return
    elif len(player2) == 0:
        label_resultat.config(text="Joueur 1 a gagné!")
        return

    # On affiche les cartes du joueur 1
    image_dos = PhotoImage(file="Images/dos.png")
    for i in range(len(player1), 0, -1):
        canvas.create_image(22+i, 207+2*i, image=image_dos, anchor="w")
    for i in range(len(tapis_joueur_1)):
        if i < len(tapis_joueur_1)-1:
            canvas.create_image(20-5*i, 200-5*i, image=image_dos, anchor="w")
        else:
            # On charge l'images
            image_carte_1 = charger_image(tapis_joueur_1[i])
            # On affiche l'image
            canvas.create_image(20-5*i, 195-5*i, image=image_carte_1, anchor="w")

    # On affiche les cartes du joueur 2
    for i in range(len(player2), 0, -1):
        canvas.create_image(578-i, 207+2*i, image=image_dos, anchor="e")
    for i in range(len(tapis_joueur_2)):
        if i < len(tapis_joueur_2)-1:
            canvas.create_image(580+5*i, 200-5*i, image=image_dos, anchor="e")
        else:
            # On charge l'images
            image_carte_2 = charger_image(tapis_joueur_2[i])
            # On affiche l'image
            canvas.create_image(580+5*i, 195-5*i, image=image_carte_2, anchor="e")

    # On récupère le nombre de points de la dernière carte de chaque tapis
    carte_1 = tapis_joueur_1[-1]
    points_1 = carte_1[1]
    carte_2 = tapis_joueur_2[-1]
    points_2 = carte_2[1]

    if points_1 > points_2:
        label_resultat.config(text="Joueur 1 remporte le tour")
        donner_le_tapis_au_joueur_1()
        poser_une_carte()
    elif points_1 < points_2:
        label_resultat.config(text="Joueur 2 remporte le tour")
        donner_le_tapis_au_joueur_2()
        poser_une_carte()
    else:
        label_resultat.config(text="Bataille!")
        poser_une_carte()
        poser_une_carte()

    tk.mainloop()

def continuer_jeu():
    afficher_cartes()


tk = Tk()
canvas = Canvas(tk, width=600, height=400, bg="ivory")
canvas.pack(side=TOP, padx=5, pady=5)
frame_choix_couleur = Frame(tk)
frame_resultat = Frame(tk)
tapis_joueur_1 = []
tapis_joueur_2 = []

demarrer_jeu()

tk.mainloop()
