#104商業技藝競賽正式試題
#Problem 1：生活問題 子題 1：電梯電費計算系統。
#Author:Yotrew
#20210711


n=int(input())
for i in range(0,n):
    input()#使用python,VB(有字串split的程式語言)可以不case此數
    x=list(map(int,input().strip().split(",")))
    #print(x)
    value=0
    prev_floor=x[0]#上一次樓層
    floor=0
    for i in range(1,len(x)):
        floor=x[i]-prev_floor
        if(floor<0):
            value+=abs(floor)*10
        else:
            value+=floor*20
        prev_floor=x[i]
    print(value)
