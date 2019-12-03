# N-Queens
**Overview**
The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. thus, a solution requires that no two queens share the same row, column, or diagonal.

Example:







**Project Structure**

├── model
│   ├── State.py
├── solvers
│   ├── CSP.py
│   ├── Genetic Algorithm.py
│   ├── HillClimbing.py
│   ├── KBeam.py
├── test
│   ├──Sample_Input.txt
├── utils
│   ├──Reader
└── Main.py 

**Models and Utils**
*Reader :*
Use it to read sample input file to get initalBoard.we can represent a 8-queen sol in a 2 dimension list filled with 0 and then, fill it with 8 ones representing the position of the queen. A better and simpler representation is that a list of length 8. Each index specifies a column of the board. The value of each index is between 0 and 7 representing the the row of a queen in a column.

*State:*
Take the board as we described in Reader and holding all required info about the board like he cost of this board by using two methods:




**Algorithms**

*Hill Climbing*
Start : Looping on all cells and compute cost in each one then select the best solution.
Restart: change the initial state in case of algorithm stucks in local optima .

*K-Beam* 
GenerateBoards: generate k random boards.
selectTheBest: get the best K solutions.
Addsolutions: add the best solutions of each successor. 


*Genetic Algorithm*
InitializeEnvironment: get P random solutions where P is the population size.
checkGoal: check if the solution with cost equals zero exists in the environment.
Crossover: make the crossover operation between two chromosomes
Mutation : using many approaches for mutation and select one of them randomly.
updateEnvironment: set the environment to the new chromosomes.


* CSP
initialDomains: create the valid domain for each variable.
updateDomains: after assignment of any variable we need to update the domains of neighbours.
isDanger: if our path may lead to wrong answer.
updateVisits:  to track the visited nodes after each assignment.
Allvisited: check if all successors of this node is visited or not.
Choice: choose the assignment that may not lead to the wrong answer.





**Sample runs**

*Hill Climbing*

To start Hill climbing algorithms we need to set parameters
hc = HC(initialSate,Dimension,False) #using initial State, Dimension of board,to restart algorithm till solve set True









* K-Beam *


To start K-Beam algorithm we need 2 values
k = Beam(K,Dimension) #parameters: value of K, Dimension of board (Hint:random start)
Start algorithm with K=8 and Dimension = 8












* Genetic Algorithm

To start genetic algorithm 
ga = GA(500,Dimension,3) #parameters: population size , Dimension of board, crossover (Hint:random start)

Start algorithm with population size =500 and Dimension = 8 and crossover =3







* CSP

To start CSP we just need to pass Dimension
csp = Backtracking(Dimension)#parameters: Dimension of board (Hint:random start)











**Notes**
- Green queen means this queen is not attacking any other queen
- In genetic algorithms it may stuck because mutation doesn’t provide new solution we tried to solve this problem by adding many approaches for mutation and select one randomly.
In K-Beam algorithm for K>100 it may lead to a solution. 
