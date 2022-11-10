#111商業技藝競賽模擬試題
#Problem #E2 迷宮
#同 108商業技藝競賽正式試題-Problem 4： 子題 2：數字迷宮
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
#Ref:https://www.larrysprognotes.com/UVa-929/
#UVa-929
'''
Dijkstra最短路徑+Priority queue
Python使用最小堆積來模擬Priority queue
*接近TLE版-因為有時會TLE,有時候會Correct
'''
import heapq
import sys

ntime=int(input())
inf=(1000000)*9 #定義無限大步數,最多999*999,每格最大為9
#from math import inf
direct=(0,1,0,-1,0) #一個格子4個方向
#0,1往下
#1,0往右
#0,-1往上
#-1,0往左


for i in range(ntime):
    m=int(sys.stdin.readline().strip())
    n=int(sys.stdin.readline().strip())
    matrix=[]
    m_l=range(m+1)
    n_l=range(n+1)
    for j in m_l[0:-1]:
        matrix.append(list(map(int,sys.stdin.readline().strip().split(" "))))
    
    values=[[inf for a in n_l] for b in m_l]
    visisted=[[False for a in n_l] for b in m_l]
        
    values[0][0]=matrix[0][0]
    pq=[]
    heapq.heappush(pq,[values[0][0],0,0])

    while pq:
        value,row,col=heapq.heappop(pq)
        visisted[row][col]=True

        for c in range(4):
            n_col,n_row=col+direct[c],row+direct[c+1]
            if n_col<0 or n_row<0 or n_col>=n or n_row>=m or visisted[n_row][n_col]:
                continue
            val=value+matrix[n_row][n_col]

            if values[n_row][n_col]>val:
                values[n_row][n_col]=val
                heapq.heappush(pq,[val,n_row,n_col])
    sys.stdout.write(f"{values[m-1][n-1]}\n")

 
