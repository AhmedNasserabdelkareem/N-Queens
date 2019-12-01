from random import shuffle
from random import randint as rand
from time import time

from src.model.State import State


class GA:
    def __init__(self,population, dimension, crossover):
        self.generationNumber = 1
        self.pSize=population
        self.d=dimension
        self.co=crossover
        self.environment=list()
        self.solved=False
        self.solution=None
        self.un=list()
        self.minCosts = list()
        self.runningTime=0
        self.expandedNodes=population

    def start(self):
        start = time()
        self.initializeEnvironmnt()
        self.checkGoal()
        while not self.solved:
            self.generationNumber+=1
            chroms=self.crossOver()
            self.updateEnvironment()
            self.checkGoal()
        end=time()
        self.runningTime=end-start
        if len(self.un)!=0:
            self.expandedNodes = len(self.un)
        self.report()





    def initializeEnvironmnt(self):
        for i in range(self.pSize):
            chrom = list(range(self.d))
            shuffle(chrom)
            while chrom in self.environment:
                shuffle(chrom)
            self.environment.append(chrom)

    def checkGoal(self):
        for chrom in self.environment:
            state=State(chrom)
            #print(chrom,">>",state.cost,">>",len(self.un),">>",self.generationNumber)
            if(state.cost==0):
                self.solved = True
                self.solution=chrom

    def crossOver(self):
        for i in range(0,len(self.environment)-1,2):
            chrom1 = self.environment[i][:]
            chrom2 = self.environment[i+1][:]
            chromo1=chrom1[0:self.co]+chrom2[self.co:]
            chromo2=chrom2[0:self.co]+chrom1[self.co:]
            self.mutant(chromo1)
            self.mutant(chromo2)

    def mutant(self, param):
        bound = self.d // 2
        leftIndex = rand(0, bound)
        RightIndex = rand(bound + 1, self.d - 1)
        newGen = []
        for dna in param:
            if dna not in newGen:
                newGen.append(dna)
        for i in range(self.d):
            if i not in newGen:
                newGen.append(i)
        gen = newGen
        gen[leftIndex] = gen[RightIndex]
        gen[RightIndex] = gen[leftIndex]
        self.environment.append(gen)

    def updateEnvironment(self):
        for chrom in self.environment:
            if chrom not in self.un:
                self.un.append(chrom)
        self.minCosts=list()
        costs = list()
        newEnvironment = list()
        for chrom in self.environment:
            state=State(chrom)
            costs.append(state.cost)
        if min(costs) == 0:
            self.solution = costs.index(min(costs))
            self.goal = self.environment[self.solution]
            return self.environment
        while len(newEnvironment) < self.d:
            minCost = min(costs)
            minIndex = costs.index(minCost)
            self.minCosts.append(costs[minIndex])
            newEnvironment.append(self.environment[minIndex])
            costs.remove(minCost)
            self.environment.remove(self.environment[minIndex])
        self.environment=newEnvironment
        print(self.minCosts,">>",len(self.un))

    def report(self):
        print("Running Time : ",self.runningTime,"s");
        print("Number of generations : ",self.generationNumber);
        print("Number of Expanded Nodes : ",self.expandedNodes);
        print("The Solution >> ",self.solution)
        print("The Final State\n")
        self.constructBoard()
        print("= = = = = = = = = = = = = = = = = = = =");

    def constructBoard(self):
        for i in range(0,len(self.solution)):
            temp = ['#'] * self.d
            index = self.solution.index(i)
            temp[index]='Q'
            print(temp)




