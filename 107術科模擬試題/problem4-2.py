#107商業技藝競賽模擬試題
#Problem 4： 子題2：最小成本生成樹。
#按照題目給於的說明做
#*是否還有什麼情況未考慮到的,像是不是有不完整的圖(分成2部份)
n=int(input())

for i in range(0,n):
    paths=[]
    x=input().split(" ")
    for a in x:
        y=a.split(",")
        paths.append([y[0],y[1],int(y[2])])#以list來存[A點,B點,距離]
    paths=sorted(paths,key=lambda x:x[2])#按題目說明,以最小的開始,就直接排序距離
    visited=[0 for a in range(0,25)]#記錄是否已存在的邊,用拜訪過的點來記錄
    cost=0
    for a in paths:#每個邊的看一次,會形成loop的踢掉
        if visited[ord(a[0])-65]==1 and visited[ord(a[1])-65]==1: #形成loop
            continue
        cost=cost+a[2]
        visited[ord(a[0])-65]=1
        visited[ord(a[1])-65]=1
    print(cost)
