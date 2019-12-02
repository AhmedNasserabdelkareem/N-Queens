from copy import deepcopy
from random import shuffle
from time import time

from src.model.State import State
from src.solver.HillClimping import HC
from termcolor import colored



class Beam:
    def __init__(self,k,dimension):
        self.K=k
        self.d=dimension
        self.board=list()
        self.allSolutions=list()
        self.bestSolutions=list()
        self.minCost=list()
        self.runningTime = 0
        self.expandedNodes = 0
        self.steps = 0
    def start(self):
        start=time()
        self.generateBoards()
        for i in range(self.K):
            state=State(self.board[i])
            solver=HC(state,False)
            solver.start()
            self.steps+=solver.steps
            self.expandedNodes+=solver.expandedNodes
            self.addSolutions(self.board[i],solver.solutions)
        self.selectThebest()
        end=time()
        self.runningTime=end-start



    def generateBoards(self):
        for i in range(self.d):
            temp= list(range(self.d))
            shuffle(temp)
            while temp in self.board:
                shuffle(temp)
            self.board.append(temp)

    def selectThebest(self):
        costs = list()
        for sol in self.allSolutions:

            state=State(sol)
            costs.append(state.cost)
        while len(self.bestSolutions) < self.K:
            minCost = min(costs)
            minIndex = costs.index(minCost)
            self.minCost.append(costs[minIndex])
            self.bestSolutions.append(self.allSolutions[minIndex])
            costs.remove(minCost)
            self.allSolutions.remove(self.allSolutions[minIndex])

    def addSolutions(self, param, solutions):
        for i in range(len(solutions)):
            tempBoard=deepcopy(param)
            tempBoard[solutions[i][1]]=solutions[i][0]
            self.allSolutions.append(tempBoard)

    def report(self):
        print("Running Time : ", self.runningTime, "s")
        print("Number of steps : ", self.steps)
        print("Number of Expanded Nodes : ", self.expandedNodes)
        print("Best Solutions")

        for i in range(len(self.bestSolutions)):
            print("The Solution >> ", self.bestSolutions[i],"With Cost",self.minCost[i])
            print("The Final State\n")
            self.constructBoard(self.bestSolutions[i])
            print("= = = = = = = = = = = = = = = = = = = =")

    def constructBoard(self,board):
        finalBoard=list()
        for i in range(0, len(board)):
            temp = ['#'] * self.d
            finalBoard.append(temp)
        for i in range(0, len(board)):
            finalBoard[board[i]][i]='Q'

        for i in range(0, len(board)):
            for j in range(len(finalBoard[i])):
                if finalBoard[i][j] =='Q':
                    print(colored(finalBoard[i][j],self.getColor(j,board)),end=" ")
                else:
                    print(finalBoard[i][j],end=" ")
            print()

    def getColor(self,j,board):
        for col in range(len(board)):
            if col!=j:
                if self.isThreaten(board[j],j,board[col],col):
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


