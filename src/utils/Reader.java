package utils;

import model.Queen;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Reader {
    public Reader(String fileName,int dimension) {
        this.fileName = fileName;
        this.d = dimension;
    }

    private String fileName;
    private int d;
    public int [] read(){
        BufferedReader reader;
        int count=0;
        int rows = 0;
        int[] board = new int[d];
        try {
            reader = new BufferedReader(new FileReader(fileName));
            String line = reader.readLine();
            while (line != null) {
                String [] temp = line.split(" ");
                for (int i=0;i<d;i++){
                    if(temp[i].compareTo("Q")==0) {
                        board[count] = i+1;
                        count++;
                    }
                }
                rows++;
                line = reader.readLine();
            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return board;
    }

}
