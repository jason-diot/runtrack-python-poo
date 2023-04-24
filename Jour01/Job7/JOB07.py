class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Le constructeur de la classe prend trois arguments : le titre du livre, l'auteur et le nombre de pages
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        
    def get_titre(self):
        # Cette méthode permet d'obtenir le titre du livre
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        # Cette méthode permet de modifier le titre du livre
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        # Cette méthode permet d'obtenir l'auteur du livre
        return self.__auteur
    
    def set_auteur(self, nouvel_auteur):
        # Cette méthode permet de modifier l'auteur du livre
        self.__auteur = nouvel_auteur
    
    def get_nb_pages(self):
        # Cette méthode permet d'obtenir le nombre de pages du livre
        return self.__nb_pages
    
    def set_nb_pages(self, nouveau_nb_pages):
        # Cette méthode permet de modifier le nombre de pages du livre
        # Si la valeur passée en paramètre est un entier positif, on l'assigne à l'attribut __nb_pages
        # Sinon, on affiche un message d'erreur
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur: le nombre de pages doit être un entier positif.")
    
    def __str__(self):
        # Cette méthode permet de renvoyer une chaîne de caractères qui représente le livre sous la forme "titre, écrit par auteur, nb_pages pages"
        return f"{self.__titre}, écrit par {self.__auteur}, {self.__nb_pages} pages"

# Créer une instance de la classe Livre avec un titre, un auteur et un nombre de pages donnés
livre1 = Livre("One Piece", "Eiichirō Oda", 215)

# Afficher le livre à l'aide de la méthode __str__()
print(livre1) 

# Modifier le nombre de pages du livre
livre1.set_nb_pages(302) 

# Afficher le livre modifié à l'aide de la méthode __str__()
print(livre1) 

# Essayer de modifier le nombre de pages du livre avec une valeur non valide
livre1.set_nb_pages(60.3)  

# Afficher le livre à nouveau (inchangé car la modification n'a pas eu lieu)
print(livre1) 
