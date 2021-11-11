#109商業技藝競賽模擬試題
#Problem 2：子題2：幾A 幾B。(程式執行限制時間: 2 秒)
#106商業技藝競賽正式試題roblem 2：子題2

n=int(input())

for i in range(0,n):
    x=input().split(", ")#有空白要處理
    A=0
    B=0
    for a in range(0,len(x[0])):
        for b in range(0,len(x[1])):
            if(a==b and x[0][a]==x[1][b]):
                A=A+1
                continue
            if(a!=b and x[0][a]==x[1][b]):
                B=B+1
                continue
    print("{}A{}B".format(A,B))
    

