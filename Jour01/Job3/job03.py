# Définition de la classe "Operation"
class Operation:
    # Initialisation de la classe avec la méthode spéciale "__init__"
    # Cette méthode prend deux paramètres "nombre1" et "nombre2"
    def __init__(self, nombre1, nombre2):
        # Définition de l'attribut "nombre1" avec la valeur du paramètre "nombre1"
        self.nombre1 = nombre1
        # Définition de l'attribut "nombre2" avec la valeur du paramètre "nombre2"
        self.nombre2 = nombre2

    # Définition de la méthode "addition"
    def addition(self):
        # Affichage du résultat de l'addition des attributs "nombre1" et "nombre2" de l'instance courante
        print(self.nombre1 + self.nombre2)

# Création d'une instance de la classe "Operation" en appelant le constructeur avec les valeurs 12 et 3 passées en paramètres
# Cette instance est assignée à la variable "operation"
operation = Operation(12, 3)

# Appel de la méthode "addition" de l'instance "operation"
operation.addition()
