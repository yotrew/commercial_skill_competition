#110選手最原始答案修改

import sys
times=0
flag=False#旗標
for line in sys.stdin.readlines():
    line=line.rstrip("\n")
    #if len(line.split())==4:#測資中可能會有 x列4欄(4個數字)的矩陣
    if flag==False:
        pre=[]
        a,b,c,d=map(int,line.split())
        A=[[]*b for i in range(a)]
        B=[[]*d for i in range(c)]
        C=[[]*d for i in range(a)]
        flag=True
    else:
        for i in map(int,line.split()):
            pre.append(i)
        if len(pre)==a*b+c*d:#矩陣運算
            flag=False#矩陣運算的下一列才會是 四個數字 a b c d

            for i in range(a):
                for j in range(b):
                    A[i].append(pre[0])
                    del pre[0]
            for i in range(c):
                for j in range(d):
                    B[i].append(pre[0])
                    del pre[0]
            for i in range(a):
                for j in range(d):
                    C[i].append(0)
                    for k in range(b):
                        C[i][j]+=A[i][k]*B[k][j]
                    print(C[i][j],end=' ')
                print()
