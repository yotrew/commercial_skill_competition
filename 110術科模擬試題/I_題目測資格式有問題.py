#110商業技藝競賽模擬試題
#Problem #I 矩陣乘法
#Author: Yotrew Wing
#2021/10/18

while True:
    try: 
        a,b,c,d=list(map(int,input().split()))
        if(b!=c):
            continue
        AB=[[0 for i in range(d)] for j in range(a)]
        A=[]
        B=[]

        for i in range(a):
            A.append(list(map(int,input().split())))
        for i in range(c):
            B.append(list(map(int,input().split())))

        for i in range(a):
            for j in range(d):
                for k in range(b):
                    #print(i,j,k)
                    AB[i][j]+=A[i][k]*B[k][j]

        for i in range(a):
            for j in range(d-1):        
                print(AB[i][j],end=" ")
            print(AB[i][-1])
    except EOFError:
        break
