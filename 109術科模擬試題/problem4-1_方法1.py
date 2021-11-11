#109商業技藝競賽模擬試題
#Problem 4： 子題1：關節點(程式執行限制時間: 2 秒)
'''
此題在題目中已提供方法:
DFS,關節點:
'''
import pprint

#Global variables
paths=[]
Articulation=[]#關節點
tree_level=0
v=[]
up=[]

def DFS(p,t):
    global paths,Articulation,tree_level,v,up
    tree_level+=1
    v[t]=tree_level
    up[t]=tree_level
    
    child=0 #此P點有幾個兒子
    AP=False
    #print(tree_level,p,t)
    next_point=0
    #print(t,"len",len(paths[t]))
    for i in range(0,len(paths[t])):
        next_point=paths[t][i]
        if(next_point!=p):
            if v[next_point]>0:
                up[t]=min(up[t],v[next_point])
            else:
                child+=1
                DFS(t,next_point)
                up[t]=min(up[t],up[next_point])
                if up[next_point]>=v[t]:
                    AP=True
    if(t==p and child>1) or (t!=p and AP==True):
        #print(t,child,AP)
        Articulation.append(t)
    #print(v,up)
    
while True:
    n=int(input())
    if n==0:#結束
        break

    #Reset Variable
    root=0
    paths=[[] for i in range(0, n+1)]
    v=[0 for i in range(0, n+1)]
    up=[0 for i in range(0, n+1)]
    Articulation=[]
    while True:#讀入Paths
        x=list(map(int,input().strip().split(" ")))
        if(root==0):
            root=x[0]
        if(x[0]==0):
            break
        
        #讀入paths
        for i in range(1,len(x)):
            #print(i)
            #paths[x[0]].append(x[i])
            if x[i] not in paths[x[0]]:
                paths[x[0]].append(x[i])
            if x[0] not in paths[x[i]]:
                paths[x[i]].append(x[0])

    #DFS
    DFS(root,root)

    print(len(Articulation))
    v1=[0 for i in range(0,n+1)]

        
