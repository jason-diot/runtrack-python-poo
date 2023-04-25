# Définition de la classe "Personne"
class Personne:
    # Constructeur avec un âge par défaut de 14 ans
    def __init__(self, age=14):
        self.age = age
    
    # Méthode pour afficher l'âge de la personne
    def afficherAge(self):
        print("Age :", self.age)
    
    # Méthode pour dire bonjour
    def bonjour(self):
        print("Hello")
    
    # Méthode pour modifier l'âge de la personne
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


# Définition de la classe "Eleve", qui hérite de "Personne"
class Eleve(Personne):
    # Constructeur, qui appelle le constructeur de la classe "Personne" avec l'âge par défaut
    def __init__(self):
        super().__init__()
    
    # Méthode pour dire qu'on va en cours
    def allerEnCours(self):
        print("Je vais en cours")
    
    # Méthode pour afficher l'âge de l'élève
    def affichageAge(self):
        print("J'ai", self.age, "ans")


# Définition de la classe "Professeur", qui hérite également de "Personne"
class Professeur(Personne):
    # Constructeur, qui appelle le constructeur de la classe "Personne" avec l'âge par défaut,
    # et qui prend un argument supplémentaire pour la matière enseignée
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
    
    # Méthode pour dire qu'on va enseigner
    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une Personne avec l'âge par défaut
personne1 = Personne()

# Instanciation d'un Eleve sans spécifier d'âge, donc avec l'âge par défaut
eleve1 = Eleve()

# Affichage de l'âge de l'élève
eleve1.affichageAge()
