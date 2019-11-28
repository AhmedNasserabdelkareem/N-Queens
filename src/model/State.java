package model;

public class State {

    private int ROWS, COLUMNS;
    private int [][] board;


    public State (int[][] board){
        this.board = board;
        ROWS = board.length;
        COLUMNS = board[0].length;
    }

    public int[][] getBoard(){
        return this.board;
    }

    public void showBoard(){
        System.out.println("Board");
        System.out.println("-----");
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLUMNS; j++) {
                System.out.printf(this.board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}