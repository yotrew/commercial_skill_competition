//#https://github.com/yotrew/commercial_skill_competition
import java.util.*;

public class F {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
				
		for(int i=0;i<n;i++){
			int dist=0;
			in1 = scanner.nextLine();
			in2 = scanner.nextLine();
			String[] ch1=in1.split("");
			String[] ch2=in2.split("");
			for(int j=0;j<ch1.length;j++){
				if(ch1[j].compareTo(ch2[j])!=0)
					dist+=1;
			}
			System.out.println(dist);
		}
		
	}
}
