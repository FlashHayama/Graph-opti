from Algo import Algo
from Lecture import Lecture


l = Lecture()
l.lecture_donnee(10)
print(l.N)
print(l.B)
print(l.E)
print(l.nbrs)

a = Algo(l.N,l.B,l.E,l.nbrs)
a.simalated_annealing()
print(a.code)
print(a.matDiv)
print(a.bestSol)