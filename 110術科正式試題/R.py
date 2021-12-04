#110商業技藝競賽正式試題
#Problem R 條條⼤路通羅⾺
#Author: Yotrew Wing
#2021/12/02
'''
DFS
'''
visited=[] #為了不要把拜訪過的節點當參數傳下去所以用全域
adj=[]     #相鄰串列
flag="No"
def DFS(end_s,nxt):
    global visited,adj,flag
    
    if flag=="Yes":
            return
    for i in adj[nxt]:
        if i==end_s: #找到就退回到最前面
            flag="Yes"
            return
        if i in visited:
            continue
        else:
            visited.append(i) 
            DFS(end_s,i)
            visited.pop(-1)
    return

N,M=map(int,input().split(" "))
adj=[[] for i in range(N+1)]
    
for i in range(M):  
    a1,b1=map(int,input().split(" "))
    adj[a1].append(b1)

A,B=map(int,input().split(" "))
visited.append(A)
DFS(B,A)
print(flag)
