#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 2：最小成本生成樹。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210713
'''
本解法也是Prim法,不到20分鐘就完成此程式
想法:
1.把"邊"集合排序
2.找任一點為起始頂點,把它加入形成MST的list中
  (並把此路徑從"邊"集合中拿掉*不拿應該也可以,拿應該可以加速)
3.以MST的list中的點去找剩下邊集合中最小邊且點沒被拜訪過
'''
n=int(input())
paths=[]
visited={}
for i in range(0,n):
    x=input().strip().split()
    paths=[]#相鄰串列
    visited={}#編號用字母,所以用dict,加速用的
    for a in x:
        y=a.split(",")
        paths.append([y[0],y[1],int(y[2])])#點1,點2,weight
        visited[y[0]]=0
        visited[y[1]]=0
        #print(y)
    paths=sorted(paths,key=lambda x:x[2])
    #print(paths)
    #print(len(visited))
    node=[]
    node.append(paths[0][0])#取一點為頂點
    visited[paths[0][0]]=1
    cost=0
    while len(node) <len(visited):
        for a in paths:
            #print(a[0],a[1])
            #if a[0] in  node and a[1] in  node:#loop ,#找那麼多次 xx in node,不會慢嗎?
            if visited[a[0]]==1 and visited[a[1]]==1:#loop
                continue
            #if not a[0] in  node and not a[1] in  node:#無法接入此圖(樹)
            if visited[a[0]]==0 and visited[a[1]]==0:#無法接入此圖(樹)
                continue
            #if a[0] not in node:
            if visited[a[0]]==0:
                node.append(a[0]) 
            else:
                node.append(a[1])
            visited[a[0]]=1
            visited[a[1]]=1
            cost+=a[2]
            paths.remove(a)#已加入的邊,就從原本的paths拿掉
            break
    print(cost)

