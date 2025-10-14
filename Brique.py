"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""
from tkinter import Tk,Label,Frame,Button,Canvas
import random as rd


class Brique:
    def __init__(self,zone_jeu):
        self.__zone_jeu = zone_jeu
        self.__position_départ_x = 10
        self.__position_départ_y = 3
        self.__taille_x = 100
        self.__taille_y = 30
        self.__espacement_x = 22
        self.__espacement_y = 10
        self.__liste_couleur = ["red","green","blue","yellow","orange","pink","purple"]
        self.__liste_brique = []
        self.__brique = None
    def create_Briques(self):
        indice = 0
        for k in range(1,6):
            for i in range(1,8):
                self.__brique = self.__zone_jeu.create_rectangle(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__taille_x,self.__position_départ_y+self.__taille_y,fill = self.__liste_couleur[rd.randint(0,6)])
                self.__liste_brique.append([indice,self.__position_départ_x,self.__position_départ_y,self.__brique])
                indice += 1
                self.__position_départ_x += self.__taille_x + self.__espacement_x
            self.__position_départ_x =10
            self.__position_départ_y += self.__taille_y + self.__espacement_y

            
            
            
    def get_position_y(self,numero):
        for j in range(len(self.__liste_brique)):
            if self.__liste_brique[j][0] == numero :
                return self.__liste_brique[j][2]
    def get_position_x(self,numero):
        for j in range(len(self.__liste_brique)):
            if self.__liste_brique[j][0] == numero :
                return self.__liste_brique[j][1]
    def get_taille_y(self):
        return self.__taille_y
    def get_taille_x(self):
        return self.__taille_x
    def get_taille_liste(self):
        return len(self.__liste_brique)
    def destruct_brique(self,numero):
        self.__zone_jeu.delete(self.__liste_brique[numero][3])
        self.__liste_brique.remove(self.__liste_brique[numero])