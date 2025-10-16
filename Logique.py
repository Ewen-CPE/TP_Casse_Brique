"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""

class Logique:
    def __init__(self):
        self.__score= 0
        self.__vies = 3
    def get_score(self):
        return self.__score
    def get_vies(self):
        return self.__vies
    def add_score(self):
        self.__score += 10
    def add_vies(self):
        self.__vies -= 1
