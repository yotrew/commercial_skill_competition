#Problem 1：
#子題2：打印機。(程式執行限制時間: 2 秒)
#字串解法
N=[]

try:
    while True:
        N.append(input())
        if(len(N)>int(N[0])):
            break
except:
    pass
  
for  i in range(1,len(N)):
    A=""
    B=""
    for j in range(0,len(N[i])):
        if(N[i][j]=="4"):
            A=A+"3"
            B=B+"1"
        else:
            A=A+N[i][j]
            B=B+"0"
    print(int(A),int(B))
