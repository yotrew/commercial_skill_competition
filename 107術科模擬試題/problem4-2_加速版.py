#107商業技藝競賽模擬試題
#Problem 4： 子題2：最小成本生成樹。
#按照題目給於的說明做
#加速版--visted array先建好,然後用copy的
import copy
n=int(input())
visited1=[0 for a in range(0,25)]
for i in range(0,n):
    paths=[]
    x=input().split(" ")
    for a in x:
        y=a.split(",")
        paths.append([ord(y[0])-65,ord(y[1])-65,int(y[2])])#以list來存[A點,B點,距離]
    paths=sorted(paths,key=lambda x:x[2])#按題目說明,以最小的開始,就直接排序距離
    #visited=visited1.copy()#記錄是否已存在的邊,用拜訪過的點來記錄
    visited=copy.deepcopy(visited1)
	
    cost=0
    for a in paths:#每個邊的看一次,會形成loop的踢掉
        if visited[a[0]]==1 and visited[a[1]]==1: #形成loop
            continue
        cost=cost+a[2]
        visited[a[0]]=1
        visited[a[1]]=1
    print(cost)
