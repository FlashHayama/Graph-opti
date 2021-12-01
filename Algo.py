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
        self.bestSol = 0
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
        self.matDiv = []
        for i in range(self.N):
            self.matDiv.append([])
            d = self.nbrs[i] // self.code[i]
            r = self.nbrs[i] % self.code[i]
            for j in range(self.code[i]):
                self.matDiv[i].append(d)
                if r > 0:
                    self.matDiv[i][j] += 1
                    r -=1
        pass

    def calc_solution(self):
        self.division()
        t = Tri()
        tab = t.fusion(self.matDiv)
        sol = 0
        for i in range(self.B):
            sol += tab[i*self.E]
        return sol

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
        iter = 100
        coeff = 0.9
        self.random_solution()
        solAccepted = self.calc_solution()
        self.bestSol = solAccepted

        while TC > TF:
            self.random_moove()
            tempSol = self.calc_solution()
            for i in range(iter):
                self.moove1(1,1)
                tempSol = self.calc_solution()
                if tempSol < self.bestSol:
                    self.bestSol = tempSol
                if tempSol < solAccepted:
                    solAccepted = tempSol
                elif tempSol > solAccepted:
                    P = math.exp(-((tempSol - solAccepted)/TC))
                    probAccept = random.random()
                    if P > probAccept:
                        solAccepted = tempSol
            TC *= coeff
            print(self.bestSol)