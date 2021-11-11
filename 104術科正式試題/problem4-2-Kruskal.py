#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 2：最小成本生成樹。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210711


table={}
for i in range(65,65+26):
    table[chr(i)]=i-65
n=int(input())
node=[]
visited=[]
edges=[]#相鄰串列
parent=[]#記錄我是從誰而來,這樣才能判斷是否為loop

def getRoot(a):
    global parent
    if parent[a]==-1:
        return a
    else:
        return getRoot(parent[a])

for i in range(0,n):
    x=input().strip().split()
    edges=[]#相鄰串列
    node=[[] for i in range(0,26)]#最多就26個點
    visited=[0 for i in range(0,26)]#最多就26個點
    parent=[-1 for i in range(0,26)]
    for a in x:
        y=a.split(",")
        #print(y)
        edges.append([table[y[0]],table[y[1]],int(y[2])])
        node[table[y[0]]]=1
        node[table[y[1]]]=1
        #adj[y[1]]={y[2]:int(y(2))}

    #Kruskal 演算法：
    edges=sorted(edges,key=lambda x:x[2])
    #print(edges)    
    cost=0
    for b in edges:
        '''
        #判斷有沒有形成loop不是這麼簡單,當形成2個樹以上就不適用(判斷loop未完成)
        if visited[b[0]]==1 and visited[b[1]]==1:#會形成loop
            continue

        '''
        if visited[b[0]]==1 and visited[b[1]]==1:#可能會形成loop
            #判斷是否會形成loop,只有其中一個沒拜訪過一定不會形成loop
            root1=getRoot(b[0])
            root2=getRoot(b[1])
            #print(root1,root2,b[0],b[1])
            if(root1 == root2):#形成loop,因為有相同的祖先,就不把此邊加入
                continue
            else:#2樹合併
                #2樹合併時,某一顆子樹要併到另一顆就要從該點併過去,
                #此點會變成該祖先的祖先,也就是要轉向
                #如A<-B<-C    D<-E<-F<-G, 合併邊為B,F,F併到B,F的父親為B,
                #則變成D->E->F<-G
                #            \    /-C
                #             -> B -> A    (當然還有其他方法)
                p=parent[b[0]]
                c=b[0]
                while c!=-1:
                    tmp=parent[p]
                    parent[p]=c
                    c=p
                    p=tmp                    
                parent[b[0]]=b[1]#2樹合併

        #記錄某一點是由另一點而來
        if visited[b[0]]==0 and visited[b[1]]==0:#都沒被拜訪過,找一個當root
            parent[b[1]]=b[0] #b[0]是由b[1]來的
        if visited[b[0]]==1 and visited[b[1]]==0:#
            parent[b[1]]=b[0] #b[1]是由b[0]來的
        if visited[b[1]]==1 and visited[b[0]]==0:#
            parent[b[0]]=b[1] #b[0]是由b[1]來的
            
        
        cost+=b[2]
        visited[b[0]]=1
        visited[b[1]]=1
    print(cost)
