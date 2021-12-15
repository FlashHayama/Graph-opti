from Algo import Algo
from Tri import Tri
class Ecriture:
    def __init__(self) -> None:
        pass

    def ecriture_donnee(self,a,name):
        file = open("challenge/Groupe1-" + name + ".txt","w")
        result = a.__str__()
        file.write(result)
        file.close()