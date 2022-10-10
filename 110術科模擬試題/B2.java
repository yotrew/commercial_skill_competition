/*
#https://github.com/yotrew/commercial_skill_competition
*/
import java.util.*;

public class B2 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;// = scanner.nextLine();
		input = scanner.nextLine();
		int n=Integer.parseInt(input);
		for(int i=0;i<n;i++){
			input = scanner.nextLine();
			int year=Integer.parseInt(input);
			if(year % 400 == 0)
				System.out.println("a leap year");
			else if( year % 4 ==0 && year % 100 !=0)
				System.out.println("a leap year");
			else
				System.out.println("a normal year");
		}
		
	}
}
