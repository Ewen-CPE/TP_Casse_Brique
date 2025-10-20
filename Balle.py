"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
"""

class Balle:
    def __init__(self,zone_jeu,niveau,couleur):
        '''initialisation de la classe'''

        self.__zone_jeu = zone_jeu #argument de la zone de jeu à paramétrer lors de l'utilisation de la classe
        self.__niveau = niveau #argument du niveau à paramétrer lors de l'utilisation de la classe
        
        #caractéristique de la balle
        self.__position_départ_x = 430
        self.__position_départ_y = 250
        self.__diametre = 20
        self.__couleur = couleur
        self.__position = [self.__position_départ_x,self.__position_départ_y]

        self.__vitesse_x = 2 *self.__niveau # Mise en place de la vitesse "x" en fonction du niveau
        self.__vitesse_y = 3 *self.__niveau # Mise en place de la vitesse "y" en fonction du niveau
        
        
    def create_balle(self):
       '''fonction qui créer la raquette du joueur'''

       self.__balle = self.__zone_jeu.create_oval(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__diametre,self.__position_départ_y+self.__diametre,fill = self.__couleur)

    def mouv_balle(self):
        '''fonction qui gère les déplacement automatique de la balle'''

        self.__position[0] = self.__position[0] + self.__vitesse_x
        if self.__position[0] > 850 - self.__diametre or self.__position[0] < 1:
            self.__vitesse_x = -self.__vitesse_x

        self.__position[1] = self.__position[1] + self.__vitesse_y
        if self.__position[1] > 490 - self.__diametre or self.__position[1] < 1:
            self.__vitesse_y = -self.__vitesse_y

        self.__zone_jeu.coords(self.__balle,self.__position[0],self.__position[1],self.__position[0] + self.__diametre,self.__position[1] + self.__diametre) # Mise à jour des coordonnées de la balle

        self.__zone_jeu.pack()
    
    # Récupération de la position "x", de la position "y", de la vitesse "x", de la vitesse "y" et du diamètre

    def get_position_x(self):
        return self.__position[0]
    
    def get_position_y(self):
        return self.__position[1]
    
    def get_diametre(self):
        return self.__diametre
    
    def get_vitesse_x(self):
        return self.__vitesse_x
    
    def get_vitesse_y(self):
        return self.__vitesse_y
    
    # Modification de la vitesse "x" et de la vitesse "y"
    def add_vitesse_y(self,vitesse_y):
        self.__vitesse_y = vitesse_y

    def add_vitesse_x(self,vitesse_x):
        self.__vitesse_x = vitesse_x
    
        


   
        