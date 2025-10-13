"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""
#Bibliothèques utilisées
from Interface_Graphique import Interface_Graphique


class Raquette(Interface_Graphique):
    def __init__(self):
        super().__init__()
        self.__position_départ_x = 100
        self.__position_départ_y = 100
        self.__taille_x = 100
        self.__taille_y = 20
        self.__couleur = "blue"
    def create_raquette(self):
        #zone_jeu = super().zone_de_jeu()
        #zone_jeu.create_rectangle(self.__position_départ_x,self.__position_départ_y,self.__position_départ_x+self.__taille_x,self.__position_départ_y+self.__taille_y,fill = self.__couleur)
        pass
