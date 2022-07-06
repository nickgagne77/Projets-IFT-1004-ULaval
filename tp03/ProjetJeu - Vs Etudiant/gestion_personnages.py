from tkinter.filedialog import *
from tkinter import messagebox

from util import Util
from personnage import Personnage
from sorcier import Sorcier
from guerrier import Guerrier


class GestionPersonnages:
    """
    Classe s'occupant de la gestion des personnages.
    Attributes:
        liste_personnages (list): La liste des personnages
        fichier_courant (str): Le nom du fichier courant
    """

    def __init__(self, liste_personnages=[], fichier_courant=None):
        self.liste_personnages = liste_personnages
        self.fichier_courant = fichier_courant

    def mettre_a_jour_liste(self):
        """
        Mets à jour et trie la liste des personnages par rapport à l'énergie courante.
        Returns (list str): La liste triée des chaînes de caractères des personnages

        """
        n = len(self.liste_personnages)

        # Parcourir toute la liste
        for i in range(n):
            for j in range(0, n - i - 1):

                # Remplacer element courant si est plus grand que le prochain
                if self.liste_personnages[j].energie_courante > self.liste_personnages[j + 1].energie_courante:
                    self.liste_personnages[j], self.liste_personnages[j + 1] = self.liste_personnages[j + 1], \
                                                                               self.liste_personnages[j]
        liste_ordonnee_str = []
        for objet in self.liste_personnages:
            liste_ordonnee_str.append(objet.to_string())

        return liste_ordonnee_str

    def gestion_creer_sorcier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier)
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """
        personnage = self.saisir_et_creer_sorcier()
        if personnage is not None:
            self.ajouter_personnage(personnage)
            messagebox.showinfo("Ajout d'un Sorcier", message="Le nouveau Sorcier a été ajouté à la liste")
        else:
            messagebox.showerror("Erreur", "Le Sorcier n'a pas été ajouté.")

    def saisir_et_creer_sorcier(self):
        """
        Retourne un objet Sorcier valide. Chaque information du sorcier demandée doit être validée.
        L’annulation d’une info entraine automatiquement l’annulation des informations suivantes.
        Si toutes les informations sont valides, un sorcier est alors instancié.

        Return (Sorcier): Le sorcier instancié si la création a réussie, None sinon.
        """
        nom = Util.saisir_string("Saisir le nom du Sorcier? (Entre 3 et 30)")
        energie_depart = Util.saisir_objet_entier(
            "Donnez la valeur de l'énergie de départ? (Une valeur positive plus petite que 101)")
        charmes = Util.saisir_objet_entier("Donnez la valeur de charmes? (une valeur positive plus petite que 21)")
        sorcier = Sorcier(nom, energie_depart, energie_depart, charmes)
        if sorcier.valider_energie_depart(sorcier.energie_depart) and sorcier.valider_nbr_charmes(
                sorcier.nbr_charmes) and sorcier.valider_nom(sorcier.nom):
            return sorcier
        else:
            None

    def gestion_creer_guerrier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier)
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """
        personnage = self.saisir_et_creer_guerrier()
        if personnage is not None:
            self.ajouter_personnage(personnage)
            messagebox.showinfo("Ajout d'un Guerrier", message="Le nouveau Guerrier a été ajouté à la liste")
        else:
            messagebox.showerror("Erreur", "Le Guerrier n'a pas été ajouté.")

    def saisir_et_creer_guerrier(self):
        """
        Retourne un objet Guerrier valide.  Chaque information du guerrier demandée doit être validée.
        L’annulation d’une information entraine automatiquement l’annulation des informations suivantes.
        Si toutes les infos sont valides, un guerrier est alors instancié.

        Returns (Guerrier): Le guerrier instancié si la création a réussie, None sinon.
        """
        nom = Util.saisir_string("Saisir le nom du Guerrier (entre 3 et 30): ")
        energie_depart = Util.saisir_objet_entier(
            "Donnez la valeur de l'énergie de départ? (Une valeur positive plus petite que 101)")
        forces = Util.saisir_objet_entier("Donnez la valeur de la force? (une valeur positive plus petite que 81)")
        guerrier = Guerrier(nom, energie_depart, energie_depart, forces)
        if guerrier.valider_energie_depart(guerrier.energie_depart) and guerrier.valider_force(
                guerrier.force) and guerrier.valider_nom(guerrier.nom):
            return guerrier
        else:
            None

    def ajouter_personnage(self, personnage):
        """
        Ajoute le Personnage à la liste.
        Args:
            personnage (Personnage): Le personnage à ajouter.
        """
        self.liste_personnages.append(personnage)

    def gestion_attaquer(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.
        Si le personnage sélectionné n’est pas mort, on saisit avec validation la force de l’attaque
        (> 0 et <= energie_max).  Lorsque la force saisie est valide, on attaque le personnage sélectionné sinon on
        affiche un message adéquat.  S’il n’y a aucun personnage sélectionné ou s’il est mort,
        un message est affiché.

        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        if index != -1:
            personnage = self.liste_personnages[index]
            if not personnage.est_mort():
                force_attaque = Util().saisir_objet_entier(
                    "Entrez la force de l'attaque? (Une valeur positive plus petite que 101)")
                if personnage.valider_energie_courante(force_attaque):
                    personnage.attaquer(force_attaque)
                else:
                    messagebox.showinfo("Erreur", message="L'attaque ne peut être réalisée.")
            else:
                messagebox.showinfo("Erreur", message="Le personnage selectionné est mort.")
        else:
            messagebox.showinfo("Erreur", message="Il n'y a aucun personnage sélectionné.")

    def gestion_augmenter_energie(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.
        Si le personnage sélectionné n’est pas mort, réinitialiser son énergie. S’il n’y a aucun personnage
        sélectionné ou s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        if index != -1:
            personnage = self.liste_personnages[index]
            if not personnage.est_mort():
                personnage.reset_energie()
            else:
                messagebox.showinfo("Erreur", message="Le personnage selectionné est mort.")
        else:
            messagebox.showinfo("Erreur", message="Il n'y a aucun personnage sélectionné.")

    def gestion_crier(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.
        Si le personnage sélectionné n’est pas mort, émettre son cri.  S’il n’y a aucun personnage sélectionné ou
        s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        if index != -1:
            personnage = self.liste_personnages[index]
            if not personnage.est_mort():
                messagebox.showinfo("Cri du personnage", message=personnage.crier())
            else:
                messagebox.showinfo("Erreur", message="Le personnage selectionné est mort.")
        else:
            messagebox.showinfo("Erreur", message="Il n'y a aucun personnage sélectionné.")

    def gestion_ouvrir(self):
        """
        Permet de gérer l'ouverture et la lecture d'un fichier de personnages
        (un fichier .txt qui contient des informations sur des personnages, un personnage par ligne).
        Si la liste n’est pas vide, on demande à l’utilisateur s’il veut sauvegarder les données courantes et
        s’il répond oui, on fait appel à gestion_enregistrer_sous.  Ensuite, on demande à l’utilisateur le nom du
        fichier à ouvrir.  Si le fichier choisi n’est pas null, le fichier à ouvrir devient le fichier courant
        et si la lecture du fichier n’a pas bien fonctionné (voir méthode lireFichierPersonnages dans classe Util),
        un message d’erreur est affiché.
        """

    def gestion_enregistrer(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans le fichier courant.
        Si on a un fichier courant, on écrit les personnages de la liste dedans
        (voir méthode ecrire_fichier_personnages dans la classe Util) et on affiche un message approprié.
        Si l’enregistrement n’a pas fonctionné, un message d’erreur est affiché. Si on n’a pas de fichier courant,
        on enregistre dans un nouveau fichier en appelant la méthode (gestion_enregistrer_sous).
        """

    def gestion_enregistrer_sous(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans un nouveau fichier.
        On demande un nom de fichier à l’utilisateur, on l’assigne au fichier courant et on écrit
        dedans les personnages (voir méthode ecrire_fichier_personnages dans la classe Util).
        Afficher un message personnalisé s’il y a erreur lors de la sauvegarde ou si la sauvegarde est ok.
        """

    def gestion_vider_liste(self):
        """
        Permet de fermer le fichier courant. Si la liste n'est pas vide et que l'utilisateur veut sauvegarder ses
        données, enregistrer les données de la liste dans le fichier courant (gestion_enregistrer) ou dans un
        nouveau fichier (gestion_enregistrer_sous) s’il n’y a pas de fichier courant.
        La liste est vidée et le fichier courant devient none.
        """

    def gestion_quitter(self):
        """
        Permet de quitter l'application après confirmation de l'utilisateur.
        """

    def get_personnage(self, index):
        return self.liste_personnages[index]
