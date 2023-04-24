class Personne:
    def __init__(self, nom1, nom2, prenom1, prenom2):
        # Initialisation des attributs nom1, nom2, prenom1 et prenom2 avec les valeurs passées en paramètres
        self.prenom1 = prenom1
        self.prenom2 = prenom2
        self.nom1 = nom1
        self.nom2 = nom2

    def Sepresenter(self):
        # Affichage des phrases de présentation avec les valeurs des attributs prenom1, nom1 et prenom2, nom2 de l'instance courante
        print("Je suis", self.prenom1, self.nom1)
        print("Je suis", self.prenom2, self.nom2)

# Création d'une instance de la classe Personne avec les valeurs "Doe", "Dupond", "John" et "Jean" passées en paramètres
personne = Personne("Doe", "Dupond", "John", "Jean")

# Appel de la méthode Sepresenter() sur l'instance personne, ce qui affiche les phrases de présentation avec les valeurs des attributs prenom1, nom1 et prenom2, nom2 de l'instance personne
personne.Sepresenter()

