class Rectangle:
    def __init__(self, longueur, largeur):
        # Le constructeur de la classe prend deux arguments : la longueur et la largeur du rectangle
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        # Cette méthode permet d'obtenir la longueur du rectangle
        return self.__longueur

    def set_longueur(self, longueur):
        # Cette méthode permet de définir la longueur du rectangle
        self.__longueur = longueur

    def get_largeur(self):
        # Cette méthode permet d'obtenir la largeur du rectangle
        return self.__largeur

    def set_largeur(self, largeur):
        # Cette méthode permet de définir la largeur du rectangle
        self.__largeur = largeur

    def afficher(self):
        # Cette méthode affiche le rectangle à l'aide de tirets (-)
        for i in range(self.__largeur):
            print("-" * self.__longueur)

# Créer une instance de la classe Rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(10, 5)

# Afficher la longueur et la largeur du rectangle
print("Longueur :", mon_rectangle.get_longueur())
print("Largeur :", mon_rectangle.get_largeur())

# Afficher le rectangle à l'aide de tirets
print("Rectangle :")
mon_rectangle.afficher()

# Modifier la longueur et la largeur du rectangle
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Afficher la nouvelle longueur et largeur du rectangle
print("Longueur modifiée :", mon_rectangle.get_longueur())
print("Largeur modifiée :", mon_rectangle.get_largeur())

# Afficher le rectangle modifié à l'aide de tirets
print("Rectangle modifié :")
mon_rectangle.afficher()



    

