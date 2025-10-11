"""
utf-8
But : Jeu casse brique
Ewen LE COGUIEC, ZALTENI chloé
3ETI
06/10/2025
Que reste-t-il à faire ?
"""

# Bibliothèques importés
from tkinter import Tk,Label,Frame,Button,Canvas

class Interface_Graphique:
    def __init__(self):
        self.__window = Tk()
        self.__window_title = self.__window.title("Casse Brique")
        self.__window_geometry = self.__window.geometry("860x520")
        self.__window_config = self.__window.config(background="#000000")

        self.__Menu = Frame(self.__window,background="#FFFFFF",relief="raised",width=450,height=350)
        self.__Menu.pack_propagate(False)
        self.__Menu_Label = Label(self.__Menu,text="Menu du Jeu",width=20,height=5).pack(pady=30)
        self.__Menu.pack(pady=100)

        self.__Bouton_Démarrez = Button(self.__Menu,text="Démarrez",fg="green",command = self.lancement_jeu,width=8,height=2).pack(pady=8)
        self.__Bouton_Arreter = Button(self.__Menu,text="Arrêtez",fg="red",command = quit,width=8,height=2).pack(pady=6)
        self.__Bouton_Paramètre = Button(self.__Menu,text="Paramètre",fg="navy",width=8,height=2).pack(pady=6)
        
        self.__zone_de_jeu = None
        
        self.__score= 0
        self.__vies = 3
        self.__bandeau = None

        self.__window_affichage = self.__window.mainloop()
    def lancement_jeu(self):
        self.__Menu.destroy()
        self.__bandeau = Frame(self.__window,width=860,height=30,background="black")
        self.__Menu_pack_propagate = self.__bandeau.pack_propagate(False)
        self.__score_affichage = Label(self.__bandeau,text="Score : "+str(self.__score),fg="white",background="black",font=("Courrier",20)).pack(side="left", padx=5)
        self.__vies_affichage = Label(self.__bandeau,text="Vies : "+str(self.__vies),fg="white",background="black",font=("Courrier",20)).pack(side="right",padx=5)
        self.__bandeau.pack()
        self.__zone_de_jeu = Canvas(self.__window,width=850,height=490,background="black").pack()



       


