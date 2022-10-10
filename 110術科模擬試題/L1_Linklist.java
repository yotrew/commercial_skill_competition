/*
#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 1：輸出二元樹的後序拜訪的結果。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210711
#110商業技藝競賽模擬試題
#Problem L 二元樹的前序拜訪/二元樹的後序拜訪
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
*/
import java.util.*;
import java.lang.*;
class Node{
		int data=0;
		Node l=null;
		Node r=null;
	}
public class L1_Linklist {
	
	static ArrayList<Integer> tr;//trversal
	public static void prefix(Node node){
		tr.add(node.data); //D
		if(node.l!=null)//#L
			prefix(node.l);
		if(node.r!=null)//R
			prefix(node.r);
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
			prefix(root);//trversal-prefix
			for(int a=0;a<tr.size()-1;a++){
				System.out.print(tr.get(a)+" ");
			}
			System.out.println(tr.get(tr.size()-1));//last one
		}

	}
}
