"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
"""

# Bibliothèques importés
from tkinter import Tk,Label,Frame,Button,Canvas,PhotoImage
from Logique import Logique
from Raquette import Raquette
from Balle import Balle
from Brique import Brique



class Interface_Graphique:
    def __init__(self):
        '''intialisation de la classe'''

        # initialisation de la fenêtre pour l'interface graphique
        self.__window = Tk()
        self.__window_title = self.__window.title("Casse Brique")
        self.__window_geometry = self.__window.geometry("860x520")
        self.__window_config = self.__window.config(background = "#000000")

        # initialisation du menu d'accueil
        self.__Menu = Frame(self.__window, background = "#FFFFFF", relief = "raised", width = 450, height = 350)
        self.__Menu.pack_propagate(False) #fonction pour désactiver la redimension automatique du Frame
        self.__Menu_Label = Label(self.__Menu, text = "Menu du Jeu", background = "#FFFFFF", font = ("Californian FB",20)).pack(pady = 30)


        # mise en place des boutons dans le menu
        self.__Bouton_Démarrez = Button(self.__Menu, text = "Démarrez", fg = "green", command = self.lancement_jeu, font = ("Arial",10), width = 15, height = 2).pack(pady = 4) # Bouton pour lancer le jeu casse brique
        self.__Bouton_Arreter = Button(self.__Menu, text = "Arrêtez", fg = "red", command = quit, font = ("Arial",10), width = 15, height = 2).pack(pady = 6) # Bouton pour quitter le menu du jeu
        self.__Bouton_Paramètre = Button(self.__Menu, text = "Paramètre", fg = "navy", command = self.parametre, font = ("Arial",10), width = 15, height = 2).pack(pady = 6) # bouton pour accéder aux paramètres du jeu

        self.__malogic = Logique() # initialisation de la classe qui initialise les données du jeu

        self.__Meilleur_score_Label = Label(self.__Menu, text = "Meilleur score : " + str(self.__malogic.get_meilleur_score()), fg = "#FF2301" , background = "#FFFFFF", font = ("Californian FB",16)).pack(pady = 5) # affichage du meilleur score

        self.__Menu.pack(pady = 100) # Ajoute un espacement vertical de 100 pixels lors de l'affichage du menu
        

        #initialisation des différentes données utiles dans la mise en place du jeu
        self.__zone_jeu = None # zone où se déroule le jeu
        self.__raquette = None # raquette du joueur
        self.__balle = None # balle du jeu
        self.__briques = None # ensembles des briques du niveau de jeu
        self.__Menu_fin =None # Menu de fin après la victoire et la défaite du joueur
        self.__score_affichage = None 
        self.__vies_affichage = None
        self.__bandeau = None # bandeau qui contient le score et la vie du joueur
        self.__Menu_parametre = None # Menu des paramètres du jeu
        self.__couleur_balle = None # couleur de la balle


        #récupération des informations types "logique"
        self.__score = self.__malogic.get_score() #score du joueur
        self.__vies = self.__malogic.get_vies() # vies du joueur

        # Arrière plan des différents niveaux
        self.__background_plaine = PhotoImage(file = "background_plaine.png")
        self.__background_glace = PhotoImage(file = "background_glace.png")
        self.__background_enfer = PhotoImage(file = "background_enfer.png")

        self.__window.mainloop()
    
    def parametre(self):

        self.__Menu.destroy()

        # initialisation du menu paramètre
        self.__Menu_parametre = Frame(self.__window, background = "#FFFFFF", relief = "raised", width = 450, height = 350)
        self.__Menu_parametre.pack_propagate(False) #fonction pour désactiver la redimension automatique du Frame
        Label(self.__Menu_parametre, text = "Paramètre", width = 20, height = 3).pack(pady = 25)
        self.__Menu_parametre.pack(pady = 100) # Ajoute un espacement vertical de 100 pixels pour le menu paramètre

        # Boutons des différentes couleurs disponibles pour la balle
        Button(self.__Menu_parametre, text = "Balle rouge", fg = "red", command = self.couleur_rouge, width = 8, height = 2).pack(pady = 2)
        Button(self.__Menu_parametre, text = "Balle rose", fg = "pink", command = self.couleur_rose, width = 8, height = 2).pack(pady = 2)
        Button(self.__Menu_parametre, text = "Balle orange", fg = "orange", command = self.couleur_orange, width = 8, height = 2).pack(pady = 2)
        Button(self.__Menu_parametre, text = "Balle vert", fg = "green", command = self.couleur_vert, width = 8, height = 2).pack(pady = 2)


    # Fonction qui permette de changer la couleur de la balle
    def couleur_rouge(self):
        self.__couleur_balle = "red"
        self.__Menu_parametre.destroy()
        self.lancement_jeu()

    def couleur_rose(self):
        self.__couleur_balle = "pink"
        self.__Menu_parametre.destroy()
        self.lancement_jeu()

    def couleur_orange(self):
        self.__couleur_balle = "orange"
        self.__Menu_parametre.destroy()
        self.lancement_jeu()

    def couleur_vert(self):
        self.__couleur_balle = "green"
        self.__Menu_parametre.destroy()
        self.lancement_jeu()




    def lancement_jeu(self): 
        '''intialisation du jeu après que l'utilisateur ait cliqué sur démarrer'''

        self.__Menu.destroy()
        self.__malogic.initialisation()

        #mise en place du bandeau avec le score et la vie
        self.__bandeau = Frame(self.__window, width = 860, height = 30, background = "black")
        self.__bandeau.pack_propagate(False) #fonction pour désactiver la redimension automatique du Frame
        self.__score_affichage = Label(self.__bandeau, text = "Score : " + str(self.__score), fg = "white", background = "black", font = ("Courrier",20))
        self.__score_affichage.pack(side = "left", padx = 5)
        self.__vies_affichage = Label(self.__bandeau, text = "Vies : " + str(self.__vies), fg = "white", background = "black", font = ("Courrier",20))
        self.__vies_affichage.pack(side = "right", padx = 5)
        self.__bandeau.pack()

        self.maj_info()
        self.zone_de_jeu()


    def zone_de_jeu(self): 
        '''initialisation de la zone de jeu'''
        self.__zone_jeu = Canvas(self.__window, width = 850, height = 490) # Création du canevas de la zone de jeu

        if self.__malogic.get_taille_liste_niveau() == 3:
            self.__zone_jeu.create_image(0, 0, image = self.__background_plaine, anchor="nw") # affichage de l'arrière plan Niveau 1

        elif self.__malogic.get_taille_liste_niveau() == 2:
            self.__zone_jeu.create_image(0, 0, image = self.__background_glace, anchor="nw") # affichage de l'arrière plan Niveau 2

        elif self.__malogic.get_taille_liste_niveau() == 1:
            self.__zone_jeu.create_image(0, 0, image = self.__background_enfer, anchor="nw") # affichage de l'arrière plan Niveau 3

        self.__raquette = Raquette(self.__zone_jeu)
        self.__raquette.create_raquette() #création de la raquette pour le joueur

        if self.__couleur_balle == None :
            self.__couleur_balle = "white" # couleur par défault de la balle si aucne couleur n'a été choisi dans les paramètres

        self.__balle = Balle(self.__zone_jeu, self.__malogic.get_niveau(), self.__couleur_balle)
        self.__balle.create_balle() #création de la balle pour le jeu

        self.__briques = Brique(self.__zone_jeu)
        self.__briques.create_Briques() #création des briques pour le jeu

        self.__zone_jeu.pack()
        self.update()

    def update(self): 
        '''fonction : routine du jeu qui se répète toutes les 20 ms'''

        self.__raquette.mouv_raquette() # mouvement de la raquette stocké dans la classe raquette
        self.__balle.mouv_balle() # mouvement de la balle stocké dans la classe balle
        self.collision_raquette()
        self.collision_briques()
        self.perdre_vie()

        self.__zone_jeu.after(20,self.update) # appel de ma fonction self.update après 20ms
        
    def collision_raquette(self):
        '''collision de la raquette avec la balle'''

        if (self.__balle.get_position_y() + self.__balle.get_diametre()) >= self.__raquette.get_position_y() : # condition si la coordonné "y" du bas de la balle dépasse la coordonnée "y" de la raquette
            if (self.__balle.get_position_x() >= self.__raquette.get_position_x()) and (self.__balle.get_position_x() <= (self.__raquette.get_position_x() + self.__raquette.get_taille_x())) : # condition si la coordonnée "x" gauche de la balle se situe sur la raquette
                self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) # inversement de la vitesse "y" de la balle
            elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__raquette.get_position_x()) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) <= (self.__raquette.get_position_x() + self.__raquette.get_taille_x())) : # condition si la coordonnée "x" droite de la balle se situe sur la raquette
                self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) 
    
    def collision_briques(self): 
        '''collision de la balle sur les briques'''

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
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y()) 
                    self.__briques.destruct_brique(k) 
                    self.__malogic.add_score() 
                    self.maj_info()
                    break
            
            #collision du haut de la brique
            if ((self.__balle.get_position_y() + self.__balle.get_diametre()) >= self.__briques.get_position_y(k)) and ((self.__balle.get_position_y() + self.__balle.get_diametre()) <= (self.__briques.get_position_y(k) + 0.25*self.__briques.get_taille_y())): # condition si la coordonnée "y" du bas la balle est plus grande que la coordonnée "y" du haut de la brique
                if (self.__balle.get_position_x() >= self.__briques.get_position_x(k)) and (self.__balle.get_position_x() <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): #condition si la coordonnée "x" gauche de la balle est supérieur à la coordonnée "x" gauche de la brique et la coordonnée "x" gauche de ma balle est inférieur à la coordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y())
                    self.__briques.destruct_brique(k) 
                    self.__malogic.add_score() 
                    self.maj_info() 
                    break
                elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__briques.get_position_x(k)) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordnnée "x" droite de la balle est supérieur à la coordonnée "x" gauche de la brique et si la coordonnée "x" droite de la balle est inférieur à la cordonnée "x" droite de la brique
                    self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y())
                    self.__briques.destruct_brique(k) 
                    self.__malogic.add_score() 
                    self.maj_info()
                    break
            
            #collision côtés de la brique
            if(self.__balle.get_position_y() <= (self.__briques.get_position_y(k) + self.__briques.get_taille_y())) and (self.__balle.get_position_y() >= self.__briques.get_position_y(k)): # condition si la coordonné "y" du haut de la balle est supérieur à la coordonnée "y" du bas de la brique et si la coordonnée "y" du haut de la balle est inférieur à la coordonnée "y" du haut de la brique
                if (self.__balle.get_position_x() <= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())) and ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= (self.__briques.get_position_x(k) + self.__briques.get_taille_x())): # condition si la coordonnée "x" gauche de la balle est inférieur à la coordonnée " x" droite de la brique
                    self.__balle.add_vitesse_x(-self.__balle.get_vitesse_x()) # inversement de la vitesse "x" de la balle
                    self.__briques.destruct_brique(k) 
                    self.__malogic.add_score() 
                    self.maj_info() 
                    break
                elif ((self.__balle.get_position_x() + self.__balle.get_diametre()) >= self.__briques.get_position_x(k)) and (self.__balle.get_position_x() <= self.__briques.get_position_x(k)):  # condition si la coordonnée "x" droite de la balle est supérieur à la coordonnée " x" gauche de la brique
                    self.__balle.add_vitesse_x(-self.__balle.get_vitesse_x()) 
                    self.__briques.destruct_brique(k) 
                    self.__malogic.add_score() 
                    self.maj_info() 
                    break

    def perdre_vie(self):
        '''fonction qui enlève une vie si la balle passe en dessous de deux fois la taille "y" de la raquette'''

        if (self.__balle.get_position_y() + self.__balle.get_diametre()) >= (self.__raquette.get_position_y() + 2*self.__raquette.get_taille_y()): # condition si la coordonnée "y" bas de la balle passe dessous de deux fois la taille "y" de la raquette
            self.__balle.add_vitesse_y(-self.__balle.get_vitesse_y())
            self.__malogic.add_vies() # retirement d'un point de vie au joueur
            self.maj_info() # modification des informations affichés
    
    def maj_info(self): 
        '''fonction qui mets à jour les informations affichées à l'écran'''

        # récupération du score et de la vie du joueur
        self.__score = self.__malogic.get_score()
        self.__vies = self.__malogic.get_vies()

        #effacement de l'affichage actuel
        self.__score_affichage.pack_forget()
        self.__vies_affichage.pack_forget()

        #affichage du nouveau score et de la vie du joueur
        self.__score_affichage = Label(self.__bandeau, text = "Score : " + str(self.__score), fg = "white", background = "black", font = ("Courrier",20))
        self.__vies_affichage = Label(self.__bandeau, text = "Vies : " + str(self.__vies), fg = "white", background = "black", font = ("Courrier",20))
        self.__score_affichage.pack(side = "left", padx = 5)
        self.__vies_affichage.pack(side = "right", padx =5)

        self.reset()
    
    def reset(self):
        '''fonction qui vérifie si le joueur à gagné ou perdu'''

        if self.__vies == 0 : # condition si la vie du joueur est à 0 (perdu)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les perdants
            self.__Menu_fin = Frame(self.__window, background = "#FFFFFF", relief = "raised", width = 450, height = 350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin, text = "Défaite", background = "#FFFFFF", font = ("Californian FB",25)).pack(pady = 30)

            self.__malogic.meilleur_score(self.__score) # renvoie du score du joueur pour l'afficher ou pas dans les meilleurs scores

            # boutons pour rejouer au jeu ou arréter
            Button(self.__Menu_fin, text = "Rejouer", fg = "green", command = self.rejouer, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)
            Button(self.__Menu_fin, text = "Arrêtez", fg = "red", command = quit, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)


            self.__Menu_fin.pack(pady = 100)

        elif self.__score == 350 and self.__malogic.get_taille_liste_niveau() == 3 : # condition si le joueur casse toutes les briques (gagner)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les gagnants
            self.__Menu_fin = Frame(self.__window,background = "#FFFFFF", relief = "raised", width = 450, height = 350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin, text = "Victoire", background = "#FFFFFF", font = ("Californian FB",25)).pack(pady = 30)

            # boutons pour continuer le jeu ou arrêter
            Button(self.__Menu_fin, text = "Continuez", fg = "green", command = self.continuer, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)
            Button(self.__Menu_fin, text = "Arrêtez", fg = "red", command = quit, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)

            self.__Menu_fin.pack(pady = 100)
        
        elif self.__score == 700 and self.__malogic.get_taille_liste_niveau() == 2 : # condition si le joueur casse toutes les briques (gagner)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les gagnants
            self.__Menu_fin = Frame(self.__window, background = "#FFFFFF", relief = "raised", width = 450, height = 350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin, text = "Victoire", background = "#FFFFFF", font = ("Californian FB",25)).pack(pady = 30)

            # boutons pour continuer le jeu ou arrêter
            Button(self.__Menu_fin, text = "Continuez", fg = "green", command = self.continuer, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)
            Button(self.__Menu_fin, text = "Arrêtez", fg = "red", command = quit, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)

            self.__Menu_fin.pack(pady = 100)
        
        elif self.__score == 1050 and self.__malogic.get_taille_liste_niveau() == 1 : # condition si le joueur casse toutes les briques (gagner)

            self.__bandeau.destroy()
            self.__zone_jeu.destroy()

            # mise en place du menu de fin pour les gagnants
            self.__Menu_fin = Frame(self.__window, background = "#FFFFFF", relief = "raised", width = 450, height = 350)
            self.__Menu_fin.pack_propagate(False)
            Label(self.__Menu_fin, text = "Victoire", background = "#FFFFFF", font = ("Californian FB",25)).pack(pady = 30)

            self.__malogic.meilleur_score(self.__score) # renvoie du score du joueur pour l'afficher ou pas dans les meilleurs scores


            # boutons pour arrêter
            Button(self.__Menu_fin, text = "Arrêtez", fg = "red", command = quit, font = ("Arial",10), width = 15, height = 2).pack(pady = 6)

            self.__Menu_fin.pack(pady = 100)

    
    def rejouer(self): 
        '''fonction si le joueur décide rejouer au jeu'''

        self.__Menu_fin.destroy()
        self.__malogic.__init__() # remise à zéro du score, de la vie et des niveaux
        self.lancement_jeu()

    def continuer(self): 
        '''fonction si le joueur décide de continuer de jouer après sa vitoire au niveau auquel il était'''

        self.__Menu_fin.destroy()
        self.__malogic.remove_niveau() # changement de niveau pour monter en difficulté
        self.lancement_jeu()
    



