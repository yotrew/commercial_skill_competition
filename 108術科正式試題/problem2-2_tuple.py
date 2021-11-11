#108商業技藝競賽正式試題
#Problem 2：子題 2：求餘數
'''
此數看似大數問題,一般的解法也是大數
1. 大數解法(慢)

'''
n=int(input())
for i in range(0,n):
    X,Y,M=map(int,input().strip().split(" "))
    R=X%M
    
    for a in range(1,Y):
        R=(R*X)%M
    
    print(R)
