# Définition de la classe "Operation"
class Operation:
    # Initialisation de la classe avec la méthode spéciale "__init__"
    def __init__(self):
        # Définition de l'attribut "nombre1" initialisé avec une chaîne vide
        self.nombre1 = ""
        # Définition de l'attribut "nombre2" initialisé avec une chaîne vide
        self.nombre2 = ""

# Création d'une variable "nombre" qui référence la classe "Operation"
# Cette ligne ne crée pas une instance de la classe "Operation"
# mais plutôt une référence à la classe elle-même
nombre = Operation

# Pour créer une instance de la classe "Operation", il faudrait plutôt écrire :
# instance = Operation()
# Cette ligne créerait un nouvel objet de la classe "Operation" et l'assignerait à la variable "instance"
