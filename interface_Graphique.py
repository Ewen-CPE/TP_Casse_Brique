"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""

# Bibliothèques importés
from tkinter import Tk,Label,Frame,Button,Canvas
from Logique import Logique
from Raquette import Raquette
from Balle import Balle
from Brique import Brique



class Interface_Graphique:
    def __init__(self): # initialisation de ma classe

        # initialisation de ma fenêtre pour l'interface graphique
        self.__window = Tk()
        self.__window_title = self.__window.title("Casse Brique")
        self.__window_geometry = self.__window.geometry("860x520")
        self.__window_config = self.__window.config(background="#000000")

        # initialisation de mon menu d'accueil
        self.__Menu = Frame(self.__window,background="#FFFFFF",relief="raised",width=450,height=350)
        self.__Menu.pack_propagate(False) #fonction pour enlever la propagation de la page par le joueur
        self.__Menu_Label = Label(self.__Menu,text="Menu du Jeu",width=20,height=5).pack(pady=30)
        self.__Menu.pack(pady=100)

        # mise en place de mes boutons dans le menu
        self.__Bouton_Démarrez = Button(self.__Menu,text="Démarrez",fg="green",command = self.lancement_jeu,width=8,height=2).pack(pady=8) # Bouton pour lancer le jeu casse brique
        self.__Bouton_Arreter = Button(self.__Menu,text="Arrêtez",fg="red",command = quit,width=8,height=2).pack(pady=6) # Bouton pour quitter le menu du jeu
        self.__Bouton_Paramètre = Button(self.__Menu,text="Paramètre",fg="navy",width=8,height=2).pack(pady=6) # bouton pour accéder aux paramètres du jeu
        

        #initialisation des différentes données utiles dans la mise en place du jeu
        self.__zone_jeu = None # zone où se déroule le jeu
        self.__raquette = None # raquette du joueur
        self.__balle = None # balle du jeu
        self.__briques = None # ensembles des briques du niveau de jeu
        self.__Menu_fin =None # Menu de fin après la victoire et la défaite du joueur
        self.__score_affichage = None 
        self.__vies_affichage = None
        self.__bandeau = None # bandeau qui contient le score et la vie du joueur

        self.__malogic = Logique() # initialisation de la classe logique

        #récupération des informations types "logique"
        self.__score = self.__malogic.get_score() 
        self.__vies = self.__malogic.get_vies()


        self.__window.mainloop()

    def lancement_jeu(self): # intialisation du jeu après que l'utilisateur a cliqué sur démarrer

        self.__Menu.destroy()
        self.__malogic.initialisation()

        #mise en place du bandeau avec le score et la vie
        self.__bandeau = Frame(self.__window,width=860,height=30,background="black")
        self.__bandeau.pack_propagate(False)
        self.__score_affichage = Label(self.__bandeau,text="Score : "+str(self.__score),fg="white",background="black",font=("Courrier",20))
        self.__score_affichage.pack(side="left", padx=5)
        self.__vies_affichage = Label(self.__bandeau,text="Vies : "+str(self.__vies),fg="white",background="black",font=("Courrier",20))
        self.__vies_affichage.pack(side="right",padx=5)
        self.__bandeau.pack()

        self.maj_info()
        self.zone_de_jeu()


    def zone_de_jeu(self): #initialisation de la zone de jeu
        self.__zone_jeu = Canvas(self.__window,width=850,height=490,background="black")

        self.__raquette = Raquette(self.__zone_jeu)
        self.__raquette.create_raquette() #création de la raquette pour le joueur

        self.__balle = Balle(self.__zone_jeu,self.__malogic.get_niveau())
        self.__balle.create_balle() #création de la balle pour le jeu

        self.__briques = Brique(self.__zone_jeu)
        self.__briques.create_Briques() #création des briques pour le jeu

        self.__zone_jeu.pack()
        self.update()

    def update(self): # routine du jeu qui se répète toutes les 20 ms

        self.__raquette.mouv_raquette() # mouvement de la raquette stocké dans la classe raquette
        self.__balle.mouv_balle() # mouvement de la balle stocké dans la classe balle
        self.collision_raquette()
        self.collision_briques()
        self.perdre_vie()

        self.__zone_jeu.after(20,self.update) # appel de ma fonction self.update après 20ms
        
    def collision_raquette(self): # collision de la raquette avec la balle

        if (self.__balle.get_position_y() + self.__balle.get_diametre()) >= self.__raquette.get_position_y() : # condition si la coordonné "y" du bas de la balle dépasse la coordonnée "y" de la raquette
            if (self.__balle.get_position_x() >= self.__raquette.get_position_x()) and (self.__balle.get_position_x() <= (self.__raquette.get_position_x() + self.__raquette.get_taille_x())) : # condition si la coordonnée "x" gauche de la balle se situe sur la raquette
                self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
            elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__raquette.get_position_x()) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) <= (self.__raquette.get_position_x() + self.__raquette.get_taille_x())) : # condition si la coordonnée "x" droite de la balle se situe sur la raquette
                self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
    
    def collision_briques(self): # collision de la balle sur les briques

        for k in range(self.__briques.get_taille_liste()): # vérification des conditions pour chacune des briques dans la liste de brique

            # collision bas de la brique
            if (self.__balle.get_position_y() <= (self.__briques.get_position_y(k) + self.__briques.get_taille_y())) and (self.__balle.get_position_y() >= (self.__briques.get_position_y(k) + 0.75*self.__briques.get_taille_y())): # condition si la coordonnée "y" du haut de la balle est plus petite que la coordonnée "y" du bas de la brique
                if (self.__balle.get_position_x() >= self.__briques.get_position_x(k)) and (self.__balle.get_position_x() <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordnnée "x" gauche de la balle est supérieur à la coordonnée "x" gauche de la brique et si la coordonnée "x" gauche de la balle est inférieur à la cordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break
                elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__briques.get_position_x(k)) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordnnée "x" droite de la balle est supérieur à la coordonnée "x" gauche de la brique et si la coordonnée "x" droite de la balle est inférieur à la cordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break
            
            #collision du haut de la brique
            if ((self.__balle.get_position_y() + self.__balle.get_diametre()) >= self.__briques.get_position_y(k)) and ((self.__balle.get_position_y() + self.__balle.get_diametre()) <= (self.__briques.get_position_y(k) + 0.25*self.__briques.get_taille_y())): # condition si la coordonnée "y" du bas la balle est plus grande que la coordonnée "y" du haut de la brique
                if (self.__balle.get_position_x() >= self.__briques.get_position_x(k)) and (self.__balle.get_position_x() <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): #condition si la coordonnée "x" gauche de la balle est supérieur à la coordonnée "x" gauche de la brique et la coordonnée "x" gauche de ma balle est inférieur à la coordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break
                elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__briques.get_position_x(k)) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordnnée "x" droite de la balle est supérieur à la coordonnée "x" gauche de la brique et si la coordonnée "x" droite de la balle est inférieur à la cordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break
            
            #collision côtés de la brique
            if(self.__balle.get_position_y() <= (self.__briques.get_position_y(k) + self.__briques.get_taille_y())) and (self.__balle.get_position_y() >= self.__briques.get_position_y(k)): # condition si la coordonné "y" du haut de la balle est supérieur à la coordonnée "y" du bas de la brique et si la coordonnée "y" du haut de la balle est inférieur à la coordonnée "y" du haut de la brique
                if (self.__balle.get_position_x() <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordonnée "x" gauche de la balle est inférieur à la coordonnée " x" droite de la brique
                    self.__balle.add_vitesse_x(-self.__balle.get_vitesse_x()) # inversement de la vitesse "x" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break
                elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__briques.get_position_x(k)) and (self.__balle.get_position_x() <= self.__briques.get_position_x(k)):  # condition si la coordonnée "x" droite de la balle est supérieur à la coordonnée " x" gauche de la brique
                    self.__balle.add_vitesse_x(-self.__balle.get_vitesse_x()) # inversement de la vitesse "x" de la balle
                    self.__briques.destruct_brique(k) #destruction de la brique indice k dans la liste
                    self.__malogic.add_score() # modification du score
                    self.maj_info() # modification des informations affichés
                    break

    def perdre_vie(self): # fonction qui enlève une vie si la balle passe en dessous de deux fois la taille "y" de la raquette

        if (self.__balle.get_position_y() + self.__balle.get_diametre()) >= (self.__raquette.get_position_y() + 2*self.__raquette.get_taille_y()): # condition si la coordonnée "y" bas de la balle passe dessous de deux fois la taille "y" de la raquette
            self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
            self.__malogic.add_vies() # retirement d'un point de vie au joueur
            self.maj_info() # modification des informations affichés
    
    def maj_info(self): # fonction qui mets à jour les informations affichées à l'écran
        # récupération du score et de la vie du joueur
        self.__score = self.__malogic.get_score()
        self.__vies = self.__malogic.get_vies()

        #effacement des de l'affichage actuel
        self.__score_affichage.pack_forget()
        self.__vies_affichage.pack_forget()

        #affichage du nouveau score et de la vie du joueur
        self.__score_affichage = Label(self.__bandeau,text="Score : " + str(self.__score),fg="white",background="black",font=("Courrier",20))
        self.__vies_affichage = Label(self.__bandeau,text="Vies : "+str(self.__vies),fg="white",background="black",font=("Courrier",20))
        self.__score_affichage.pack(side="left", padx=5)
        self.__vies_affichage.pack(side="right",padx=5)

        self.reset()
    
    def reset(self): # fonction qui vérifie si le joueur à gagné ou perdu
        if self.__vies == 0 : # condition si la vie du joueur est à 0 (perdu)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les perdants
            self.__Menu_fin = Frame(self.__window,background="#FFFFFF",relief="raised",width=450,height=350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin,text="Défaite",width=20,height=5).pack(pady=30)
            # bouton pour rejouer au jeu ou arrétez
            Button(self.__Menu_fin,text="Rejouer",fg="green",command = self.rejouer,width=8,height=2).pack(pady=6)
            Button(self.__Menu_fin,text="Arrêtez",fg="red",command = quit,width=8,height=2).pack(pady=6)

            self.__malogic.meilleur_score(self.__score) # renvoie du score du joueur pour l'afficher ou pas dans les meilleurs scores

            self.__Menu_fin.pack(pady=100)

        elif self.__score == 350 : # condition si le joueur casse toutes les briques (gagner)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les gagnants
            self.__Menu_fin = Frame(self.__window,background="#FFFFFF",relief="raised",width=450,height=350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin,text="Victoire",width=20,height=5).pack(pady=30)
            Button(self.__Menu_fin,text="Continuez",fg="green",command = self.continuer,width=8,height=2).pack(pady=6)
            Button(self.__Menu_fin,text="Arrêtez",fg="red",command = quit,width=8,height=2).pack(pady=6)

            self.__malogic.meilleur_score(self.__score) # renvoie du score du joueur pour l'afficher ou pas dans les meilleurs scores

            self.__Menu_fin.pack(pady=100)

    
    def rejouer(self): # fonction si le joueur décide rejouer au jeu

        self.__Menu_fin.destroy()
        self.__malogic.__init__() # remise à zéro du score, de la vie et des niveaux
        self.lancement_jeu()

    def continuer(self): # fonction si le joueur décide de continuer de jouer après sa vitoire au niveau auquel il était

        self.__Menu_fin.destroy()
        self.__malogic.remove_niveau() # changement de niveau pour monter en difficulté
        self.lancement_jeu()
    



