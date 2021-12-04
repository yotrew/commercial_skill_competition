#110商業技藝競賽正式試題
#Problem M 矩陣的直積

#Author: Yotrew Wing
#2021/12/02

matrix=[[0 for i in range(20*20+1)] for j in range(20*20+1)]
while True:
    try:
        A=[]
        B=[]
        m,n,p,r=map(int,input().split(" "))
        
        for i in range(m):
            A.append(list(map(int,input().split(" "))))
        for i in range(p):
            B.append(list(map(int,input().split(" "))))


        for a in range(m):
            for c in range(p):
                for b in range(n):
                    for d in range(r):
                        matrix[a*p+c][b*r+d]=A[a][b]*B[c][d]
        outs=""
        for a in range(m):
            for c in range(p):
                for b in range(n):
                    for d in range(r):
                        outs+=str(matrix[a*p+c][b*r+d])+" "
                print(outs[:-1])
                outs=""
    except Exception as e:
        break


