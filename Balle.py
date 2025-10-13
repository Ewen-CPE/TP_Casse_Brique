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


class Balle:
    def __init__(self):
        self.__zone_jeu = Interface_Graphique.zone_de_jeu
        self.__position_départ_x = 100
        self.__position_départ_y = 100
        self.__rayon = 10
        self.__couleur = "blue"
    def create_raquette(self):
       self.__zone_jeu.create_oval(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__rayon,self.__position_départ_y+self.__rayon,fill = self.__couleur)
       self.__zone_jeu.pack()