#104商業技藝競賽正式試題
#Problem 3：其他 子題 1：計算位元為1 的個數。(程式執行限制時間: 2 秒)
#同105商業技藝競賽正式試題 Problem 2：數學問題 子題 2：最大公約數計算
#Author:Yotrew
#20210711

n=int(input())

for i in range(0,n):
    x=int(input().strip())
    cnt=0
    while x>0:
        if(x%2==1):
            cnt+=1
        x//=2
    print(cnt)
    
    
