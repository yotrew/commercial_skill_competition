import java.util.*;
import java.lang.*;
public class L2 {
	static ArrayList<int []> tree;
	static ArrayList<Integer> tr;//trversal
	public static void postfix(int node){
		if(tree.get(node)[2]!=-1)//#L
			postfix(tree.get(node)[2]);
		if(tree.get(node)[3]!=-1)//R
			postfix(tree.get(node)[3]);
		tr.add(tree.get(node)[1]); //D
	}
    
		
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n =Integer.parseInt( scanner.nextLine());
		for(int i=0;i<n;i++){
			int node_cnt =Integer.parseInt( scanner.nextLine());
			String[] x=scanner.nextLine().split(",");
			int num=1;
			tree = new ArrayList<int []>();
			int[] tmp1= {0,Integer.parseInt(x[0]),-1,-1};
			tree.add(tmp1);
			tr=new ArrayList<Integer>();
			for(int b=1;b<x.length;b++){
				int a=Integer.parseInt(x[b]);
				int node=0;
				//System.out.println(a);
				while(true){
					//System.out.println("node:"+node);
					if(a>tree.get(node)[1]){
						if(tree.get(node)[3]!=-1){
							node=tree.get(node)[3];
						}else{         
							int[] tmp={num,a,-1,-1};
							tree.add(tmp);
							tree.get(node)[3]=num;
							num+=1;
							break;
						}
					}
					else{
						if(tree.get(node)[2]!=-1){
							node=tree.get(node)[2];
						}else{
							int[] tmp={num,a,-1,-1};						
							tree.add(tmp);
							tree.get(node)[2]=num;
							num+=1;
							break;
						}
					}
				}
			}
			/*for(int []c:tree){//print Tree
				System.out.println(c[0]+","+c[1]+","+c[2]+","+c[3]);
			}*/
			//System.out.println(d[y.length][x.length]);
			postfix(0);//trversal-postfix
			for(int a=0;a<tr.size()-1;a++){
				System.out.print(tr.get(a)+" ");
			}
			System.out.println(tr.get(tr.size()-1));//last one
		}

	}
}
