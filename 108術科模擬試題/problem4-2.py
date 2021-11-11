#108商業技藝競賽模擬試題
#Problem 4：子題 2：組合
#Author:Yotrew
#20210709
'''
一樣大數問題,先約分
'''
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    a=x[0]
    b=x[1]
    c=a-b
    f=1
    if(b<c):#若b小於c就2個互換<--這樣就可以約分約掉,可加速許多
            #不互換會TLE
        b,c=c,b 
        
    for i in range(b+1,a+1):
        f=f*i
    for i in range(2,c+1):
        f=f/i
    print(int(f))

    
   
