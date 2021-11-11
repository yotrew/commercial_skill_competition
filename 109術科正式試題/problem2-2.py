#Problem 2：
#子題2：數字相乘。(程式執行限制時間: 2 秒)
N=int(input())
num=[]
for i in range(0,N):
    num.append(int(input()))

#print(num)
for i in range(0,N):
    A=num[i]
    Q=0
    P=0

    j=9
    while j>=2:
        if A%j ==0:
            Q=Q+j*10**P #若是python可以使用串字串的方式
            A=A/j
            P=P+1
        else:
            j-=1
    if(A>2):
        #print(-1,A,Q)
        print(-1)
    elif Q==0 and A==1:
        print(1)
    else:
        print(Q)

