#109商業技藝競賽模擬試題
#Problem 1：子題1：找出比某數小的最大質數。
'''
建質數表會比較快,一樣建表,但建表方式不一樣(好像沒有比較快)
題目限制最大值為65535,所以只要找出2~65535的所有質數
'''
prime=[False for i in range(0,65536)]#2,3是質數
prime[2]=True
prime[3]=True
n=int(input())
for i in range(5,65535,2):#2的倍數不會是質數
    isPrime=True
    if i%3==0:
        isPrime=False
    for a in range(5,int(i**0.5)+1,2):
        if(i%a==0 and isPrime==True):#可被整除
            isPrime=False
            break
    if(isPrime):
        prime[i]=True
        
#print(len(prime),prime[0:20])
for i in range(0,n):
    x=int(input())
    for i in range(x-1,-1,-1):
        if(prime[i]):
            print(i)
            break
        
        
    
