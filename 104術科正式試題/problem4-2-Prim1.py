#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 2：最小成本生成樹。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210712

table={}
for i in range(65,65+26):
    table[chr(i)]=i-65
n=int(input())
node=[]
visited=[]
for i in range(0,n):
    x=input().strip().split()
    adj=[[65536 for a in range(0,26)] for a in range(0,26)]#相鄰串列
    node=[0 for a in range(0,26)]#最多就26個點
    visited=[0 for a in range(0,26)]#最多就26個點
    for a in x:
        y=a.split(",")
        #print(y)
        adj[table[y[0]]][table[y[1]]]=int(y[2])
        adj[table[y[1]]][table[y[0]]]=int(y[2])
        node[table[y[0]]]=1
        node[table[y[1]]]=1
    node_cnt=0
    #print(node)
    start=-1
    for a in range(0,len(node)):
        if(node[a]==1):
            start=a
            node_cnt+=1

    #Prim 演算法：
    queue=[]

    queue.append(start)
    cost=0
    visited[start]=1
    while len(queue)<(node_cnt):
        min_pos=65536#邊最大值為65535
        min_target=-1
        for a in queue:
            #print(a,queue)
            
            for b in range(0,len(adj[a])):
                if(a==b):
                    continue
                if(visited[b]==0 and adj[a][b]<min_pos and node[b]==1):#未被拜訪過的點,且邊為最小
                    min_pos=adj[a][b]
                    min_target=b
        if(min_target!=-1):
            cost+=min_pos
            queue.append(min_target)
            visited[min_target]=1
            #print(cost)
            #print(visited,min_target)
    #print(queue)
    print(cost)
