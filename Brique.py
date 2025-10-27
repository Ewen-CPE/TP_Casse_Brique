"""
utf-8
But : Créer une classe pour les briques du jeu
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
"""
#Bibliothèque utilisé

import random as rd

# Classe

class Brique:
    def __init__(self,zone_jeu):
        '''initialisation de la classe'''

        self.__zone_jeu = zone_jeu #argument de la zone de jeu à paramétrer lors de l'utilisation de la classe

        #caractéristique des briques
        self.__position_départ_x = 10
        self.__position_départ_y = 3
        self.__taille_x = 100
        self.__taille_y = 30
        self.__espacement_x = 22 # Espacement "x" des briques
        self.__espacement_y = 10 # Espacement "y" des briques

        # Liste des couleurs pour les briques
        self.__liste_couleur = ["red","green","blue","yellow","orange","pink","purple"]

        #Liste des briques
        self.__liste_brique = []

        self.__brique = None

    def create_Briques(self):
        '''fonction qui créer les briques pour le jeu'''

        indice = 0 # indique le numéro de la brique

        for _ in range(1,6):
            for _ in range(1,8):
                self.__brique = self.__zone_jeu.create_rectangle(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__taille_x,self.__position_départ_y+self.__taille_y,fill = self.__liste_couleur[rd.randint(0,6)]) # création d'une brique
                self.__liste_brique.append([indice,self.__position_départ_x,self.__position_départ_y,self.__brique]) # ajout de la brique à la liste de brique avec son indice, sa position "x", sa position "y" et son canevas
                indice += 1
                self.__position_départ_x += self.__taille_x + self.__espacement_x # met à jour la position "x" pour la prochaine brique (largeur + espacement)
            self.__position_départ_x = 10 # position de départ pour la prochaine ligne de brique
            self.__position_départ_y += self.__taille_y + self.__espacement_y # met à jour la position "y" pour la prochaine brique (largeur + espacement)

            
            
    # Récupération de la position "x", de la position "y", de la vitesse "x", de la vitesse "y" et du diamètre

    def get_position_y(self,numero):
        '''
        entrée : numéro de la brique
        sortie : position y du coin supérieur gauche de la brique
        '''
        for j in range(len(self.__liste_brique)):
            if self.__liste_brique[j][0] == numero : # On prends la brique qui correspond au numéro en argument
                return self.__liste_brique[j][2] 
            
    def get_position_x(self,numero):
        '''
        entrée : numéro de la brique
        sortie : position x du coin supérieur gauche de la brique
        '''
        for j in range(len(self.__liste_brique)):
            if self.__liste_brique[j][0] == numero :
                return self.__liste_brique[j][1] 
            
    def get_taille_y(self):
        '''sortie : taille y de la brique'''
        return self.__taille_y
    
    def get_taille_x(self):
        '''sortie : taille x de la brique'''
        return self.__taille_x
    
    def get_taille_liste(self):
        '''sortie : taille de la liste de briques'''
        return len(self.__liste_brique)
    



    def destruct_brique(self,numero):
        '''
        Détruit une brique
        entrée : numéro de la brique
        
        '''
        self.__zone_jeu.delete(self.__liste_brique[numero][3])
        self.__liste_brique.remove(self.__liste_brique[numero])
        self.maj_indice()

    def maj_indice(self):
        '''Mise à jour des indices des briques'''
        for k in range(len(self.__liste_brique)):
            self.__liste_brique[k][0] = k