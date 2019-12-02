package solver;

import model.State;

import java.util.ArrayList;
import java.util.Collections;

public class GeneticAlgorithm {
    private int population;
    private State initialState;
    private int crossover;
    private int dimension;
    private ArrayList<int []> environment;

    public GeneticAlgorithm(int population, State initialState, int crossover, int dimension) {
        this.population = population;
        this.initialState = initialState;
        this.crossover = crossover;
        this.dimension = dimension;
        environment = new ArrayList<>(population);
    }

    private int getUtility(int [] board){
        State temp = new State(board);
        return temp.getCost();
    }

    private void generatePopulation(){

    }

    private ArrayList<int []> crossOver(int [] a,int [] b){
        int [] a1 = new int[dimension];
        int [] b1 = new int[dimension];
        ArrayList<int []> temp = new ArrayList<>();
        for (int i = 0; i < dimension; i++) {
            if(i<crossover){
                a1[i]=a[i];
                b1[i] =b[i];
            }else{
                a1[i]=b[i];
                b1[i]=a[i];
            }
        }
        temp.add(a1);
        temp.add(b1);
        return temp;
    }


    private ArrayList<int []> mutation(int [] a,int [] b){
        int [] a1 = new int[dimension];
        int [] b1 = new int[dimension];
        ArrayList<int []> temp = new ArrayList<>();
        //Some Approches
        temp.add(a1);
        temp.add(b1);
        Collections.shuffle(Collections.singletonList(a));
        return temp;
    }

    private void updateEnvironment(){

    }
    private ArrayList<Integer> arrtoList(int [] a){
        ArrayList<Integer> temp = new ArrayList<>(dimension);
        for (int i = 0; i < dimension; i++) {
            temp.add(a[i]);
        }
    return temp;
    }

}
