class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
# Instanciation de la classe Rectangle
rect = Rectangle(5, 10)

# Appel de la méthode périmètre
print("Le périmètre du rectangle est :", rect.perimetre()) # Affiche : Le périmètre du rectangle est : 30

# Appel de la méthode surface
print("La surface du rectangle est :", rect.surface()) # Affiche : La surface du rectangle est : 50

# Utilisation des accesseurs pour obtenir les valeurs des attributs
print("La longueur du rectangle est :", rect.get_longueur()) # Affiche : La longueur du rectangle est : 5
print("La largeur du rectangle est :", rect.get_largeur()) # Affiche : La largeur du rectangle est : 10

# Utilisation des mutateurs pour modifier les valeurs des attributs
rect.set_longueur(7)
rect.set_largeur(14)
print("La longueur du rectangle est maintenant de :", rect.get_longueur()) # Affiche : La longueur du rectangle est maintenant de : 7
print("La largeur du rectangle est maintenant de :", rect.get_largeur()) # Affiche : La largeur du rectangle est maintenant de : 14

# Instanciation de la classe Parallelepipede
par = Parallelepipede(3, 4, 5)

# Appel de la méthode périmètre de la classe Rectangle
print("Le périmètre du parallélépipède est :", par.perimetre()) # Affiche : Le périmètre du parallélépipède est : 14

# Appel de la méthode volume de la classe Parallelepipede
print("Le volume du parallélépipède est :", par.volume()) # Affiche : Le volume du parallélépipède est : 60

# Utilisation de l'accesseur pour obtenir la valeur de l'attribut hauteur
print("La hauteur du parallélépipède est :", par.get_hauteur()) # Affiche : La hauteur du parallélépipède est : 5

# Utilisation du mutateur pour modifier la valeur de l'attribut hauteur
par.set_hauteur(7)
print("La hauteur du parallélépipède est maintenant de :", par.get_hauteur()) # Affiche : La hauteur du parallélépipède est maintenant de : 7

