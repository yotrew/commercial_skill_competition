#108商業技藝競賽正式試題
#Problem 2：子題 1：包含某個數字

'''
寫程式偷懶做法:變字串,但效率可能不好,但寫程式就很快(比賽中要去取捨的)
*但其他解法好像也沒比較快

'''
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    A=x[0]
    B=x[1]
    N=str(x[2])
    count=0
    for a in range(A,B+1):
        y=str(a)
        if N in y:
            count+=1
    print(count)
