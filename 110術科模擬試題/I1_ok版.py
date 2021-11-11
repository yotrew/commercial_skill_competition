#I 矩陣乘法--不會因為測資格式問題而run-time error版
while True:
    try: 
        a,b,c,d=list(map(int,input().split()))
        if(b!=c):
            continue
        AB=[[0 for i in range(d)] for j in range(a)]
        A=[]
        B=[]
        tmp=[]
        while (len(tmp)<a*b+b*d):
            tmp.extend(list(map(int,input().split())))
 
        for i in range(a):
            A.append([])
            for j in range(b):
                A[i].append(tmp.pop(0))
        for i in range(b):
            B.append([])
            for j in range(d):
                B[i].append(tmp.pop(0))
        
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
