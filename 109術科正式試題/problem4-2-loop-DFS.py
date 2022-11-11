#Problem 4：
#子題2：特殊郵件
#此題要找的是從那一個開始會傳最多點,但若有2點以上傳數目一樣多就輸出index較小的
#用2維的會爆,且不會有一對多個(所以此題就已經有所限制),所只需1維

n=int(input())

for i in range(0,n):
    N=int(input())
    #paths=[0 for i in range(0,N+1)] #路徑列表
    #cost=[0 for i in range(0,N+1)] #
    
    paths=[0] * (N+1) #路徑列表 #[x]*n 如果[x]是list會有問題<--參考107商業技藝競賽正式試題 #Problem 4：子題 1。
    cost=[0] * (N+1)
    
    for j in range(0,N):#資料輸入並處理,放到路徑表中
        x=input().split(" ")
        paths[int(x[0])]=int(x[1])
    #print(paths)
    max_cost=0
    max_cost_node=0
    visited=[0 for i in range(0,N+1)]#真正被拜訪過的node
    visited2=[0 for i in range(0,N+1)]#<---在Python中加速用的小技巧
    stack=[] 
    for j in range(1,N+1):#從每一點出發,找出此點最大寄件數
        next_node=j
        stack=[]
        visited1=visited2.copy()#copy會比[0 for i in range(0,N+1)]快
                                #visited1用來尋找路徑過程暫存被拜訪過的
        while visited1[next_node]==0 and visited[next_node]==0:
            stack.append(next_node)#push
            visited1[next_node]=1#誰來拜訪我
            next_node=paths[next_node]

        if(len(stack)==0):
            continue
        
        #loop要先處理,loop不可能接出去: 因為題目就限制住了
        #不可能分支出去,分支出去代表某個點有2個分支
        loop=-1
        if(paths[stack[-1]]!=0 and len(stack)>1):
            #最後一點的下一點不是0,代表發生loop或接枝
            for i in range(0,len(stack)):#找到loop在此stack的那裡
                if(paths[stack[-1]]==stack[i]):
                    loop=i
                    break

        cost_tmp=len(stack)-loop
        if(loop!=-1):#串接
            for i in range(len(stack)-1,loop-1,-1):
                cost[stack[i]]=cost_tmp
                visited[stack[i]]=1
                stack.pop()
            
        count=0
        
        
        for i in range(len(stack)-1,-1,-1):#接枝
            pos=stack[i]

            if i==(len(stack)-1):
                if visited[paths[pos]]==1 :#串接
                    cost[pos]=len(stack)-i+cost[paths[pos]]
                else:
                    cost[pos]=1
            else:
                cost[pos]=1+cost[paths[pos]]
            visited[pos]=1
            
    for i in range(1,N+1):#找出最大cost,且編號小的
        if cost[max_cost_node] < cost[i]:
            max_cost_node=i
    print(max_cost_node)

