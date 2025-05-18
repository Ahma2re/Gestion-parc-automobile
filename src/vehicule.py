from abc import ABC, abstractmethod 

class Vehicule(ABC):
    
    def __init__(self,marque,modele,annee):
        self._marque=marque
        self._modele=modele
        self._annee=annee
        self._disponible=True

    @abstractmethod
    def afficher_info():
        pass

    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele
    
    def get_annee(self):
        return self._annee
    
    def set_marque(self,marque):
        self._marque = marque

    def set_modele(self,modele):
        self._modele = modele
    
    def set_annee(self,annee):
        self._annee = annee
    
    def louer(self):
        self._disponible = False
    def rendre(self):
        self._disponible = True
    def est_dispo(self):
        return self._disponible

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_porte):
        super().__init__(marque, modele, annee)
        self.nb_porte = nb_porte
    
    def afficher_info(self):
        dispo = "Disponible" if self.est_dispo() else "Loué"
        return f"Voiture: {self.get_marque()} {self.get_modele()} ({self.get_annee()}) - {self.nb_porte} portes - {dispo}"
    
class Camion(Vehicule):
    def __init__(self, marque, modele, annee,capacite):
        super().__init__(marque, modele, annee)
        self.capacite = capacite
    
    def afficher_info(self):
        dispo = "Disponible" if self.est_dispo() else "Loué"
        return f"Camion: {self.get_marque()} {self.get_modele()} ({self.get_annee()}) - {self.capacite}T - {dispo}"
    


    