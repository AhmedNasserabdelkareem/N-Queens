package solver;

import model.State;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class HillClimbing {
    private int steps = 0;
    private long runningTime = 0;
    private int nodeExpanded = 0;
    private int [][] finalBoard;
    private State initialState;
    private int d;
    private HashMap<Point,Integer> dict;
    private Point solution;

    public HillClimbing(State initialState) {
        this.initialState = initialState;
        d=initialState.getDimension();
        dict= new HashMap<>();
        finalBoard=new int [d][d];
        solve();
    }

    private void solve() {
        if (initialState.getCost() == 0) {
            constructFinalBoard(initialState.getBoard());

            return;
        }
        long startTime = System.nanoTime();
        int cost, BestCost = d*d;
        int[] tempBoard;
        for (int i = 0; i < d; i++) {
            for (int j = 0; j < (d - 1); j++) {
                tempBoard = copyBoard();
                tempBoard[i] = (tempBoard[i] + j + 1) % d;
                State temp = new State(tempBoard);
                cost = temp.getCost();
                if (cost < BestCost) {
                    BestCost = cost;
                    dict.clear();
                    dict.put(new Point(tempBoard[i], i), cost);
                }else if (cost == BestCost){
                    dict.put(new Point(tempBoard[i], i), cost);
                }
            }
        }
        Boolean check = true;
        for (Map.Entry<Point, Integer> entry : dict.entrySet()) {
            if (entry.getValue() == BestCost) {
                solution = entry.getKey();
                break;
            }
        }
        long endTime = System.nanoTime();
        runningTime = (endTime - startTime) / 1000000;
        nodeExpanded = d * (d - 1);
        tempBoard = initialState.getBoard();
        steps = ((solution.y) * (d - 1)) + (Math.abs(solution.x-tempBoard[solution.y]));
        tempBoard[solution.y] = solution.x;
        constructFinalBoard(tempBoard);
    }

    private void constructFinalBoard(int[] tempBoard) {
        for (int i = 0; i < d; i++) {
            finalBoard[tempBoard[i]][i]=1;
        }
    }

    private int[] copyBoard() {
        int [] temp = new int[d];
        for (int i = 0; i <d ; i++) {
            temp[i]=initialState.getBoard()[i];
        }
        return temp;
    }

    public void showResults() {
        for (int i=0;i<d;i++){
            for (int j=0;j<d;j++){
                if (finalBoard[i][j]==1){
                    System.out.print("Q ");
                }else{
                    System.out.print("# ");
                }
            }
            System.out.println();
        }
        System.out.println("Running Time : "+runningTime+"ms");
        System.out.println("Number of steps : "+steps);
        System.out.println("Number of Expanded Nodes : "+nodeExpanded);
        System.out.println("= = = = = = = = ");
    }
}
