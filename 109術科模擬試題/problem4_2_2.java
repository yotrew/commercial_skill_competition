import java.util.*;
import java.lang.*;

public class problem4_2_2 {
	
	public static void main(String[] args) {
		final Comparator<int[]> arrayComparator = new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				/*obj1 > obj2 if x > 0.
				obj1 < obj2 if x < 0.
				obj1 equals obj2 if x = 0.
				*/
				if(o1[3]<o2[3])
					return 1;	
				else
					return -1;
				
			}
		};
	
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
		int[][] score=new int[50][4];
		for(int i=0;i<n;i++){
			in1 = scanner.nextLine();
			String[] x=in1.split(" ");
			score[i][0]=Integer.parseInt(x[0]);
			score[i][1]=Integer.parseInt(x[1]);
			score[i][2]=Integer.parseInt(x[2]);
			score[i][3]=score[i][1]*100000+score[i][2]*100+(100-score[i][0]);
		}
		Arrays.sort(score,0,n, arrayComparator);
		for(int i=0;i<n;i++){
			System.out.println(score[i][0]+" "+score[i][1]+" "+score[i][2]);
		}

	}
}
