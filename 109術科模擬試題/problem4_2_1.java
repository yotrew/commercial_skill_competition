import java.util.*;
import java.lang.*;

public class problem4_2_1 {
	
	public static void main(String[] args) {
		final Comparator<int[]> arrayComparator = new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				/*obj1 > obj2 if x > 0.
				obj1 < obj2 if x < 0.
				obj1 equals obj2 if x = 0.
				*/
				if(o1[1]<o2[1])
					return 1;
				else if(o1[1]>o2[1])
					return -1;
				else{
					if(o1[2]<o2[2])
						return 1;
					else if(o1[2]>o2[2])
						return -1;
					else{
						if(o1[0]>o2[0])
							return 1;
						else if(o1[0]<o2[0])
							return -1;
						else{
							return 0;
						}
					}
				}
				
				
			}
		};
	
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
		int[][] score=new int[50][3];
		for(int i=0;i<n;i++){
			in1 = scanner.nextLine();
			String[] x=in1.split(" ");
			score[i][0]=Integer.parseInt(x[0]);
			score[i][1]=Integer.parseInt(x[1]);
			score[i][2]=Integer.parseInt(x[2]);
		}
		Arrays.sort(score,0,n, arrayComparator);
		for(int i=0;i<n;i++){
			System.out.println(score[i][0]+" "+score[i][1]+" "+score[i][2]);
		}

	}
}
