from Algo import Algo
from Tri import Tri
class Ecriture:
    def __init__(self) -> None:
        pass

    def ecriture_donnee(self,a):
        file = open("challenge/GroupeG1.txt","w")
        result = a.__str__()
        file.write(result)
        file.close()