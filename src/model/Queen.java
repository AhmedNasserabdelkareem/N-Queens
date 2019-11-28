package model;


public class Queen {
    public Queen(int id, int x,int y) {
        this.id = id;
        this.x = x;
        this.y=y;
    }

    public int getId() {
        return id;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    private int id;

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    private int x;
    private int y;
}
