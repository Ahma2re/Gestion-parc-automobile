from vehicule import Voiture, Camion
from client import Client
from date import Date
from location import Location
from parc_auto import ParcAuto

# Création du parc et véhicules
parc = ParcAuto()
v1 = Voiture("Mercedes", "GLE 400", 2024, 4)
v2 = Camion("Renault", "Master", 2018, 3.5)
v3 = Voiture("BMW", "X7", 2024, 4)
parc.ajouter_vehicule(v1)
parc.ajouter_vehicule(v2)
parc.ajouter_vehicule(v3)

# Clients
c1 = Client("Yuyu", 1)
c2 = Client("Big Dave",2)

# Dates
d1 = Date(10, 5, 2025)
dr1 = Date(15, 5, 2025)

d2 = Date(10, 5, 2025)
dr2 = Date(12, 6, 2025)
# Location
loc1 = Location(c1,v1,d1,dr1)
loc1.afficher()
print("Prix :", Location.calcul_prix(loc1.duree()), "€")

loc2 = Location(c2,v2,d2,dr2)
loc2.afficher()
print("Prix :", Location.calcul_prix(loc2.duree()), "€")

#Liste de vehicules
voitures = parc.lister_voitures()
print("\nVéhicules du parking :")
for voiture in voitures:
    print(voiture.afficher_info())

# Véhicules disponibles
disponibles = parc.lister_dispo()
print("\nVéhicules disponibles :")
for vehicule in disponibles:
    print(vehicule.afficher_info())

# Recherche par modèle
modele_recherche = "X7"
resultat = parc.rechercher(modele_recherche)
print(f"\nRecherche du modèle '{modele_recherche}':")
for vehicule in resultat:
    print(vehicule.afficher_info())


#Rendre voiture
v2.rendre()

# Apres retour des véhicules disponibles
disponibles = parc.lister_dispo()
print("\nVéhicules disponibles Now :")
for vehicule in disponibles:
    print(vehicule.afficher_info())

