#Problem 4：
#子題2：特殊郵件
#此題要找的是從那一個開始會傳最多點,但若有2點以上傳數目一樣多就輸出index較小的
#用2維的會爆,且不會有一對多個(所以此題就已經有所限制),所只需1維
n=int(input())


for i in range(0,n):
    N=int(input())
    paths=[0 for i in range(0,N+1)] #路徑列表
    for j in range(0,N):#資料輸入並處理,放到路徑表中
        x=input().split(" ")
        paths[int(x[0])]=int(x[1])
    #print(paths)
    max_cost=0
    max_cost_node=N+1
    visited1=[0 for i in range(0,N+1)]#加速用
    
    for j in range(1,N+1):#從每一點出發,找出此點最大寄件數
        visited=visited1.copy()#
        visited[0]=visited[j]=1
        next_node=paths[j]
        cost=0
        #print(next_node,end="-->")
        while visited[next_node]==0:
            visited[next_node]=1
            cost+=1
            next_node=paths[next_node]

            #print(next_node,end="-->")
        #print()
        if(cost>max_cost):
            max_cost=cost
            max_cost_node = j
    print(max_cost_node)


