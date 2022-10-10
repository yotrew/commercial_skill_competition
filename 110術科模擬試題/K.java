/*
#107商業技藝競賽模擬試題
#Problem 4： 子題 1：最長共同子序列(Longest common subsequence)。
#按照題目給於的說明應該就可以推出規則
#因為只要輸出最長有多長,因此使用DP方式來解
#Author:Yotrew
#20210628
#https://github.com/yotrew/commercial_skill_competition
*/
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
