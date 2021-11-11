import java.util.*;
import java.lang.*;
class Node{
		int data=0;
		Node l=null;
		Node r=null;
	}
public class L2_Linklist {
	
	static ArrayList<Integer> tr;//trversal
	public static void postfix(Node node){
		if(node.l!=null)//#L
			postfix(node.l);
		if(node.r!=null)//R
			postfix(node.r);
		tr.add(node.data); //D
	}
    
		
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n =Integer.parseInt( scanner.nextLine());
		Node root;
		for(int i=0;i<n;i++){
			int node_cnt =Integer.parseInt( scanner.nextLine());
			String[] x=scanner.nextLine().split(",");
			tr=new ArrayList<Integer>();
			root=null;
			for(int b=0;b<x.length;b++){
				int a=Integer.parseInt(x[b]);
				Node node=root;
				//System.out.println(a);
				while(true){
					if(root==null){
						root=new Node();
						root.data=a;
						break;
					}
					if(a>node.data){
						if(node.r!=null){
							node=node.r;
						}else{         
							node.r=new Node();
							node.r.data=a;
							break;
						}
					}
					else{
						if(node.l!=null){
							node=node.l;
						}else{
							node.l=new Node();
							node.l.data=a;
							break;
						}
					}
				}
			}
			/*for(int []c:tree){//print Tree
				System.out.println(c[0]+","+c[1]+","+c[2]+","+c[3]);
			}*/
			//System.out.println(d[y.length][x.length]);
			postfix(root);//trversal-postfix
			for(int a=0;a<tr.size()-1;a++){
				System.out.print(tr.get(a)+" ");
			}
			System.out.println(tr.get(tr.size()-1));//last one
		}

	}
}
