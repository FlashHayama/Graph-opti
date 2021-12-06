from Algo import Algo
from Lecture import Lecture
from Ecriture import Ecriture


l = Lecture()
l.lecture_donnee(1)
print("Quantité de nombre à traiter :          ",l.N)
print("Quntité de boite à créer :              ",l.B)
print("Quantité d'emplacement dans les boite : ",l.E)
print(l.nbrs)

a = Algo(l.N,l.B,l.E,l.nbrs)
a.simalated_annealing(1000,0.1,100,0.9)
print(a.bestCode)
print(a.BestMatDiv)
print(a.bestSol)

e = Ecriture()
e.ecriture_donnee(a)
print(a)