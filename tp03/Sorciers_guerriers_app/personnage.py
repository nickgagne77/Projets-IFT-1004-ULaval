from numpy import isin


class Personnage:
    """ 
    Attributes:
        energie_depart_defaut (int): L'énergie de départ par défaut
        energie_depart_min (int): L'énergie de départ minimum
        energie_max (int): L'énergie maximum en tout temps
        longueur_nom_min (int) : La longueur minimale du nom
        longueur_nom_max (int) : La longueur maximale du nom
        nom (str) : Le nom
        energie_depart (int): L'énergie de départ
        energie_courante (int): L'énergie courante
    """
    def __init__(self, nom, energie_depart):
        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """
        self.energie_depart_defaut = 20
        self.energie_depart_min = 1
        self.energie_max = 100
        self.longueur_nom_min = 3
        self.longueur_nom_max = 30
        self.nom = nom
        self.energie_depart = energie_depart
        self.energie_courante = energie_depart

    def crier(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self, force_attaque):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def est_mort(self):
        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """
        if self.energie_courante == 0:
            return True
        else:
            return False

    def valider_nom(self, nom):
        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """
        if self.longueur_nom_min <= len(nom) <= self.longueur_nom_max:
            return True
        else:
            return False 

    def valider_energie_courante(self, energie_courante):
        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.
        """
        if 0 <= energie_courante <= self.energie_max:
            return True
        else:
            return False

    def valider_energie_depart(self, energie_depart):
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """
        if self.energie_depart_min <= energie_depart <= self.energie_max:
            return True
        else:
            return False

    def reset_energie(self):
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """
        self.energie_courante = self.energie_depart

    def get_energie_courante(self):
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """
        return self.energie_courante

    def set_energie_courante(self, energie_courante):
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_courante(energie_courante):
            self.energie_courante = energie_courante
            return True
        else:
            return False

    def get_nom(self):
        """
        Retourne le nom.
        Returns (str): Le nom.
        """
        return self.nom

    def set_nom(self, nom):
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_nom(nom):
            self.nom = nom
            return True
        else:
            return False

    def get_energie_depart(self):
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """
        return self.energie_depart

    def set_energie_depart(self, energie_depart):
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_depart(energie_depart):
            self.energie_depart = energie_depart
            return True
        else:
            return False

    def to_string(self):
        """
        Retourne un chaine du genre : nom du Personnage, a une énergie de valeur de l'énergie.
        Returns:
            str: Chaine à retourner
        """
        return "{} a une énergie de {}".format(self.nom, str(self.energie_courante))
    
if __name__ == '__main__':
    pers1 = Personnage("John", 80)
    pers2 = Personnage("Yu", 50)
    pers3 = Personnage("Larry", 150)
    pers4 = Personnage("Hello My name is Anakin Skywalerker", 1)
    print()
    print("Tests unitaires en cours...")
    print()
    
    assert isinstance(pers1, Personnage)
    assert isinstance(pers3, Personnage)
    assert isinstance(pers3, Personnage)
    assert isinstance(pers4, Personnage)
    assert not isinstance("Dwight Schrute", Personnage)
    
    assert pers1.valider_nom(pers1.nom)
    assert not pers2.valider_nom(pers2.nom)
    assert pers3.valider_nom(pers3.nom)
    assert not pers4.valider_nom(pers4.nom)
    
    assert pers3.get_energie_depart() == 150
    
    assert not pers1.est_mort()
    assert not pers2.est_mort()
    
    assert pers1.valider_energie_depart(pers1.energie_depart)
    assert pers2.valider_energie_depart(pers2.energie_depart)
    assert not pers3.valider_energie_depart(pers3.energie_depart)
    
    assert not pers2.set_energie_depart(-20)
    assert not pers1.set_energie_depart(0)
    assert pers3.set_energie_depart(1)
    
    assert pers1.get_energie_depart() == 80
    assert pers2.get_energie_depart() == 50
    assert pers3.get_energie_depart() == 1
    
    assert pers3.set_energie_courante(75)
    assert pers1.set_energie_courante(30)
    assert not pers2.set_energie_courante(-40)
    
    assert pers1.get_energie_courante() == 30
    assert pers2.get_energie_courante() == 50
    assert pers3.get_energie_courante() == 75
    
    pers1.reset_energie()
    pers2.reset_energie()
    pers3.reset_energie()
    assert pers1.get_energie_courante() == 80
    assert pers2.get_energie_courante() == 50
    assert pers3.get_energie_courante() == 1
    
    assert not pers1.valider_energie_courante(-20)
    assert pers2.valider_energie_courante(pers2.energie_courante)
    assert pers3.valider_energie_courante(pers3.energie_courante)
    
    assert pers3.set_energie_courante(0)
    assert pers3.est_mort()
    assert not pers1.est_mort()
    assert not pers2.est_mort()
    
    assert pers1.set_nom("Nico")
    assert pers2.set_nom("Charles-Edouard")
    assert not pers3.set_nom("Hi")
    
    assert pers1.get_nom() == "Nico"
    assert pers2.get_nom() == "Charles-Edouard"
    assert pers3.get_nom() == "Larry"
    
    assert pers1.to_string() == "Nico a une énergie de 80"
    assert pers2.to_string() == "Charles-Edouard a une énergie de 50"
    assert pers3.to_string() == "Larry a une énergie de 0"
    
    print("Tests réussis!")
