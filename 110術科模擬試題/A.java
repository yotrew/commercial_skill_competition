import java.util.*;

public class A {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;// = scanner.nextLine();
		
		String[] split;
		while(scanner.hasNext()){
			input = scanner.nextLine();
			//System.out.println(input);
			split = input.split(" ");
			int w=0;
            w=Integer.parseInt(split[0])*24+14*Integer.parseInt(split[1])+6*Integer.parseInt(split[2]);
            System.out.println(w);
		}	
	}
}
