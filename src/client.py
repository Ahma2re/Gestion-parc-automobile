
class Client:
    def __init__(self,nom,id):
        self.nom=nom
        self.id=id
    def infos(self):
        return f"Bonjour {self.nom} ton id est {self.id}"
    
        