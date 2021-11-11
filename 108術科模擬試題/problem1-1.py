#108商業技藝競賽模擬試題
#Problem 1：子題 1：二進位轉十進位。
#Author:Yotrew
#20210709

n=int(input())
for i in range(0,n):
    x=input().strip().split(".")
    ans=0
    for i in range(0,len(x[0])):
        ans+=int(x[0][i])*(2**(len(x[0])-i-1))
        #print(x[0][i])
    
    for i in range(0,len(x[1])):
        ans+=int(x[1][i])*(0.5**(i+1))#可能會有精準度問題,可能沒有
        if(i==5):
            break
    print(ans)
