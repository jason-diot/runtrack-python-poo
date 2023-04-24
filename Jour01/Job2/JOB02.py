# Définition de la classe "Operation"
class Operation:
    # Initialisation de la classe avec la méthode spéciale "__init__"
    def __init__(self):
        # Définition de l'attribut "nombre1" initialisé avec une chaîne vide
        self.nombre1 = ""
        # Définition de l'attribut "nombre2" initialisé avec une chaîne vide
        self.nombre2 = ""

# Création d'une instance de la classe "Operation" en appelant le constructeur avec la syntaxe "Operation()"
# Cette instance est assignée à la variable "nombre"
nombre = Operation()

# Modification de l'attribut "nombre1" de l'instance "nombre" en lui assignant la valeur 12
nombre.nombre1 = 12
# Modification de l'attribut "nombre2" de l'instance "nombre" en lui assignant la valeur 3
nombre.nombre2 = 3

# Affichage des valeurs des attributs "nombre1" et "nombre2" de l'instance "nombre" avec la fonction "print"
print("nombre1 est", nombre.nombre1)
print("nombre2 est", nombre.nombre2)
