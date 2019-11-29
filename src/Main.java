import model.Queen;
import model.State;
import solver.HillClimbing;
import utils.Reader;

public class Main {
    public static void main(String[] args) {
        Reader r = new Reader("src/test/Sample_Input.txt",8);
        //int[] initialBoard = r.read();
        int [] initialBoard ={3,2,0,6,1,7,5,3};
        State initialState = new State(initialBoard);
        initialState.showBoard();
        HillClimbing h = new HillClimbing(initialState);
        h.showResults();
    }
}
