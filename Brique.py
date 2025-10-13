"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""
from tkinter import Tk,Label,Frame,Button,Canvas
from Interface_Graphique import Interface_Graphique


class Brique:
    def __init__(self):
        self.__zone_jeu = Interface_Graphique.zone_de_jeu
        self.__position_départ_x = 100
        self.__position_départ_y = 100
        self.__taille_x = 100
        self.__taille_y = 20
        self.__couleur = "blue"
    def create_raquette(self):
        self.__zone_jeu.create_rectangle(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__taille_x,self.__position_départ_y+self.__taille_y,fill = self.__couleur)
        self.__zone_jeu.pack()