#107商業技藝競賽正式試題
#Problem 3：子題 1：大數乘冪運算。
'''
此題看起來是大數問題,但其實就只是數學問題
此題要求的是m^k共有幾位數
m^k=10^x --> x就是位數
兩邊取log
log(m^k,10)=log(10^x,10)
k*log(m,10)=x  -->x就是位數,也就是求出k*log(m,10)的上限就是結果
'''
n=int(input())

import math
for i in range(0,n):
    x=list(map(int,input().split(",")))
    print(int(x[1]*math.log(x[0],10))+1)
    

