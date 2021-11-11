#103商業技藝競賽正式試題
#Problem 4： 資料結構—樹、陣列 子題 2：列出所有樹的某節點到根節點之路徑長度。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210713
'''
雖然這題說是樹,但就只是對路徑的追蹤追到root,直接用迴圈的DFS
'''
#print(fib)

n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    m=x[0]
    k=x[1]
    v=x[2]

    path=[[] for i in range(0,m)]
    for a in range(0,m):
        x=list(map(int,input().strip().replace("  "," ").replace("  "," ").replace("  "," ").split(" ")))#一堆空白
        path[x[0]]=x[1:]
               
    #print(path)
    distance=[]
    for a in range(0,k):
        #print(v,a)
        node=path[v][a]
        cnt=0
        while node!=999:
            node=path[node][a]
            cnt+=1
        distance.append(cnt)
    for a in range(0,len(distance)-1):
        print(distance[a],end=",")
    print(distance[-1])
        
    
        
