from Algo import Algo
from Lecture import Lecture


l = Lecture()
l.lecture_donnee(10)
print("Quantité de nombre à traiter :          ",l.N)
print("Quntité de boite à créer :              ",l.B)
print("Quantité d'emplacement dans les boite : ",l.E)
print(l.nbrs)

a = Algo(l.N,l.B,l.E,l.nbrs)
a.simalated_annealing()
print(a.bestCode)
print(a.BestMatDiv)
print(a.bestSol)