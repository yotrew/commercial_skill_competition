#Problem 1：
#子題2：打印機。(程式執行限制時間: 2 秒)
#數字解法
N=[]

try:
    while True:
        N.append(int(input()))
        if(len(N)>N[0]):
            break
except:
    pass
  
for  i in range(1,len(N)):
    tmp=N[i]
    A=0
    B=0
    P=1
    while(tmp>0):
        y=tmp%10
        if(y==4):
            A=A+3*P
            B=B+1*P
        else:
            A=A+y*P
        P=P*10
        tmp=int(tmp/10)
    print(A,B)
