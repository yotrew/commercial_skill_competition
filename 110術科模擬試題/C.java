import java.util.*;

public class C {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;// = scanner.nextLine();
		
		int tiger=0;
		int lion=0;
		while(scanner.hasNext()){
			input = scanner.nextLine();
			//System.out.println(input);
			if(input.trim().compareTo("Tiger")==0)
				tiger++;
			else
				lion++;
		}
		if (tiger>lion)
			System.out.println("Tiger");
		else
			System.out.println("Lion");
		
	}
}
