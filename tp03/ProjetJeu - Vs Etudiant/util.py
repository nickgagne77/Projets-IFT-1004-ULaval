from tkinter.filedialog import *
from tkinter import messagebox, simpledialog
from sorcier import Sorcier
from guerrier import Guerrier
import sys
 
class MauvaisFormatException(Exception):
    pass

class Annuler(Exception):
    pass
class Util:
    """
    Classe utilitaire comportant uniquement des méthodes statiques.
    """
    TYPE_SORCIER = "Sorcier"
    TYPE_GUERRIER = "Guerrier"

    @staticmethod
    def lire_fichier_personnages(fichier, liste_personnages):
        """
        Permet de lire un fichier de personnages reçu en entrée et de remplir la liste de personnages. Pour plus
        de détails, voir l'énoncé du travail. 
        Args:
            fichier (str): Le nom du fichier à lire 
            liste_personnages (list): La liste de personnages que la méthode doit remplir.  

        Returns:

        """
        try:
            f = open(fichier, 'r')
            liste_lignes = f.readlines()
            f.close()
            for ligne in liste_lignes:
                if ligne.count(';') < 4:
                    raise MauvaisFormatException
        except FileNotFoundError:
            return False
        except MauvaisFormatException:
            return False
        
        try:
            pass
        except Exception:
            print(sys.stderr, "erreur d'execution dans gestionOuvrir")
            sys.exit(1)
            return False
        ligne_tmp = []
        for ligne in liste_lignes:
            ligne_tmp = (ligne.rstrip('\n').split(';'))
            if ligne_tmp[0] == "Sorcier":
                liste_personnages.append(Sorcier(ligne_tmp[1], int(ligne_tmp[2]), int(ligne_tmp[3]), int(ligne_tmp[4])))
            else:
                liste_personnages.append(Guerrier(ligne_tmp[1], int(ligne_tmp[2]), int(ligne_tmp[3]), int(ligne_tmp[4])))
        return True


    @staticmethod
    def ecrire_fichier_personnages(fichier, liste_personnages):
        """
        Permet d’écrire la liste de personnages reçue en paramètre dans le fichier de personnages aussi reçu en entrée.
        Pour plus de détails, voir l'énoncé du travail.
        Args:
            fichier: fichier texte à écrire pour stocker les personnages
            liste_personnages: Liste de personnages à écrire dans le fichier
        """
        try:
            f = open(fichier, 'w')
        except FileNotFoundError:
            return False
        
        chaine = "{};{};{};{};{}"
        for ligne in liste_personnages:
            if isinstance(ligne, Sorcier):
                f.write(chaine.format("Sorcier", ligne.nom, ligne.energie_depart, ligne.energie_courante, ligne.nbr_charmes))
                f.write('\n')
            elif isinstance(ligne, Guerrier):
                f.write(chaine.format("Guerrier", ligne.nom, ligne.energie_depart, ligne.energie_courante, ligne.force))
                f.write('\n')
        f.close()
        return True

    @staticmethod
    def saisir_objet_entier(question):
        """
        Permet de demander la saisie d'un entier et de le valider
        Args:
            question (str): La question à poser 

        Returns (int): L'entier saisi

        """
        objet_entier = -1

        valide = False

        while not valide:
            objet_entier = simpledialog.askstring("Saisie d'un entier", question)
            if objet_entier == None:
                raise Annuler

            try:
                objet_entier = int(objet_entier)
                valide = True
            except ValueError:
                messagebox.showerror("Erreur", message="Aucune saisiee effectuée.")
            
                

        return objet_entier


    @staticmethod
    def saisir_string(question):
        """
        Permet de demander la saisie d'une chaîne de caractères
        Args:
            question (str): La question à poser 

        Returns (str): La chaîne saisie

        """
        string_temp = ""

        valide = False

        while string_temp == "" and not valide:
            string_temp = simpledialog.askstring("Saisie d'une chaine de caractères", question)
            if string_temp == None:
                raise Annuler

            if string_temp == "":
                messagebox.showerror("Erreur", message="Aucune saisie effectuée.")
            else:
                valide = True

        return string_temp
