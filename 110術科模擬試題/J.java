//https://github.com/yotrew/commercial_skill_competition
import java.util.*;
import java.lang.*;
public class J {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int a,b,d;
		while(scanner.hasNext()){
			String[] ch1=scanner.nextLine().split(" ");
			a=Integer.parseInt(ch1[0]);
			b=Integer.parseInt(ch1[1]);
			
			ArrayList<Integer> c= new ArrayList<Integer>();
			for(int i=1;i<(a+1);i++){
				c.add(i);
			}
			b=b-1;
			d=b;
			while(c.size()>1){
				if(d >= c.size()){
					d=d%c.size();
				}
				c.remove(d);
				d+=b;
			}
            
			System.out.println(c.get(0));
		}
		//System.out.println(d[y.length][x.length]);
	}
}
