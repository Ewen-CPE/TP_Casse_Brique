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
        self.__niveau1 = 1
        self.__niveau2 = 1.5
        self.__niveau3 = 2
        self.__niveau =[self.__niveau1,self.__niveau2,self.__niveau3]
    def initialisation(self):
        self.__score= 0
        self.__vies = 3
    
    def meilleur_score(self,perf):
        with open("score.txt","r") as score_lu:
            lignes = score_lu.readlines()
        for j in range(len(lignes)):
            lignes[j]=lignes[j].split(" ")[0]

        if perf > int(lignes[0]):
            lignes[2] = lignes[1]
            lignes[1] = lignes[0]
            lignes[0] = perf
        elif perf > int(lignes[1]):
            lignes[2] = lignes[1]
            lignes[1] = perf
        elif perf > int(lignes[2]):
            lignes[2] = perf
        with open("score.txt","w") as score_ecrit:
            for k in range(3):
                score_ecrit.write(str(lignes[k]) + " \n")





    def get_score(self):
        return self.__score
    def get_vies(self):
        return self.__vies
    def get_niveau(self):
        return self.__niveau[0]
    
    def add_score(self):
        self.__score += 10
    def add_vies(self):
        self.__vies -= 1
    def remove_niveau(self):
        self.__niveau.pop(0)
