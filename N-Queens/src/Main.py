from src.model.State import State
from src.solver.CSP import Backtracking
from src.solver.HillClimping import HC
from src.solver.KBeam import Beam
from src.utils.Reader import Reader
from src.solver.GeneticAlgorithm import GA
Dimension = 8
r = Reader('test/Sample_Input.txt')
board = r.readFile()
initialSate=State(board)
# ga = GA(500,Dimension,3)
# ga.start()
# hc = HC(initialSate,True)
# hc.start()
# csp = Backtracking(Dimension)
# csp.start()
k = Beam(8,Dimension)
k.start()
k.report()