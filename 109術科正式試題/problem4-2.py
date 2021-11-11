#Problem 4：
#子題2：特殊郵件
#此題要找的是從那一個開始會傳最多點,但若有2點以上傳數目一樣多就輸出index較小的
# keyword:DFS,路徑拜訪

import pprint #為了輸出2維list會比較好看

paths=[] #為了方便及效率就使用全域變數但這是不太好的
def DFS(n,level,visited):#n從那一點開始,level為第幾層,visited有拜訪過的列表
    global paths
    #print(n,level)
    #pprint.pprint(visited)
    for i in range(1,len(paths)):
        if(i==n):
            continue
        if(paths[n][i]==1 and i not in visited):
            tmp=visited.copy()
            tmp.append(i)
            level=DFS(i,level+1,tmp)
    return level


n=int(input())
for i in range(0,n):
    N=int(input())
    paths=[[0 for j in range(0,N+1)] for i in range(0,N+1)] #路徑列表

    cost=[0 for j in range(0,N+1)]

    for j in range(0,N):#資料輸入並處理,放到路徑表中
        x=input().strip().split(" ")
        u=int(x[0])
        v=int(x[1])
        paths[u][v]=1
        
    for j in range(1,N+1):#使用DFS路徑拜訪
        cost[j]=DFS(j,1,[j])
        

    max_cost_pos=0 #假設最大路徑的值在第0個(第0個沒有用到)
    for j in range(1,N+1):#找出最大路徑,記得是N+1
        if cost[max_cost_pos]<cost[j]:
            max_cost_pos=j
    print(max_cost_pos)



