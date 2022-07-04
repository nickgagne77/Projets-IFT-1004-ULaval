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
        self.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=menu)
        menu.add_command(label="Ouvrir...", command=self.menuOuvrir_Click)
        menu.add_command(label="Enregistrer", command=self.menuEnregistrer_Click)
        menu.add_command(label="Enregistrer sous...", command=self.menuEnregistrerSous_Click)
        menu.add_command(label="Vider liste", command=self.menuViderListe_Click)
        menu.add_command(label="Quitter", command=self.menuQuitter_Click)
       #ajouter les autres options


        self.master.config(menu=self.menubar)

        # frame 1 (droite)
        self.frame1 = Frame(self)
        self.frame1.grid(row=0, column=1)
        # frame 2 (gauche)
        self.frame2 = Frame(self)
        self.frame2.grid(row=0, column=0)
        # Ajout de labels dans les frames
        

        # Ajout du listbox
        self.scrollbar = Scrollbar(self.frame2, orient="vertical")
        self.listbox = Listbox(self.frame2, height= 25, width=80)
        self.listbox.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1)
        self.listbox.config(yscrollcommand=self.scrollbar.set)  
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<Button-1>', self.listbox_Click)
        # Ajout de bouttons
        self.creer_sorcier_bouton = Button(self.frame1, text="Créer un sorcier", height=4, width=26)
        self.creer_sorcier_bouton.bind('<ButtonRelease>', self.btnSorcier_Click)
        self.creer_guerrier_bouton = Button(self.frame1, text="Créer un guerrier", height=4, width=26)
        self.creer_guerrier_bouton.bind('<ButtonRelease>', self.btnGuerrier_Click)
        self.attaquer_bouton = Button(self.frame1, text="Attaquer", height=4, width=26)
        self.attaquer_bouton.bind('<ButtonRelease>', self.btnAttaquer_Click)
        self.redonner_energie_bouton = Button(self.frame1, text="Réinitialiser l'Énergie", height=4, width=26)
        self.redonner_energie_bouton.bind('<ButtonRelease>', self.btnRedonnerEnergie_Click)
        self.crier_bouton = Button(self.frame1, text="Crier", height=4, width=26)
        self.crier_bouton.bind('<ButtonRelease>', self.btnCrier_Click)
        
        self.creer_sorcier_bouton.grid(row=0, column=0, sticky=N, pady=4, padx=1)
        self.creer_guerrier_bouton.grid(row=1, column=0, sticky=N, pady=4, padx=1)
        self.attaquer_bouton.grid(row=2, column=0, sticky=N, pady=4, padx=1)
        self.redonner_energie_bouton.grid(row=3, column=0, sticky=N, pady=4, padx=1)
        self.crier_bouton.grid(row=4, column=0, sticky=N, pady=4, padx=1)

    def listIsEmpty(self):
        try:
            self.index = int(self.listbox.curselection()[0])
        except IndexError:
            return True

        return False

    #Ajoute un personnage dans la listbox
    def appendList(self, personnage):
        self.listbox.insert(END, personnage)


    #Remplace tous les personnages de la listbox par une nouvelle liste
    def updateList(self, personnages):
        self.listbox.delete(0, END)

        for personnage in personnages:
            self.listbox.insert(END, personnage)

        self.pIndex = -1

    #Permet d'identifier le personnage selectionné (set pIndex)
    def listbox_Click(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        index = widget.curselection()[0]

        #print ("selection:", selection, ": '%s'" % value)

        self.pIndex = index
        #print(gp.getPersonnage(index))


    def menuOuvrir_Click(self):
        self.gp.gestionOuvrir()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)


    def menuEnregistrer_Click(self):
        self.gp.gestionEnregistrer()

    def menuEnregistrerSous_Click(self):
        self.gp.gestionEnregistrerSous()


    def menuViderListe_Click(self):
        self.gp.gestionViderListe()
        self.listbox.delete(0, END)
            #quit()

    def menuQuitter_Click(self):
        if self.gp.gestionQuitter():
            quit()



    def btnSorcier_Click(self):
        self.gp.gestionCreerSorcier()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)

    def btnGuerrier_Click(self):
        self.gp.gestionCreerGuerrier()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)


    def btnAttaquer_Click(self):
        self.gp.gestionAttaquer(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")


    def btnRedonnerEnergie_Click(self):
        self.gp.gestionAugmenterEnergie(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettreAJourListe()

        # Update listview
        self.updateList(personnages)

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnCrier_Click(self):
        self.gp.gestionCrier(self.pIndex)
        row = self.pIndex

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")



def main():
    root = Tk()
    root.geometry("700x400+300+100")
    app = Interface(root)
    root.mainloop()



if __name__ == '__main__':
    main()
    