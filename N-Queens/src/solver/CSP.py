from copy import deepcopy
from random import choice
from time import time

from termcolor import colored


class Backtracking:
    def __init__(self,size):
        self.d=size
        self.solution = list()
        self.domains=self.initialDomains(size)
        self.queens=list()
        self.isGoal=False
        self.stackDomains=list()
        self.stackVisits=list()
        self.runningTime=0
        self.expandedNodes = 0
        self.steps=0
        self.visited=self.initialVisits(size)


    def start(self):
        start = time()
        col=0
        count=0
        self.stackDomains.append(self.domains)
        self.stackVisits.append(self.visited)
        while not self.isGoal:
            if col ==self.d:
                self.isGoal=True
                break
            if not self.isDanger():
                ypos = choice(self.stackDomains[len(self.stackDomains)-1][col])
                temp = deepcopy(self.domains)
                newD = self.updateDomains(ypos, col,temp)
                self.stackDomains.append(newD)
                self.expandedNodes+=1
                tempvisited = deepcopy(self.visited)
                newVisited = self.updatevisits(ypos,col,tempvisited)
                self.stackVisits.append(newVisited)
                col+=1
                count+=1
            else:
                self.stackDomains.pop()
                popUp=self.stackVisits.pop()
                col-=1
                self.updateVisits(popUp,col)
                index=len(self.stackVisits)-1
                checkVisit=self.allVisited(col,self.stackVisits[index],self.stackDomains[len(self.stackDomains) -1])
                checkLength=len(self.stackDomains[len(self.stackDomains) -1][col])<=1
                while checkLength or checkVisit:
                    col-=1
                    self.stackDomains.pop()
                    popDown=self.stackVisits.pop()
                    self.updateVisits(popDown, col)
                    index = len(self.stackVisits) - 1
                    checkVisit = self.allVisited(col, self.stackVisits[index],self.stackDomains[len(self.stackDomains) - 1])
                    checkLength = len(self.stackDomains[len(self.stackDomains) - 1][col]) <= 1
                self.domains = self.stackDomains[len(self.stackDomains) -1]
                self.visited=self.stackVisits[len(self.stackVisits) -1]
                yneg = self.choice(col)
                dtemp=deepcopy(self.domains)
                newD = self.updateDomains(yneg, col,dtemp)
                self.stackDomains.append(newD)
                visitsTemp=deepcopy(self.visited)
                newvisits = self.updatevisits(yneg, col,visitsTemp)
                self.stackVisits.append(newvisits)
                col+=1
                count+=1
        end = time()
        self.runningTime=end-start
        self.steps=count
        for k,v in self.domains.items():
            self.solution.append(v[0])




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
        print("Running Time : ",self.runningTime,"s")
        print("Number of steps : ",self.steps)
        print("Number of Expanded Nodes : ",self.expandedNodes)
        print("The Solution >> ",self.solution)
        print("The Final State\n")
        self.constructBoard()
        print("= = = = = = = = = = = = = = = = = = = =")

    def constructBoard(self):
        for i in range(0,len(self.solution)):
            temp = ['#'] * self.d
            index = self.solution.index(i)
            temp[index]='Q'
            for j in range(len(temp)):
                if temp[j] == 'Q':
                    print(colored(temp[j], self.getColor(j,self.solution)), end=" ")
                else:
                    print(temp[j], end=" ")
            print()

    def initialVisits(self, size):
        temp = dict()
        for i in range(size):
            temp[i] = [False] * size
        return temp

    def updatevisits(self, ypos, col, tempvisited):
        tempvisited[col][ypos]=True
        self.visited=tempvisited
        return tempvisited

    def allVisited(self, col, o, o1):
        count=0
        for i in o1[col]:
            if o[col][i]:
                count+=1
        if count == len(o1[col]):
            return True
        return False

    def updateVisits(self, popUp, col):
        self.stackVisits[len(self.stackVisits)-1][col]=popUp[col]

    def choice(self, col):
        for i in self.domains[col]:
            if self.visited[col][i]==False:
                return i

    def getColor(self, j, board):
        for col in range(len(board)):
            if col != j:
                if self.isThreaten(board[j], j, board[col], col):
                    return "red"

        return "green"

    def isThreaten(self, i, param, j, param1):
        if i == j:
            return True
        if param == param1:
            return True
        if abs(i - j) == abs(param1 - param):
            return True
        return False



