from Algo import Algo
from Lecture import Lecture
from Ecriture import Ecriture


l = Lecture()
l.lecture_donnee(3)
print("Quantité de nombre à traiter :          ",l.N)
print("Quntité de boite à créer :              ",l.B)
print("Quantité d'emplacement dans les boite : ",l.E)
print(l.nbrs)

a = Algo(l.N,l.B,l.E,l.nbrs)

#a.simalated_annealing(a.random_solution(),1000,0.1,100,0.99)
a.Variable_neighborhood(a.balanced_solution(),10000,a.basic_moove,a.inverse_moove,a.moove1,a.random_moove)

e = Ecriture()
e.ecriture_donnee(a)
print(a)