from Algo import Algo
from Tri import Tri
class Ecriture:
    def __init__(self) -> None:
        pass

    def ecriture_donnee(self,a):
        file = open("challenge/GroupeG1.txt","w")
        for i in range(a.N):
            file.write(str(i+1)+"\t"+str(a.nbrs[i])+"\t"+str(a.bestCode[i])+"\t")
            for j in range(a.bestCode[i]):
                file.write(str(a.BestMatDiv[i][j])+" ")

            file.write("\n")
        t = Tri()
        tabTrie = t.fusion(a.BestMatDiv)
        for iterB in range(a.B):
            file.write("B"+str(iterB+1)+"\t")
           
            file.write(str(tabTrie[a.E*iterB])+"\n")

        file.write("COST  "+str(a.bestSol))
        file.close()