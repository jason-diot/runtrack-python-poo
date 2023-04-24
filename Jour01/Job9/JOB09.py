# Définition de la classe Student
class Student:
    
    # Constructeur de la classe Student, qui prend en entrée le nom, le prénom, le numéro d'étudiant et un crédit initial
    def __init__(self, nom, prenom, num_etudiant, credit=0):
        self.__nom = nom             # Attribut "nom" de l'étudiant, privé pour empêcher une modification directe
        self.__prenom = prenom       # Attribut "prenom" de l'étudiant, privé pour empêcher une modification directe
        self.__num_etudiant = num_etudiant   # Attribut "num_etudiant" de l'étudiant, privé pour empêcher une modification directe
        self.__credit = credit       # Attribut "credit" de l'étudiant, qui représente le nombre de crédits obtenus
        self.__level = self.__studentEval()  # Attribut "level" de l'étudiant, qui représente son niveau selon les crédits obtenus
    
    # Méthode "add_credits" pour ajouter des crédits à l'étudiant, qui prend en entrée le nombre de crédits à ajouter
    def add_credits(self, credit):
        if credit > 0:               # Vérifie que le nombre de crédits ajouté est positif
            self.__credit += credit  # Ajoute le nombre de crédits à l'attribut "credit" de l'étudiant
            self.__level = self.__studentEval()  # Met à jour l'attribut "level" de l'étudiant selon les crédits obtenus
    
    # Méthode privée "__studentEval" pour déterminer le niveau de l'étudiant en fonction du nombre de crédits obtenus
    def __studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    # Méthode "studentInfo" pour afficher les informations de l'étudiant
    def studentInfo(self):
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Numéro d'étudiant:", self.__num_etudiant)
        print("Niveau:", self.__level)

# Instanciation de l'objet "John Doe" de la classe Student avec des arguments pour les attributs nom, prénom et numéro d'étudiant
john_doe = Student("Doe", "John", 145)

# Ajout des crédits à l'étudiant "John Doe"
john_doe.add_credits(15)
john_doe.add_credits(35)
john_doe.add_credits(20)

# Affichage des informations de l'étudiant "John Doe"
john_doe.studentInfo()

