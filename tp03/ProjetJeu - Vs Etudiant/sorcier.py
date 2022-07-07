from personnage import Personnage


class Sorcier(Personnage):
    """ 
    Classe représentant un Sorcier. Hérite de Personnage.
    Attributes:
        nb_charmes_defaut (int): Le nombre de charmes par défaut
        nb_charmes_max (int): Le nombre de charmes maximum
        nb_charmes (int): Le nombre de charmes courant
    """
    def __init__(self, nom, energie_depart, energie_courante, nbr_charmes):
        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB: pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie_courante: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """
        super().__init__(nom, energie_depart)
        self.nbr_charmes_defaut = 20
        self.nbr_charmes_max = 20
        # Bien que les consignes indiquent que l'attribut nbr_charmes = 0, il ne s'agit que d'une borne inférieure
        self.nbr_charmes = nbr_charmes
        # L'attribut energie_courante est obtenue de la classe parente
        # self.energie_courante = energie_courante

    def to_string(self, classe_perso=2):
        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """
        return super().to_string(classe_perso)

    def valider_nbr_charmes(self, nb_charmes):
        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """
        return nb_charmes >= 0 and nb_charmes <= self.nbr_charmes_max

    def crier(self):
        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """
        return "Je vais tous vous anéantir!"

    def attaquer(self, force_attaque):
        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """
        if force_attaque >= self.energie_courante:
            self.energie_courante = 0
        else:
            self.energie_courante -= force_attaque

    def get_nbr_charmes(self):
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.

        """
        return self.nbr_charmes

    def set_nbr_charmes(self, nb_charmes):
        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """
        if self.valider_nbr_charmes(nb_charmes):
            self.nbr_charmes = nb_charmes
            return True
        else:
            return False


if __name__ == '__main__':
    sorc1 = Sorcier("John", 10, 20, 30)
    sorc2 = Sorcier("Yu", 50, 100, 21)
    sorc3 = Sorcier("Larry", 25, 15, -1)
    print()
    print("Tests unitaires en cours...")
    print()
    
    assert type(sorc1) == Sorcier

    assert not sorc1.set_nbr_charmes(21)
    sorc1.set_nbr_charmes(10)
    assert sorc1.nbr_charmes == 10
    assert sorc1.get_nbr_charmes() == 10


    assert sorc1.valider_nbr_charmes(sorc1.nbr_charmes)
    assert not sorc2.valider_nbr_charmes(sorc2.nbr_charmes)
    assert not sorc3.valider_nbr_charmes(sorc3.nbr_charmes)

    assert sorc2.get_nbr_charmes() == 21

    assert sorc1.crier() == "Je vais tous vous anéantir!"

    sorc1.attaquer(5)
    assert sorc1.energie_courante == 15

    sorc1.attaquer(-5)
    assert sorc1.energie_courante == 20

    sorc1.attaquer(sorc1.energie_courante)
    assert sorc1.energie_courante == 0

    assert sorc1.to_string() == "Le sorcier John a une énergie de 0 et 10 charmes."

    print("Tests réussis!")
