from personnage import Personnage


class Guerrier(Personnage):
    """
    Classe représentant un Guerrier. Hérite de Personnage.
    Attributes:
        force_defaut (int): La valeur par défaut de la force
        force_max (int): La valeur maximum de la force
        perte_force_defaut (int): La perte de force lors d'une attaque
        gain_force_defaut (int): Le gain de force lors d'une resitution d'énergie
        force (int): La force courante du guerrier
    """
    def __init__(self, nom, energie_depart, energie_courante, force):
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB: pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie_courante(int): L'énergie courante du guerrier
            force (int): La force du guerrier 
        """
        super().__init__(nom, energie_depart)
        # la ligne 26 peut être omise puisqu'elle n'a aucune utilité
        self.force_defaut = 20
        self.force_max = 80
        self.perte_force_defaut = 2
        self.gain_force_defaut = 10
        # Bien que les consignes indiquent que l'attribut force = 0, il ne s'agit que d'une borne inférieure
        self.force = force
        
    def to_string(self):
        """
        Retourne une chaîne du genre: "Le guerrier, nom de Personnage, a une énergie de valeur de
        l’énergie et une force de valeur de la force."

        Returns (str): La chaîne représentant le guerrier.
        """
        return "Le guerrier " + super().to_string() + " et une force de {}.".format(self.force)

    def valider_force(self, force):
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """
        return 0 <= force <= self.force_max

    def crier(self):
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """
        return "Vous allez goûter à la puissance de mon épée!"

    def attaquer(self, force_attaque):
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """
        if force_attaque >= self.energie_courante:
            self.energie_courante = 0
            self.force = 0
        else:
            self.energie_courante -= force_attaque
            if self.force != 0:
                self.force -= self.perte_force_defaut


    def reset_energie(self):
        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """
        self.energie_courante = self.energie_depart
        if self.force <= self.force_max and (self.force + self.gain_force_defaut) <= self.force_max:
            self.force += self.gain_force_defaut
        else:
            self.force = self.force_max

    def get_force(self):
        """
        Retourne la force du guerrier.
        Returns (int): La force du guerrier.

        """
        return self.force

    def set_force(self, nb_force):
        """
        Assigne la force du guerrier. La force doit être valide.
        Args:
            nb_force (int): La nouvelle valeur de force

        Returns (bool): True si le nombre de forces est valide et a été modifié, False sinon.
        """
        if self.valider_force(nb_force):
            self.force = nb_force
            return True
        else:
            return False


if __name__ == '__main__':
    guer1 = Guerrier("Max", 20, 20, 20)
    guer2 = Guerrier("Miko", 5, 100, 81)
    guer3 = Guerrier("Mike", 10, 90, 50)
    print()
    print("Tests unitaires en cours...")
    print()
    
    assert type(guer1) == Guerrier

    assert guer1.to_string() == "Le guerrier Max a une énergie de 20 et une force de 20."

    assert guer1.valider_force(guer1.force)
    assert not guer2.valider_force(guer2.force)
    assert guer3.valider_force(guer3.force)

    assert guer1.crier() == "Vous allez goûter à la puissance de mon épée!"

    guer1.attaquer(20)
    assert guer1.force == 0
    assert guer1.energie_courante == 0

    guer1.reset_energie()
    assert guer1.force == 10
    assert guer1.energie_courante == 20

    assert guer1.get_force() == 10
    assert guer2.get_force() == 81
    assert guer3.get_force() == 50

    guer1.set_force(-10)
    assert guer1.force != -10
    assert guer1.force == 10

    guer1.set_force(30)
    assert guer1.force == 30

    print("Tests réussis!")
