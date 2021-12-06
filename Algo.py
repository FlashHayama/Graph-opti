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
        """ Search last occurence of max
        Args:
            code (list): Code of the actual solution
        
        Returns: 
            int: Last maximum of the solution
        """
        max = 0
        for i in range(self.N):
            if code[i] >= code[max]:
                max = i
        return max

    def division(self,code) -> list:
        """Divide each element of nbrs by the number in code

        Args:
            code (list): Code of the actual solution

        Returns:
            list: Matrix representing the division of numbers in nbrs
        """
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
        """Calculate the solution with a matrix send by division

        Args:
            code (list): Code of the actual solution

        Returns:
            tuple: Return solution and new matrix
        """
        matDiv = self.division(code)
        t = Tri()
        tab = t.fusion(matDiv)
        sol = 0
        for i in range(self.B):
            sol += tab[i*self.E]
        return sol,matDiv

    def random_solution(self) -> list:
        """Find a random solution for code so that the sum of the numbers makes B * E

        Returns:
            list: Code of the new solution
        """
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
    
    def balanced_solution(self):
        BE = (self.B * self.E)
        s = BE // self.N
        r = BE % self.N
        code = [s] * self.N
        for i in range(r):
            code[i] += 1
        return code
        

    def random_moove(self,code, iter = 0) -> list:
        """Randomly move on code

        Args:
            code (list): Code of the old solution

        Returns:
            list: Code of the new solution
        """
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

    def moove1(self, code, iter = 0, step = 1, m = 1) -> list:
        """Max to next index from step

        Args:
            code (list): Code of the old solution
            step (int): Number of jumps on code
            m (int): Value move to code

        Returns:
            list: Code of the new solution
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
    
    def basic_moove(self, code, iter, step = 1, m = 1) -> list:
        current = iter % self.N
        next = (current + step) % self.N
        if code[current] > m:
            code[current] -= m
            code[next] += m
        else : self.basic_moove(code,iter + 1)
        return code
    
    def inverse_moove(self, code, iter, step = 1, m = 1)-> list:
        current = iter % self.N
        next = (current + step) % self.N
        tempcode = code[current]
        code[current] = code[next]
        code[next] = tempcode
        return code
    
    def transposition_moove(self, code, iter, step = 1, m = 1)-> list:
        current = iter % self.N
        next = (current + random.randint(0,self.N-1)) % self.N
        tempcode = code[current]
        code[current] = code[next]
        code[next] = tempcode
        return code

    def simalated_annealing(self, code,intensification,diversification,T0 = 100,TF = 0.1,iter = 10,coeff = 0.9):
        """Simulated annealing metaheuristics

        Args:
            T0 (int, optional): Initial temperature. Defaults to 100.
            TF (float, optional): Final temperature. Defaults to 0.1.
            iter (int, optional): Number of iterations at constant temperature. Defaults to 10.
            coeff (float, optional): Temperature decay coefficient. Defaults to 0.9.
        """
        matDiv = []
        TC = T0
        solAccepted,matDiv = self.calc_solution(code)
        self.bestSol = solAccepted

        while TC > TF:
            code = diversification(code)
            tempSol,matDiv = self.calc_solution(code)
            for i in range(iter):
                code = intensification(code,i)
                tempSol,matDiv = self.calc_solution(code)
                if tempSol < self.bestSol:
                    self.bestSol = tempSol
                    self.bestCode = code[:]
                    self.BestMatDiv = matDiv[:]
                    print(self.bestSol)
                if tempSol < solAccepted:
                    solAccepted = tempSol
                elif tempSol > solAccepted:
                    P = math.exp(-((tempSol - solAccepted)/TC))
                    probAccept = random.random()
                    if P > probAccept:
                        solAccepted = tempSol
            TC *= coeff
            
    def Variable_neighborhood(self,code,iter = 100, *f):
        matDiv = []
        matDiv2 = []
        length = len(f)
        k = 0
        j = 0
        localSearch = f[0]
        sol,matDiv = self.calc_solution(code)
        sol2 = 0
        self.bestSol = sol
        code1 = code
        code2 = code
        for i in range(iter):
            k = 0
            while k < length:
                if k > 0 : code1 = f[k](code[:],j)
                code2 = localSearch(code1[:],j)
                j += 1
                sol,matDiv = self.calc_solution(code)
                sol2,matDiv2 = self.calc_solution(code2)
                if sol2 < sol: code = code2[:]
                else : k += 1
                if sol2 < self.bestSol:
                    self.bestSol = sol2
                    self.bestCode = code2[:]
                    self.BestMatDiv = matDiv2
                    print(self.bestSol)

    def __str__(self) -> str:
        str_Result = ""
        for i in range(self.N):
            str_Result+=(str(i+1)+"\t"+str(self.nbrs[i])+"\t"+str(self.bestCode[i])+"\t")
            for j in range(self.bestCode[i]):
                str_Result+=(str(self.BestMatDiv[i][j])+" ")

            str_Result+=("\n")
        t = Tri()
        tabTrie = t.fusion(self.BestMatDiv)
        for iterB in range(self.B):
            str_Result+=("B"+str(iterB+1)+"\t")
           
            str_Result+=(str(tabTrie[self.E*iterB])+"\n")

        str_Result+=("COST  "+str(self.bestSol))
        return str_Result
        