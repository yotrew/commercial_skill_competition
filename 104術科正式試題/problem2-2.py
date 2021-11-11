#104商業技藝競賽正式試題
#Problem 2：數學問題 子題 2：最大公約數計算。(程式執行限制時間: 2 秒)
#同105商業技藝競賽正式試題 Problem 2：數學問題 子題 2：最大公約數計算
#Author:Yotrew
#20210711
'''
'''

def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)
    
n=int(input())

for i in range(0,n):
    in_str=list(map(int,input().strip().split(",")))
    ans=in_str[0]
    for a in range(1,len(in_str)):
        ans=GCD(ans,in_str[a])
    print(ans)
    
    
