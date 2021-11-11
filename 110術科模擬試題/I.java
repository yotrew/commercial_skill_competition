import java.util.*;
public class I {
	public static void main(String[] args) {
		int a,b,c,d;
		Scanner scanner = new Scanner(System.in);
		String[] ch1;
		while(scanner.hasNext()){
			ch1=scanner.nextLine().split(" ");	
			a=Integer.parseInt(ch1[0]);
			b=Integer.parseInt(ch1[1]);
			c=Integer.parseInt(ch1[2]);
			d=Integer.parseInt(ch1[3]);
			if(b!=c)
				break;
			int[][] AB=new int[a][d];
			int[][] A=new int[a][b];
			int[][] B=new int[b][d];
			int[] tmp=new int[a*b+b*d];
			int cnt=0;
			//System.out.println(a+":"+b+":"+c+":"+d);
			while (cnt<(a*b+b*d)){
				ch1=scanner.nextLine().split(" ");
				for(int j=0;j<ch1.length;j++)
				{
					if(ch1[j].trim().length()==0) //測資數字和數字之間可能有2個以上的空白ex.3  4
						continue;
					tmp[cnt++]=Integer.parseInt(ch1[j]);
				}
			}
			cnt=0;
			for(int i=0;i<a;i++){
				for(int j=0;j<b;j++)
					A[i][j]=tmp[cnt++];
			}
			for(int i=0;i<b;i++){
				for(int j=0;j<d;j++)
					B[i][j]=tmp[cnt++];
			}
			for(int i=0;i<a;i++)
				for(int j=0;j<d;j++)
					for(int k=0;k<b;k++)
						AB[i][j]+=A[i][k]*B[k][j];

			for(int i=0;i<a;i++){
				for(int j=0;j<(d-1);j++)        
					System.out.print(AB[i][j]+" ");
				System.out.println(AB[i][d-1]);
            }
		}
		
	}
}
