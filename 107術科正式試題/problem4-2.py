#107商業技藝競賽正式試題
#子題 2：循環排列cyclic permutation。
'''
本題似乎沒有很難,只是題目敍述有點難懂
'''

n=int(input())
x_visited1=[0]* 21 #[x]*n 如果[x]是list會有問題<--參考107商業技藝競賽正式試題 #Problem 4：子題 1。
for i in range(0,n):
    #2個list結合成一個list,用"+"
    y=[0]+(list(map(int,input().replace("[","").replace("]","").split(","))))
    x_visited=x_visited1.copy()
    len_y=len(y)
    out=[]
    for a in range(1,len_y):#從1開始,因為從小的開始
        if(x_visited[a]==1):
            continue
        pos=0
        tmp=[]
        
        for b in range(1,len_y):#找到a的所在位置
            if(y[b]==a):
                pos=b
                break
            
        x_visited[y[pos]]=1
        tmp.append(y[pos])
        pos=y[pos]
        while y[pos]!=a:#找出循環
            x_visited[y[pos]]=1
            tmp.append(y[pos])
            pos=y[pos]
        out.append(tmp)
    print(out)   

