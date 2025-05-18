from datetime import date

class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def to_string(self):
        return f"{self.jour}/{self.mois}/{self.annee}"

    def difference(self, autre: 'Date')->int:
        d1 = date(self.annee, self.mois, self.jour)
        d2 = date(autre.annee, autre.mois, autre.jour)
        return abs((d1 - d2).days)
