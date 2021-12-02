import math
import random
from Tri import Tri

class Algo:

    def __init__(self,N,B,E,nbrs):
        self.N = N
        self.B = B
        self.E = E
        self.nbrs = nbrs
        self.bestCode = [None] * self.N
        self.bestSol = 0
        self.BestMatDiv = []

    def get_last_max_in_code(self,code) -> int:
        """ return last occurence of max
        """
        max = 0
        for i in range(self.N):
            if code[i] >= code[max]:
                max = i
        return max

    def division(self,code) -> list:
        tempMatDiv = []
        for i in range(self.N):
            tempMatDiv.append([])
            d = self.nbrs[i] // code[i]
            r = self.nbrs[i] % code[i]
            for j in range(code[i]):
                tempMatDiv[i].append(d)
                if r > 0:
                    tempMatDiv[i][j] += 1
                    r -=1
        return tempMatDiv
        

    def calc_solution(self,code) -> tuple:
        matDiv = self.division(code)
        t = Tri()
        tab = t.fusion(matDiv)
        sol = 0
        for i in range(self.B):
            sol += tab[i*self.E]
        return sol,matDiv

    def random_solution(self) -> list:
        code = self.bestCode[:]
        BE = (self.B * self.E)
        for i in range(self.N):
            r = random.randint(1,(BE // self.N) + (self.N // 2))
            code[i] = r
        if sum(code) > BE:
            dif = sum(code) - BE
            for j in range(dif):
                code[code.index(max(code))] -= 1
        elif(sum(code) < BE):
            dif = BE - sum(code)
            for j in range(dif):
                code[code.index(min(code))] += 1
        return code

    def random_moove(self,code) -> list:
        tempCode = code[:]
        randIndexDown = random.randint(0,self.N - 1)
        while tempCode[randIndexDown] == 1:
            randIndexDown = random.randint(0,self.N - 1)
        randMoove = random.randint(1,tempCode[randIndexDown] - 1)
        randIndexUp = random.randint(0,self.N - 1)
        while randIndexUp == randIndexDown:
            randIndexUp = random.randint(0, self.N - 1)

        tempCode[randIndexDown] -= randMoove
        tempCode[randIndexUp] += randMoove
        return tempCode

    def moove1(self, code, step, m):
        """ Max to next index from step
        """
        tempCode = code[:]
        max = self.get_last_max_in_code(tempCode)
        next = max + step
        if next >= self.N: next -= self.N
        if tempCode[max] > m:
            tempCode[max] -= m
            tempCode[next] += m
        else :
            n = tempCode[max] - 1
            tempCode[max] -= n
            tempCode[next] += n
        return tempCode

    def simalated_annealing(self):
        matDiv = []
        T0 = 1000
        TF = 0.1
        TC = T0
        iter = 100
        coeff = 0.99
        code = self.random_solution()
        solAccepted,matDiv = self.calc_solution(code)
        self.bestSol = solAccepted

        while TC > TF:
            code = self.random_moove(code)
            tempSol,matDiv = self.calc_solution(code)
            for i in range(iter):
                code = self.moove1(code,1,1)
                tempSol,matDiv = self.calc_solution(code)
                if tempSol < self.bestSol:
                    self.bestSol = tempSol
                    self.bestCode = code[:]
                    self.BestMatDiv = matDiv[:]
                if tempSol < solAccepted:
                    solAccepted = tempSol
                elif tempSol > solAccepted:
                    P = math.exp(-((tempSol - solAccepted)/TC))
                    probAccept = random.random()
                    if P > probAccept:
                        solAccepted = tempSol
            TC *= coeff
            print(self.bestSol)

    def __str__(self):
        pass