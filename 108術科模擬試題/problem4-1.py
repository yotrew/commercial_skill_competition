#108商業技藝競賽模擬試題
#Problem 4：子題 1：樹。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210709
'''
此題要找出root和樹的高度
1.leaf連到0
2.root不是leaf也沒出現在被連到的點就是了
找出root後就由root做DFS就知道高度了
'''
visited=[]
adj=[]
height=0
def DFS(v,lv):#拜訪v點,現在深度為lv
    global visited,adj
    visited[v]=1
    height=lv
    max_height=lv
    for i in range(0,len(adj[v])):
        #print(adj[v][i],visited,v)
        if(visited[adj[v][i]]==0):
            height=DFS(adj[v][i],lv+1)
            max_height=max(max_height,height)
    return max_height
    
    
n=int(input())
node=[0 for i in range(0,n+1)]
adj=[[] for i in range(0,n+1)]
visited=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    x=list(map(int,input().strip().split(" ")))
    if(x[0]==0):
        node[i]=2#leaf
    for a in x:
        node[a]=1#有parent不會是root
    adj[i]=x
root=0
for i in range(1,n+1):
    if node[i]==0:
        root=i
        print(i)
        break
height=DFS(root,0)

print(height)
   
