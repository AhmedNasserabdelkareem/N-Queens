class State:
    def __init__(self, initial):
        self.board = initial
        self.cost = self.computeCost()

    def computeCost(self):
        sum = 0
        for i in range(0, len(self.board)):
            for j in range(i + 1, len(self.board)):
                check = self.isThreaten(i, self.board[i], j, self.board[j])
                if check:
                    sum += 1
        return sum

    def isThreaten(self, i, param, j, param1):
        if i == j:
            return True
        if param == param1:
            return True
        if abs(i - j) == abs(param1 - param):
            return True
        return False
