import java.util.*;
import java.lang.*;
public class K {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
		for(int i=0;i<n;i++){
			in1 = scanner.nextLine();
			in2 = scanner.nextLine();
			String[] x=in1.split("");
			String[] y=in2.split("");
			//System.out.println(y.length);
			int[][] d=new int[y.length+1][x.length+1];
			
			for(int a=0;a<y.length;a++){
				for(int b=0;b<x.length;b++){
					if(y[a].compareTo(x[b])==0)
						d[a+1][b+1]=d[a][b]+1;
					else
						d[a+1][b+1]=Math.max(d[a+1][b],d[a][b+1]);
				}
			}
			System.out.println(d[y.length][x.length]);
		}

	}
}
