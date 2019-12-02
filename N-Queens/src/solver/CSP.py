from copy import deepcopy
from random import choice
from time import time


class Backtracking:
    def __init__(self,size):
        self.d=size
        self.board=self.createBoard(size)
        self.solution = list()
        self.domains=self.initialDomains(size)
        self.queens=list()
        self.isGoal=False
        self.stackDomains=list()
        self.runningTime=0
        self.steps=0


    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def start(self):
        start = time()
        col=0
        count=0
        self.stackDomains.append(self.domains)
        while not self.isGoal:
            print(self.stackDomains[len(self.stackDomains)-1],col)
            if col ==self.d:
                self.isGoal=True
                break
            if not self.isDanger():
                y = choice(self.stackDomains[len(self.stackDomains)-1][col])
                temp = deepcopy(self.domains)
                newD = self.updateDomains(y, col,temp)
                self.stackDomains.append(newD)
                col+=1
                count+=1
            else:
                self.stackDomains.pop()
                col-=1
                while len(self.stackDomains[len(self.stackDomains) -1][col])<=1:
                    col-=1
                    self.stackDomains.pop()
                self.domains = self.stackDomains[len(self.stackDomains) -1]
                y = choice(self.domains[col])
                dtemp=deepcopy(self.domains)
                newD = self.updateDomains(y, col,dtemp)
                self.stackDomains.append(newD)
                col+=1
                count+=1
        end = time()
        self.runningTime=end-start
        self.steps=count
        for k,v in self.domains.items():
            self.solution.append(v[0])
        self.report()




    def initialDomains(self, size):
        temp=dict()
        for i in range(size):
            temp[i]=list(range(size))
        return temp

    def updateDomains(self, ival, col, temp1):
        temp1[col]=[ival]
        for i in range(col+1,self.d):
            d = deepcopy(temp1[i])
            for j in d:
                if j == ival:
                    temp1[i].remove(j)
                if abs(j-ival) == abs(col-i):
                    temp1[i].remove(j)
        self.domains=temp1
        return temp1

    def isDanger(self):
        for i in range(len(self.domains)):
            if len(self.domains[i]) == 0:
                return True
        return False
    def report(self):
        print("Running Time : ",self.runningTime,"s");
        print("Number of steps : ",self.steps);
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
