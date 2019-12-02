from time import time
from random import randint as rand, shuffle

from termcolor import colored

from src.model.State import State


class HC:
    def __init__(self,initialState,dimension,restart):
        self.d=len(initialState.board)
        self.initialstate =initialState
        self.initialBoard=initialState.board
        self.solutions = list()
        self.d=dimension
        self.runningTime = 0
        self.expandedNodes = 0
        self.board=list()
        self.steps=0
        self.randSolution = None
        self.isFound=False
        self.option=restart
    def start(self):
        if self.initialstate.cost ==0:
            self.solutions.append(self.initialstate.board)
            self.steps=0
            self.runningTime=0
            self.expandedNodes=0
            self.board=self.initialstate.board
            #self.report(self.initialstate.board)
            return
        start = time()
        if self.option:
            while not self.isFound:
                BestCost = self.d * self.d
                for i in range(0,self.d):
                    for j in range(0,self.d-1):
                        tempBoard=self.copyBoard()
                        tempBoard[i]= (tempBoard[i] + j + 1)% self.d
                        tempState = State(tempBoard)
                        if(tempState.cost<BestCost):
                            BestCost=tempState.cost
                            self.solutions.clear()
                            self.solutions.append([tempBoard[i],i,BestCost])
                        elif tempState.cost == BestCost:
                            self.solutions.append([tempBoard[i],i,BestCost])
                        if (BestCost == 0):
                            self.isFound =True
                if len(self.solutions) >0:
                    index = rand(0, len(self.solutions)-1)
                    self.randSolution = self.solutions[index]
                print(self.initialBoard,">>",self.randSolution,">>",BestCost)
                self.restart()
            index = rand(0, len(self.solutions))
            self.randSolution = self.solutions[index]
        else:
            BestCost = self.d * self.d
            for i in range(0, self.d):
                for j in range(0, self.d - 1):
                    tempBoard = self.copyBoard()
                    tempBoard[i] = (tempBoard[i] + j + 1) % self.d
                    tempState = State(tempBoard)
                    if (tempState.cost < BestCost):
                        BestCost = tempState.cost
                        self.solutions.clear()
                        self.solutions.append([tempBoard[i], i, BestCost])
                    elif tempState.cost == BestCost:
                        self.solutions.append([tempBoard[i], i, BestCost])
            if len(self.solutions) > 0:
                index = rand(0, len(self.solutions) - 1)
                self.randSolution = self.solutions[index]

        end = time()
        self.runningTime=end-start
        self.expandedNodes=(self.d)*(self.d-1)
        tempBoard=self.initialBoard
        self.steps=((self.randSolution[1]) * (self.d - 1)) + (abs(self.randSolution[0]-tempBoard[self.randSolution[1]]))
        tempBoard[self.randSolution[1]]=self.randSolution[0]
        self.board=tempBoard
        #self.report(tempBoard)
    def report(self):
        print("Running Time : ", self.runningTime, "s")
        print("Number of steps : ", self.steps)
        print("Number of Expanded Nodes : ", self.expandedNodes)
        print("The Solution >> ", self.board)
        print("The Final State\n")
        self.constructBoard(self.board)
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


    def copyBoard(self):
        temp = list()
        for i in self.initialBoard:
            temp.append(i)
        return temp

    def restart(self):
        self.solutions=list()
        self.randSolution=None
        self.initialBoard = list(range(self.d))
        shuffle(self.initialBoard)
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
