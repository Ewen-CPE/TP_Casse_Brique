"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""
#Bibliothèques utilisées
from tkinter import Tk,Label,Frame,Button,Canvas


class Raquette:
    def __init__(self,zone_jeu):
        self.__zone_jeu = zone_jeu
        self.__position_départ_x = 390
        self.__position_départ_y = 460
        self.__taille_x = 70
        self.__taille_y = 10
        self.__couleur = "blue"
        self.__raquette = None
        self.__position_x = 390

    def create_raquette(self):
        self.__raquette = self.__zone_jeu.create_rectangle(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__taille_x,self.__position_départ_y+self.__taille_y,fill = self.__couleur)
    def clavier(self,event):
        self.__touche = event.keysym
        if self.__touche == "Left":
            if self.__position_x <= 10 :
                self.__position_x -=0
            else:
                self.__position_x -= 10 
        if self.__touche == "Right":
            if self.__position_x >= 770 :
                self.__position_x += 0
            else:
                self.__position_x += 10
        self.__zone_jeu.coords(self.__raquette,self.__position_x,self.__position_départ_y,self.__position_x + self.__taille_x,self.__position_départ_y + self.__taille_y)
    def mouv_raquette(self):
        self.__zone_jeu.focus_set()
        self.__zone_jeu.bind('<Key>',self.clavier)
        self.__zone_jeu.pack()
    def get_position_x(self):
        return self.__position_x
    def get_position_y(self):
        return self.__position_départ_y
    def get_taille_x(self):
        return self.__taille_x
    def get_taille_y(self):
        return self.__taille_y

