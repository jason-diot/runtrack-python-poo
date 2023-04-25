# Importation de la bibliothèque math pour utiliser la constante pi
import math

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

# Définition de la sous-classe Cercle qui hérite de la classe parent Forme
class Cercle(Forme):
    # Initialisation de la classe Cercle avec un rayon
    def __init__(self, radius):
        self.radius = radius
    
    # Redéfinition de la méthode aire pour calculer l'aire du cercle
    def aire(self):
        return math.pi * self.radius ** 2

# Création d'une instance de Rectangle avec une largeur de 5 et une hauteur de 10
mon_rectangle = Rectangle(5, 10)

# Création d'une instance de Cercle avec un rayon de 10
mon_cercle = Cercle(10)

# Appel de la méthode aire de chaque instance pour calculer l'aire
print(mon_rectangle.aire())  # sortie: 50
print(mon_cercle.aire())  # sortie approximative: 314.16
