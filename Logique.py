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

    def initialisation(self): # initialisation des vies du joueur à chaque fois que le joueur relance le jeu
        self.__vies = 3
    
    def meilleur_score(self,perf): # remplacement du meilleurs score si la performance du joueur est supérieur au meilleur score précedént
        with open("score.txt","r") as score_lu:
            lignes = score_lu.readlines() #lecture du fichier texte score.txt et extraction du contenue des lignes
        
        #Données du meilleur score sous forme de pile

        for j in range(len(lignes)):
            lignes[2-j]=lignes[j].split(" ")[0] # séparation du score et du retour à la ligne (\n)

        if perf > int(lignes[2]): #vérification si la performance du joueur peut remplacer le meilleur score

            #implémentation du meilleur score dans notre pile
            lignes.append(perf)

        if len(lignes) == 4:
            lignes.pop(0)

        with open("score.txt","w") as score_ecrit:
            for k in range(3):
                score_ecrit.write(str(lignes[2-k]) + " \n") #écriture des 3 derniers meilleurs scores dans le fichier score.txt


# "guetteur" de la classe logique pour accéder aux scores, aux vies et aux niveaux
    def get_score(self):
        '''sortie : score du joueur'''
        return self.__score
    
    def get_vies(self):
        '''sortie : vies du joueur'''
        return self.__vies
    
    def get_niveau(self):
        '''sortie : niveau de jeu'''
        return self.__niveau[0] # premier élément car les niveaux sont compris dans une file
    
    def get_taille_liste_niveau(self):
        '''sortie : taille de la file des niveaux'''
        return len(self.__niveau)
    
    def get_meilleur_score(self):
        '''sortie : meilleur score'''
        with open("score.txt","r") as score_lu:
            score = score_lu.readlines() #lecture du fichier texte score.txt et extraction du contenue des lignes

        for i in range(len(score)):
            score[i] = score[i].split(" ")[0] # séparation du score et du retour à la ligne (\n)
        return score[0]

# Fonctions pour changer le score, les vies et le niveau  
    def add_score(self):
        self.__score += 10 # Chaque brique cassée rapporte 10 points

    def add_vies(self):
        self.__vies -= 1 # Chaque fois que la balle touche le sol on perd une vie 

    def remove_niveau(self):
        self.__niveau.pop(0) # Lorsqu'un niveau est réussie et que le joueur continue de jouer on enlève le niveau réussi pour passer au suivant
