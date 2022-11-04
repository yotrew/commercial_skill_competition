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

        
    values[0][0]=matrix[0][0]
    pq=[]
    heapq.heappush(pq,[values[0][0],0,0])

    while pq:
        value,x,y=heapq.heappop(pq)

        for c in range(4):
            nx,ny=x+direct[c],y+direct[c+1]
            if nx<0 or ny<0 or nx>=n or ny>=m :#or visisted[ny][nx]==1:
                continue
            val=value+matrix[ny][nx]

            if values[ny][nx]>val:
                values[ny][nx]=val
                heapq.heappush(pq,[val,nx,ny])
    sys.stdout.write(f"{values[m-1][n-1]}\n")

 
