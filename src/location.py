# from client import Client
# from vehicule import Vehicule
# from datetime import date
# from date import Date

# class Location:
#     def __init__(self, date_debut :'date', date_fin:'date', vehicule,client):
#         self.date_debut = date_debut
#         self.date_fin = date_fin
#         self.vehicule = vehicule
#         self.client=client
#         self.vehicule.louer()
    
#     def duree(self):
#         return self.date_debut.difference(self.date_fin)
    
#     def calcul_prix(self):
#         return self.duree() * 50

#     def afficher(self):
#         return f"Bonjour {self.client}, Vous avez louez un {self.vehicule} du {self.date_debut} au {self.date_fin} ce qui vous fera {self.calcul_prix} euro"
    
     

class Location:
    def __init__(self, client, vehicule, date_debut, date_fin):
        self.client = client
        self.vehicule = vehicule
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.vehicule.louer()

    def duree(self):
        return self.date_debut.difference(self.date_fin)

    def afficher(self):
        print("Location :")
        print(self.client.infos())
        print(self.vehicule.afficher_info())
        print("Du", self.date_debut.to_string(), "au", self.date_fin.to_string())

    @staticmethod
    def calcul_prix(nb_jours):
        return 50 * nb_jours

