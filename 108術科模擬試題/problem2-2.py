#108商業技藝競賽模擬試題
#Problem 2：子題 2：阿姆斯壯數。
#Author:Yotrew
#20210709
n=int(input())
for i in range(0,n):
    x=input().strip()
    y=list(map(int,x))
    armstrong=0
    power=len(y)#次方就是數字位數
    for i in range(0,power):
        armstrong+=y[i]**power
    if(int(x)==armstrong):
        print("Y")
    else:
        print("N")

