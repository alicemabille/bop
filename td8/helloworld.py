# -*- coding: utf-8 -*-

from tkinter import *

# Création de la fenêtre graphique
fenetre = Tk()
fenetre.title("Hello")
fenetre.geometry('640x480')
fenetre.resizable(width=True,height=True)

# Création des widgets
label = Label(fenetre, text="Hello World !")
bouton = Button(fenetre, text="Quitter", command=fenetre.destroy)
champ = Entry(fenetre)

# Positionnement des widgets dans la fenêtre graphique avec la méthode pack()
label.pack()
bouton.pack()
champ.pack()

# Lancement du gestionnaire d’évènements
#fenetre.mainloop()
