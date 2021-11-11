#108商業技藝競賽正式試題
#Problem 2：子題 1：包含某個數字

'''
數學解法:
N介於0~999因此prefix只有n=10(N長度為1),n=10(N長度為2),n=1000(N長度為3)
利用prefix將目前的數縮成1~3位數
然後使用loop從A~B找,
若N=13, A,B=132~213
132%100=32 != 13 -->132//10=13
13%100=13 == 13
'''
n=int(input())
for i in range(0,n):
    A,B,N=map(int,input().strip().split(" "))

    if 0<=N<=9:
        n=10
    elif 10<=N<=99:
        n=100
    elif 100<=N<=999:
        n=1000
        
    count=0
    for a in range(A,B+1):
        x=a
        while x>0:
            if x%n==N:
                count+=1
                break
            x//=10
    if N==0 and A==0:#特殊情況
        count+=1
    print(count)
