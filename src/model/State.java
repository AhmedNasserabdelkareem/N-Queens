package model;

public class State {

    private int Dimension;
    private Queen [] board;
    private int cost;


    public State (Queen[] board){
        this.board = board;
        Dimension = board.length;
        this.cost=computeCost();
    }

    public Queen[] getBoard(){
        return this.board;
    }

    public void showBoard(){
        System.out.println("Board");
        System.out.println("-----");
        for (int i = 0; i < Dimension; i++) {
                System.out.printf("("+this.board[i].getX() + ","+this.board[i].getY()+")");

        }
        System.out.printf(" Cost = "+cost);
        System.out.println();
    }

    private int getCost(){
        return cost;
    }
    private int computeCost(){
        int cost=0;
        for(int i=0;i<Dimension;i++){
            for (int j=i+1;j<Dimension;j++){
                if(isThreaten(board[i],board[j])){
                    cost+=1;
                }
            }
        }
        return cost;
    }

    private boolean isThreaten(Queen a, Queen b) {
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