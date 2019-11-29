package model;

import java.awt.*;

public class State {

    public int getDimension() {
        return Dimension;
    }

    private int Dimension;
    private int [] board;
    private int cost;


    public State (int[] board){
        this.board = board;
        Dimension = board.length;
        this.cost=computeCost();
    }

    public int[] getBoard(){
        return this.board;
    }

    public void showBoard(){
        System.out.println("Board");
        System.out.println("-----");
        for (int i = 0; i < Dimension; i++) {
                System.out.printf(String.valueOf(board[i]));

        }
        System.out.printf(" Cost = "+cost);
        System.out.println();
    }

    public int getCost(){
        return cost;
    }
    private int computeCost(){
        int cost=0;
        for(int i=0;i<Dimension;i++){
            for (int j=i+1;j<Dimension;j++){
                if(isThreaten(new Point(i,board[i]),new Point(j,board[j]))){
                    cost+=1;
                }
            }
        }
        return cost;
    }

    private boolean isThreaten(Point a, Point b) {
        if(a.getX()==b.getX()){
            return true;
        }
        if(a.getY()==b.getY()){
            return true;
        }
        if(Math.abs(a.getX()-b.getX())==Math.abs(a.getY()-b.getY())){
            return true;
        }
        return false;
    }

}