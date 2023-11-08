import tkinter as tk

# Crée une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Échiquier avec Reines")

# Fonction pour dessiner un échiquier avec des reines sur les cases noires
def dessiner_echiquier():
    taille_case = 50  # Taille d'une case en pixels

    for ligne in range(8):
        for colonne in range(8):
            # Alterner la couleur des cases
            couleur_case = "white" if (ligne + colonne) % 2 == 0 else "black"
            
            # Dessiner la case
            canevas.create_rectangle(colonne * taille_case, ligne * taille_case,
                                     (colonne + 1) * taille_case, (ligne + 1) * taille_case,
                                     fill=couleur_case)

            # Ajouter une reine sur les cases noires
            if couleur_case == "black":
                reine_image = tk.PhotoImage(file="reine.png")  # Assurez-vous d'avoir une image de reine
                canevas.create_image(colonne * taille_case, ligne * taille_case, anchor=tk.NW, image=reine_image)

# Crée un canevas pour dessiner l'échiquier
canevas = tk.Canvas(fenetre, width=400, height=400)
canevas.pack()

# Dessine l'échiquier avec des reines
dessiner_echiquier()

# Lancement de la boucle principale
fenetre.resizable(False,False)
fenetre.mainloop()