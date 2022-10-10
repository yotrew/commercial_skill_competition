/*
/*
https://github.com/yotrew/commercial_skill_competition
*/
*/
import java.lang.*;
import java.io.Console;
public class A1{
    public static void main(String args[]){
        String input = System.console().readLine();
        while( input!= null){
            String[] split = input.split(" ");
            int w=0;
            w=Integer.parseInt(split[0])*24+14*Integer.parseInt(split[1])+6*Integer.parseInt(split[2]);
            System.out.println(w);
            input=System.console().readLine();
        }
        
    }
}