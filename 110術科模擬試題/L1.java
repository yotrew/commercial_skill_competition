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
public class L1 {
	static ArrayList<int []> tree;
	static ArrayList<Integer> tr;//trversal
	public static void prefix(int node){
		tr.add(tree.get(node)[1]); //D
		if(tree.get(node)[2]!=-1)//#L
			prefix(tree.get(node)[2]);
		if(tree.get(node)[3]!=-1)//R
			prefix(tree.get(node)[3]);
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
			prefix(0);//trversal-prefix
			for(int a=0;a<tr.size()-1;a++){
				System.out.print(tr.get(a)+" ");
			}
			System.out.println(tr.get(tr.size()-1));//last one
		}

	}
}
