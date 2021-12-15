from Algo import Algo
from Lecture import Lecture
from Ecriture import Ecriture
import time

start = time.time()

l = Lecture()
l.lecture_donnee(1)
print("Quantité de nombre à traiter :          ",l.N)
print("Quntité de boite à créer :              ",l.B)
print("Quantité d'emplacement dans les boite : ",l.E)
print(l.nbrs)

a = Algo(l.N,l.B,l.E,l.nbrs)

a.Variable_neighborhood(a.balanced_solution(),10000,a.basic_moove,a.moove_from_max,a.inverse_moove,a.transposition_moove,a.random_moove)
#a.simalated_annealing(a.bestCode,a.basic_moove,a.random_moove,100,0.1,100,0.99)

e = Ecriture()
e.ecriture_donnee(a,"instance1")
print(a)


end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.2}ms')