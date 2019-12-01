from time import time
from random import randint as rand, shuffle

from src.model.State import State


class HC:
    def __init__(self,initialState):
        self.d=len(initialState.board)
        self.initialstate =initialState
        self.initialBoard=initialState.board
        self.solutions = list()
        self.runningTime = 0
        self.expandedNodes = 0
        self.steps=0
        self.randSolution = None
        self.isFound=False
    def start(self):
        if(self.initialstate.cost ==0):
            self.report()
            return
        start = time()
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
        index = rand(0,len(self.solutions))
        self.randSolution=self.solutions[index]
        end = time()
        self.runningTime=end-start
        self.expandedNodes=(self.d)*(self.d-1)
        tempBoard=self.initialBoard
        self.steps=((self.randSolution[1]) * (self.d - 1)) + (abs(self.randSolution[0]-tempBoard[self.randSolution[1]]))
        tempBoard[self.randSolution[1]]=self.randSolution[0]
        self.report(tempBoard)
    def report(self,board):
        print("Running Time : ", self.runningTime, "s");
        print("Number of steps : ", self.steps);
        print("Number of Expanded Nodes : ", self.expandedNodes);
        print("The Solution >> ", board)
        print("The Final State\n")
        self.constructBoard(board)
        print("= = = = = = = = = = = = = = = = = = = =");

    def constructBoard(self,board):
        finalBoard=list()
        for i in range(0, len(board)):
            temp = ['#'] * self.d
            finalBoard.append(temp)
        for i in range(0, len(board)):
            finalBoard[board[i]][i]='Q'
        for i in range(0, len(board)):
            print(finalBoard[i])

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
        pass