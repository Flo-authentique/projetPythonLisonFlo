import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        self.m = Moteur()
        
        self.matrice = self.m.matrice
        
        self.root = root

        self.root.attributes('-fullscreen',True)
        self.root.bind("<Escape>",self.quitterEchap)
        self.root.title("Flood It")
        #self.root.background("black")
        
        

        self.cote = 800 # format de la fenêtre de jeu
        
        #prendre les infos de la fenêtre
        self.ecranLargeur = root.winfo_screenwidth()
        self.ecranHauteur = root.winfo_screenheight()        
        
        print(self.ecranLargeur,self.ecranHauteur)
        
        self.canvas=tk.Canvas(root,width=self.ecranLargeur,height=self.ecranHauteur,borderwidth=0,bg="Black")
        
        self.canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N+tk.S+tk.W)
        
        self.titre = tk.PhotoImage(file="titre.png")
        print(self.ecranLargeur//2)
        self.canvas.create_image((self.ecranLargeur//2,100),image=self.titre) #fixer le titre au milieu de l'écran
        
        #affichage respectif
        self.afficheAutre()
        self.afficheJeu(self.matrice)
        
        
    def afficheJeu(self,matrice):
        
        #self.m.montre()
        pass
        
 
    def afficheAutre(self):
        #BOUTON QUITTER
        self.boutton_quitter=None
        self.root.protocol("WM_DELETE_WINDOW",self.quitter)

        self.boutton_quitter=tk.Button(self.canvas,borderwidth=0,bg="Red",activebackground="Blue",command=self.quitter,cursor="X_cursor").place(x=10,y=10)
    
    
    
    def quitterEchap(self,event):
        self.quitter()
    def quitter(self):
        self.root.destroy()
