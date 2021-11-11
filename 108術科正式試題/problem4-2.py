#108商業技藝競賽正式試題
#Problem 4： 子題 2：數字迷宮
'''
題目提示使用Dijkstra,但BFS/DFS應該也可以只是會爆吧
Dijkstra???????

UVa929
https://theriseofdavid.github.io/2020/03/11/UVa/UVa929/
本題給的連結有誤
https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji/d793-acm-929-numbermaze

How to Pronounce Dijkstra
https://www.youtube.com/watch?v=lg6uIPSvclU

'''
import pprint
n=int(input())
for i in range(0,n):
    N=int(input())
    M=int(input())
    table=[]
    inf_dist=1000#因為最大值為999,就假設1000為無限大路徑
    dist=[inf_dist for a in range(0,N*M)]
	
    for a in range(0,N):
        table.append(list(map(int,input().strip().split(" "))))
    #dist[0-1]=#-1超出範圍 #向左
    if(M>1):
        dist[0+1]=table[0][1]#向右
    #dist[0-M]=table[-1][0]#向上
    if(N>1):
        dist[0+M]=table[1][0]#向下
    dist[0]=table[0][0]
    for a in range(1,len(dist)):
        l=a-1
        r=a+1
        top=a-M
        bottom=a+M
        row=int(a/M)
        col=a%M
        
        cost=table[row][col]
        costl=inf_dist
        costr=inf_dist
        costt=inf_dist
        costb=inf_dist
        if(col-1) >= 0:
            costl=cost+dist[l]
        if(col+1) < M:
            costr=cost+dist[r]
        if(row-1) >=0:
            costt=cost+dist[top]
        if(row+1)<N:
            costb=cost+dist[bottom]
        dist[a]=min(costl,costr,costt,costb)
        
        
    print(dist[-1])
    
