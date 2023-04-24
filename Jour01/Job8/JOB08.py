class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Initialise les attributs du livre : titre, auteur, nombre de pages et disponibilité
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
        
    def get_titre(self):
        # Retourne le titre du livre
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        # Modifie le titre du livre
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        # Retourne l'auteur du livre
        return self.__auteur
    
    def set_auteur(self, nouvel_auteur):
        # Modifie l'auteur du livre
        self.__auteur = nouvel_auteur
    
    def get_nb_pages(self):
        # Retourne le nombre de pages du livre
        return self.__nb_pages
    
    def set_nb_pages(self, nouveau_nb_pages):
        # Modifie le nombre de pages du livre
        self.__nb_pages = nouveau_nb_pages
    
    def verification(self):
        # Vérifie si le livre est disponible
        return self.__disponible
    
    def emprunter(self):
        # Emprunte le livre si il est disponible
        if self.verification():
            self.__disponible = False
            print("Le livre {} a été emprunté.".format(self.__titre))
        else:
            print("Le livre {} n'est pas disponible.".format(self.__titre))
    
    def rendre(self):
        # Rend le livre si il n'est pas disponible
        if not self.verification():
            self.__disponible = True
            print("Le livre {} a été rendu.".format(self.__titre))
        else:
            print("Le livre {} n'a pas été emprunté.".format(self.__titre))

# Exemple d'utilisation de la classe Livre
livre1 = Livre("One piece", "Eiichirō Oda", 1000)

# Emprunte le livre
livre1.emprunter() 

# Rend le livre
livre1.rendre()

# Essaye de rendre le livre à nouveau
livre1.rendre()
