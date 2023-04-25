# Définition de la classe Personne
class Personne:
    def __init__(self, age=14):  # Constructeur avec un âge par défaut de 14 ans
        self.age = age           # Attribut âge
    
    def afficherAge(self):       # Méthode pour afficher l'âge
        print("Age :", self.age)
    
    def bonjour(self):           # Méthode pour saluer
        print("Bonjour")
    
    def modifierAge(self, nouvel_age):  # Méthode pour modifier l'âge
        self.age = nouvel_age


# Définition de la classe Eleve qui hérite de Personne
class Eleve(Personne):
    def __init__(self):
        super().__init__()     # Appel du constructeur de la classe parente
    
    def allerEnCours(self):    # Méthode pour dire qu'il va en cours
        print("Je vais en cours")
    
    def affichageAge(self):    # Méthode pour afficher l'âge
        print("J'ai", self.age, "ans")


# Définition de la classe Professeur qui hérite de Personne
class Professeur(Personne):
    def __init__(self, matiereEnseignee):  # Constructeur avec une matière enseignée
        super().__init__()                # Appel du constructeur de la classe parente
        self.__matiereEnseignee = matiereEnseignee  # Attribut matière enseignée
    
    def enseigner(self):        # Méthode pour enseigner
        print("Le cours va commencer")


# Instanciation d'une Personne et d'un Eleve
personne1 = Personne()         # Création d'une instance de la classe Personne avec l'âge par défaut
eleve1 = Eleve()               # Création d'une instance de la classe Eleve

# Affichage de l'âge de l'élève par défaut
eleve1.modifierAge(15)         # Modification de l'âge de l'élève
eleve1.affichageAge()          # Affichage de l'âge de l'élève

# Instanciation d'un élève
eleve1 = Eleve()               # Création d'une nouvelle instance de la classe Eleve

# Dire bonjour à l'élève et le faire aller en cours
eleve1.bonjour()               # Appel de la méthode bonjour de la classe Eleve
eleve1.allerEnCours()          # Appel de la méthode allerEnCours de la classe Eleve

# Instanciation d'un professeur
prof1 = Professeur("Mathématiques")  # Création d'une instance de la classe Professeur avec une matière enseignée
prof1.modifierAge(40)                # Modification de l'âge du professeur

# Dire bonjour au professeur et commencer le cours
prof1.bonjour()               # Appel de la méthode bonjour de la classe Professeur
prof1.enseigner()             # Appel de la méthode enseigner de la classe Professeur
