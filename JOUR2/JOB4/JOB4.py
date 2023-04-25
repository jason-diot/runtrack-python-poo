# Définition de la classe parent Forme
class Forme:
    # Méthode qui renvoie une valeur par défaut de zéro pour l'aire
    def aire(self):
        return 0

# Définition de la sous-classe Rectangle qui hérite de la classe parent Forme
class Rectangle(Forme):
    # Initialisation de la classe Rectangle avec une largeur et une hauteur
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    # Redéfinition de la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

# Création d'une instance de Rectangle avec une largeur de 5 et une hauteur de 10
mon_rectangle = Rectangle(5, 10)

# Appel de la méthode aire de l'instance de Rectangle pour calculer l'aire
print(mon_rectangle.aire())  # sortie: 50
