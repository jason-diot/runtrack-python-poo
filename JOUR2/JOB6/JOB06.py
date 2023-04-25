class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("Année:", self.annee)
        print("Prix:", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes:", self.portes)

    def demarrer(self):
        print("Je démarre la voiture")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues:", self.roue)

    def demarrer(self):
        print("Je démarre la moto")

# Instanciation d'un objet Voiture
ma_voiture = Voiture("Renault", 2010, 5000)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

# Instanciation d'un objet Moto
ma_moto = Moto("Yamaha", 2015, 3000)
ma_moto.informationsVehicule()
ma_moto.demarrer()
