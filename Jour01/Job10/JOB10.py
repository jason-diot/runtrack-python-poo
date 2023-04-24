# Définition de la classe Voiture
class Voiture:
    
    # Initialisation des attributs de la voiture
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50  # capacité maximale du réservoir de carburant en litres
    
    # Méthodes getter et setter pour l'attribut "marque"
    def get_marque(self):
        return self.marque
    
    def set_marque(self, marque):
        self.marque = marque
    
    # Méthodes getter et setter pour l'attribut "modele"
    def get_modele(self):
        return self.modele
    
    def set_modele(self, modele):
        self.modele = modele
    
    # Méthodes getter et setter pour l'attribut "annee"
    def get_annee(self):
        return self.annee
    
    def set_annee(self, annee):
        self.annee = annee
    
    # Méthodes getter et setter pour l'attribut "kilometrage"
    def get_kilometrage(self):
        return self.kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage
    
    # Méthode getter pour l'attribut "en_marche"
    def get_en_marche(self):
        return self.en_marche
    
    # Méthode setter pour l'attribut "en_marche"
    def set_en_marche(self, en_marche):
        self.en_marche = en_marche
    
    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.verifier_plein():  # si le réservoir est suffisamment plein pour démarrer
            self.en_marche = True  # la voiture démarre
        else:  # sinon
            print("Le réservoir est presque vide. Faites le plein avant de démarrer.")  # afficher un message d'erreur
    
    # Méthode pour arrêter la voiture
    def arreter(self):
        self.en_marche = False  # mettre l'attribut "en_marche" à False pour arrêter la voiture
    
    # Méthode pour vérifier si le réservoir est suffisamment plein pour démarrer
    def verifier_plein(self):
        return self.reservoir > 5  # renvoyer True si le réservoir contient plus de 5 litres d'essence
    
# Exemples d'utilisation de la classe Voiture
ma_voiture = Voiture("Renault", "Clio", 2010, 100000)  # création d'une instance de la classe Voiture avec les valeurs données
print(ma_voiture.get_marque())  # Affiche "Renault"
ma_voiture.set_kilometrage(110000)  # modification de l'attribut "kilometrage"
print(ma_voiture.get_kilometrage())  # Affiche 110000
ma_voiture.demarrer()  # Affiche "Le réservoir est presque vide. Faites le plein avant de démarrer."
ma_voiture.reservoir = 25  # modification de l
ma_voiture.demarrer()  # La voiture démarre
print(ma_voiture.get_en_marche())  # Affiche True
ma_voiture.arreter()
print(ma_voiture.get_en_marche())  # Affiche False
