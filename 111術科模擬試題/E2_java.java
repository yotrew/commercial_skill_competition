/*
#111商業技藝競賽模擬試題
#Problem #E2 迷宮
#同 108商業技藝競賽正式試題-Problem 4： 子題 2：數字迷宮
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
#Ref:https://www.larrysprognotes.com/UVa-929/
#UVa-929
// javac -encoding utf-8 E2_java.java
*/
import java.io.*;
import java.util.*;
public class E2_java{
	static int[] direct = {0,1,0,-1,0};
	static int n,m,inf=Integer.MAX_VALUE;
	static int[][] matrix;

	public static void main(String[] args) throws Throwable {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		int times = Integer.parseInt(br.readLine().trim());
		for(int t=0;t<times;t++)
		{
			n = Integer.parseInt(br.readLine().trim());
			m = Integer.parseInt(br.readLine().trim());
			matrix = new int[n][m];
			for (int i = 0; i < n; i++) 
			{
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < m; j++) 
				{
					matrix[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			//Dijkstra
			PriorityQueue<Node> q = new PriorityQueue<Node>();
			int[][] value = new int[n][m];
			boolean [][] visisted =new boolean [n][m];
			for (int i = 0; i < value.length; i++){
				Arrays.fill(value[i], inf);
				Arrays.fill(visisted[i], false);
			}
				
			
			value[0][0] = matrix[0][0];
			q.add(new Node(0,0,value[0][0]));
			while(!q.isEmpty())
			{
				Node cur = q.poll();
				visisted[cur.x][cur.y]=true;
				
				for (int i = 0; i < 4; i++) 
				{
					int ny = cur.y + direct[i];
					int nx = cur.x + direct[i+1];
					
					
					if(!(nx<0 || ny<0 || nx>=n || ny>=m ||visisted[nx][ny]))
					{
						int val = cur.value + matrix[nx][ny];
						if(val<value[nx][ny])
						{
							value[nx][ny] = val;
							q.add(new Node(nx,ny,val));
						}
					}
				}
			}

            System.out.println(value[n-1][m-1]);
		}
	}
	static class Node implements Comparable<Node>
	{
		int x,y,value;
		public Node(int i,int j,int v)
		{
			x = i;
			y = j;
			value = v;
		}
		public int compareTo(Node o) {
			return value-o.value;
		}
	}
}