from tkinter import *
from tkinter.filedialog import *
from gestion_personnages import GestionPersonnages


class Interface(Frame):
    gp = GestionPersonnages()
    pIndex = -1

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
        self.pack(side=TOP, fill=BOTH, expand=True)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=menu)
        menu.add_command(label="Ouvrir...", command=self.menuOuvrir_Click)
        # Ajout de labels dans les frames
        # Ajout des autres options
        menu.add_command(label="Enregistrer", command=self.menuEnregistrer_Click)
        menu.add_command(label="Enregistrer sous...", command=self.menuEnregistrerSous_Click)
        menu.add_command(label="Vider liste", command=self.menuViderListe_Click)
        menu.add_command(label="Quitter", command=self.menuQuitter_Click)

        self.master.config(menu=self.menubar)
        
        # Methode .pack() utilisée car meilleur résultat su MacOS et Windows

        # frame 1 (droite)
        self.frame1 = Frame(self)
        self.frame1.pack(side=RIGHT,expand=YES) 
        
        # frame 2 (gauche)
        self.frame2 = Frame(self)
        self.frame2.pack(side=LEFT, expand=YES)   

        # Ajout du listbox
        self.listbox = Listbox(self.frame2, height=24, width=80)
        self.listbox.pack(side=LEFT, expand=YES) 
        self.scrollbar = Scrollbar(self.frame2, orient="vertical")
        self.scrollbar.pack(side=RIGHT, expand=YES) 
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.listbox_Click)
        self.var = IntVar()
        
        # Ajout de bouttons
        self.creer_sorcier_bouton = Button(self.frame1, text="Créer un sorcier", height=4, width=26)
        self.creer_sorcier_bouton.bind('<ButtonRelease-1>', self.btnSorcier_Click)
        self.creer_guerrier_bouton = Button(self.frame1, text="Créer un guerrier", height=4, width=26)
        self.creer_guerrier_bouton.bind('<ButtonRelease-1>', self.btnGuerrier_Click)
        self.attaquer_bouton = Button(self.frame1, text="Attaquer", height=4, width=26)
        self.attaquer_bouton.bind('<ButtonRelease-1>', self.btnAttaquer_Click)
        self.redonner_energie_bouton = Button(self.frame1, text="Réinitialiser l'Énergie", height=4, width=26)
        self.redonner_energie_bouton.bind('<ButtonRelease-1>', self.btnRedonnerEnergie_Click)
        self.crier_bouton = Button(self.frame1, text="Crier", height=4, width=26)
        self.crier_bouton.bind('<ButtonRelease-1>', self.btnCrier_Click)
        
        # Methode .pack() utilisée car meilleur résultat su MacOS et Windows
        
        self.creer_sorcier_bouton.pack(side=TOP) 
        self.creer_guerrier_bouton.pack(side=TOP) 
        self.attaquer_bouton.pack(side=TOP) 
        self.redonner_energie_bouton.pack(side=TOP)
        self.crier_bouton.pack(side=TOP) 

    def listIsEmpty(self):
        try:
            self.index = int(self.listbox.curselection()[0])
        except IndexError:
            return True

        return False

    # Ajoute un personnage dans la listbox
    def appendList(self, personnage):
        self.listbox.insert(END, personnage)

    # Remplace tous les personnages de la listbox par une nouvelle liste
    def updateList(self, personnages):
        self.listbox.delete(0, END)

        for personnage in personnages:
            self.listbox.insert(END, personnage)

        self.pIndex = -1

    # Permet d'identifier le personnage selectionné (set pIndex)
    def listbox_Click(self, event):
        widget = event.widget
        # selection=widget.curselection()
        try:
            index = widget.curselection()[0]
            self.pIndex = index
        # Survient si on aucun personnage sélectionné et on accroche un bouton
        except IndexError:
            pass
            
        #print(self.gp.get_personnage(index))

        # value = widget.get(selection[0])
        # print ("selection:", selection, ": '%s'" % value)

    def menuOuvrir_Click(self):
        self.gp.gestion_ouvrir()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.updateList(personnages)

    def menuEnregistrer_Click(self):
        self.gp.gestion_enregistrer()

    def menuEnregistrerSous_Click(self):
        self.gp.gestion_enregistrer_sous()

    def menuViderListe_Click(self):
        self.gp.gestion_vider_liste()
        self.listbox.delete(0, END)
        # quit()

    def menuQuitter_Click(self):
        if self.gp.gestion_quitter():
            quit()

    def btnSorcier_Click(self, event):
        self.gp.gestion_creer_sorcier()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.updateList(personnages)

    def btnGuerrier_Click(self, event):
        self.gp.gestion_creer_guerrier()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.updateList(personnages)

    def btnAttaquer_Click(self, event):
        self.gp.gestion_attaquer(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.updateList(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnRedonnerEnergie_Click(self, event):
        self.gp.gestion_augmenter_energie(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        self.updateList(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnCrier_Click(self, event):
        self.gp.gestion_crier(self.pIndex)
        row = self.pIndex

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")
        

def main():
    root = Tk()
    root.geometry("700x400+300+100")
    app = Interface(root)
    app.mainloop()

if __name__ == '__main__':
    main()
    