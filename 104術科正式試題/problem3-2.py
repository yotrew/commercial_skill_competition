#104商業技藝競賽正式試題
#Problem 3：其他 子題 1：矩陣的乘法AB=A*B。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210712

n=int(input())

for i in range(0,n):
    A=[]
    B=[]
    AB=[]
    x=list(map(int,input().strip().split(",")))
    m=x[0]
    r=x[1]
    n=x[3]
    unknow=-1#9999在那一個matrix,0代表A,1代表B,-1代表還未找到
    uk_i=0#9999存在第幾列
    uk_j=0#9999存在第幾欄
    for a in range(0,m):
        y=input().strip().replace("\t"," ").split(" ")#有奇怪的測資
        y=list(map(int,y))
        A.append(y)
        for b in range(0,r):
            #print(r,len(y))
            if(unknow==-1 and y[b]==9999):
                uk_i=a
                uk_j=b
                unknow=0
    for a in range(0,r):
        y=input().strip().replace("\t"," ").split(" ")#有奇怪的測資
        y=list(map(int,y))
        B.append(y)
        for b in range(0,n):
            if(unknow==-1 and y[b]==9999):
                uk_i=a
                uk_j=b
                unknow=1
    #print(uk_i,uk_j,unknow)
    for a in range(0,m):
        y=input().strip().replace("\t"," ").split(" ")#有奇怪的測資
        y=list(map(int,y))
        AB.append(y)

    ans=0
    if(unknow==0):#在A martrix中
        col=(uk_j+1)%n#取的欄不能是所在列-->if a!=uk_j:
        ans=AB[uk_i][col]
        #print(ans,unknow,uk_i,uk_j)
        for a in range(0,r):
            if a!=uk_j:
                ans-=A[uk_i][a]*B[a][col]
        if(B[uk_j][col]!=0):
            ans = ans / B[uk_j][col]
    else:#在B martrix中
        row=(uk_i+1)%m#取的列不能是所在欄-->if a!=uk_i:
        ans=AB[row][uk_j]
        for a in range(0,r):
            if a!=uk_i:
                ans-=A[row][a]*B[a][uk_j]
                #print(ans,A[row][a],B[a][uk_j])
        if(A[row][uk_i]!=0):
            ans = ans / A[row][uk_i]
    #print(A)
    #print(B)
    #print(AB)
    print(int(ans))
    
