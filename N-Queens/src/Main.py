from src.model.State import State
from src.utils.Reader import Reader
from src.solver.GeneticAlgorithm import GA
Dimension = 8
r = Reader('test/Sample_Input.txt')
board = r.readFile()
initialSate=State(board)
ga = GA(initialSate,1000,Dimension,3)
ga.start()