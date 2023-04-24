# Définition de la classe Animal
class Animal:
    # Constructeur de la classe Animal
    def __init__(self):
        # Initialisation des attributs age et prenom
        self.age=0
        self.prenom=""

    # Définition de la méthode vieillir qui incrémente l'attribut age de l'instance courante
    def vieillir(self): 
        self.age += 1

    # Définition de la méthode nommer qui prend un argument prenom et affecte sa valeur à l'attribut prenom de l'instance courante
    def nommer(self,prenom):
        self.prenom= prenom

# Création d'une instance de la classe Animal et assignation à la variable animal
animal = Animal()

# Affichage de l'âge initial de l'animal (0)
print("L'Âge de l'animal", animal.age)

# Appel de la méthode vieillir sur l'instance animal pour augmenter son âge de 1
animal.vieillir()
# Affichage de la nouvelle valeur de l'âge de l'animal (1)
print("L'Âge de l'animal", animal.age)

# Appel de la méthode nommer sur l'instance animal pour lui donner le prénom "Luna"
animal.nommer("Luna")
# Affichage du prénom de l'animal ("Luna")
print("L'animal se nomme", animal.prenom)


