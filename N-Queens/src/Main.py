from src.model.State import State
from src.solver.CSP import Backtracking
from src.solver.HillClimping import HC
from src.solver.KBeam import Beam
from src.utils.Reader import Reader
from src.solver.GeneticAlgorithm import GA
Dimension = 8 # For N-Queen problem here N=8
r = Reader('test/Sample_Input.txt')
board = r.readFile()
initialSate=State(board)

# ga = GA(500,Dimension,3) #parameters: population size , Dimension of board, crossover (Hint:random start)
# ga.start()
# ga.report()

# hc = HC(initialSate,Dimension,False) #using initial State, Dimension of board,to restart algorithm till solve set True
# hc.start()
# hc.report()

# csp = Backtracking(Dimension)#parameters: Dimension of board (Hint:random start)
# csp.start()
# csp.report()

# k = Beam(8,Dimension) #parameters: value of K, Dimension of board (Hint:random start)
# k.start()
# k.report()
