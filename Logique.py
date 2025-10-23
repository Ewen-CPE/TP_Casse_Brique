"""
utf-8
But : créer une classe logique qui contient toutes les informations de types "logique" du jeu casse-brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
"""

class Logique:
    def __init__(self): # initialisation de la classe
        self.__score = 0 #score du joueur au début du jeu
        self.__vies = 3 #vies du joueurs au début du jeu

#Implémentation de différents niveau de jeu avec le système d'une file
        self.__niveau1 = 1
        self.__niveau2 = 1.5 #coefficient multiplicateur de la vitesse de la balle
        self.__niveau3 = 2 #coefficient multiplicateur de la vitesse de la balle
        self.__niveau = [self.__niveau1, self.__niveau2, self.__niveau3] #file qui contient tous les niveaux de jeu

    def initialisation(self): # initialisation du score et des vies du joueur à chaque fois que le joueur relance le jeu
        self.__vies = 3
    
    def meilleur_score(self,perf): # remplacement des meilleurs scores si la performance du joueur est supérieur au meilleur score précedént
        with open("score.txt","r") as score_lu:
            lignes = score_lu.readlines() #lecture du fichier texte score.txt et extraction du contenue des lignes
        
        #Données du meilleur score sous forme de pile

        for j in range(len(lignes)):
            lignes[j]=lignes[j].split(" ")[0] # séparation du score et du retour à la ligne (\n)
        
        if perf > int(lignes[0]): #vérification si la performance du joueur peut remplacer le meilleur score

            #implémentation du meilleur score dans notre pile
            lignes[2] = lignes[1]
            lignes[1] = lignes[0]
            lignes[0] = perf

        elif perf > int(lignes[1]): #vérification si la performance du joueur peut remplacer le deuxième meilleur score

            #implémentation du meilleur score dans notre pile
            lignes[2] = lignes[1]
            lignes[1] = perf

        elif perf > int(lignes[2]): #vérification si la performance du joueur peut remplacer le troisième meilleur score

            #implémentation du meilleur score dans notre pile
            lignes[2] = perf

        with open("score.txt","w") as score_ecrit:
            for k in range(3):
                score_ecrit.write(str(lignes[k]) + " \n") #écriture des nouveaux meilleurs scores dans le fichier score.txt


# "guetteur" de la classe logique pour accéder au score, aux vies et au niveau
    def get_score(self):
        return self.__score
    
    def get_vies(self):
        return self.__vies
    
    def get_niveau(self):
        return self.__niveau[0] # premier élément car les niveaux sont compris dans une file
    
    def get_taille_liste_niveau(self):
        return len(self.__niveau)

# Fonctions pour changer le score, les vies et le niveau  
    def add_score(self):
        self.__score += 10 # Chaque brique cassée rapporte 10 points

    def add_vies(self):
        self.__vies -= 1 # Chaque fois que la balle touche le sol on perd une vie 

    def remove_niveau(self):
        self.__niveau.pop(0) # Lorsqu'un niveau est réussie et que le joueur continue de jouer on enlève le niveau réussi pour passer au suivant
