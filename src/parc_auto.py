from vehicule import Vehicule

class ParcAuto:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self,v):
        self.vehicules.append(v)
    
    def lister_dispo(self):
        return [v for v in self.vehicules if v.est_dispo()]
    
    def rechercher(self,modele):
        return [v for v in self.vehicules if v._modele.lower() == modele.lower()]
    
    def lister_voitures(self):
        return [v for v in self.vehicules if isinstance(v, Vehicule)]
