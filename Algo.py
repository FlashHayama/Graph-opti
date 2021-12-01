import math
import random
from Tri import Tri

class Algo:

    def __init__(self,N,B,E,nbrs):
        self.N = N
        self.B = B
        self.E = E
        self.nbrs = nbrs
        self.code = [None] * self.N
        self.bestSol = math.inf
        self.matDiv = []

    def get_last_max_in_code(self) -> int:
        """ return last occurence of max
        """
        max = 0
        for i in range(self.N):
            if self.code[i] >= self.code[max]:
                max = i
        return max

    def division(self):
        pass

    def calc_solution(self):
        t = Tri()
        tab = t.fusion(self.matDiv)
        sol = 0
        for i in range(self.B):
            sol += tab[i*self.E]
        print(sol)

    def random_solution(self):
        BE = (self.B * self.E)
        for i in range(self.N):
            r = random.randint(1,(BE // self.N) + (self.N // 2))
            self.code[i] = r
        if sum(self.code) > BE:
            dif = sum(self.code) - BE
            for j in range(dif):
                self.code[self.code.index(max(self.code))] -= 1
        elif(sum(self.code) < BE):
            dif = BE - sum(self.code)
            for j in range(dif):
                self.code[self.code.index(min(self.code))] += 1
        print(self.code)
        print(sum(self.code))

    def random_moove(self):
        randIndexDown = random.randint(0,self.N - 1)
        while self.code[randIndexDown] == 1:
            randIndexDown = random.randint(0,self.N - 1)
        randMoove = random.randint(1,self.code[randIndexDown] - 1)
        randIndexUp = random.randint(0,self.N - 1)
        while randIndexUp == randIndexDown:
            randIndexUp = random.randint(0, self.N - 1)

        self.code[randIndexDown] -= randMoove
        self.code[randIndexUp] += randMoove
        
        print(randIndexDown)
        print(randIndexUp)
        print(randMoove)
        print(self.code)

    def moove1(self, step, m):
        """ Max to next index from step
        """
        max = self.get_last_max_in_code()
        next = max + step
        if next >= self.N: next -= self.N
        if self.code[max] > m:
            self.code[max] -= m
            self.code[next] += m
        else :
            n = self.code[max] - 1
            self.code[max] -= n
            self.code[next] += n

    def simalated_annealing(self):
        T0 = 100
        TF = 0.1
        TC = T0
        iter = 10
        coeff = 0.9
        self.random_solution()
        solAccepted = self.calc_solution()

        while TC > TF:
            for i in range(iter):
                self.random_moove()
                tempSol = self.calc_solution()

                if tempSol > self.bestSol:
                    self.bestSol = tempSol
                if tempSol > solAccepted:
                    solAccepted = tempSol
                elif tempSol < solAccepted:
                    P = math.exp(-((solAccepted - tempSol)/TC))
                    probAccept = random.random()
                    if P > probAccept:
                        solAccepted = tempSol
            TC *= coeff

a = Algo(10,3,10,{})
"""a.matDiv = [
    [2430, 2430, 2240, 560],
    [2430,2430,2430],
    [2430,2430,2180],
    [2430,2240,2220],
    [2430,2240,610,580],
    [2240,2240,610],
    [2430,2210],
    [2240,610,610,370],
    [2240,610,610],
    [580]
]
a.calc_solution()"""
a.random_solution()
a.moove1(4)
print(a.code)