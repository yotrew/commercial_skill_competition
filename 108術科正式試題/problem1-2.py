#108商業技藝競賽正式試題
#Problem 1：子題 2：保齡球計分
#此題應該是延續上一題的概念
#*第10局的全倒沒有往後加分,所以要先找出第10局在那裡
'''
方法2:給學生的方法是儲存成像真實保齡球一樣的表格
以[a,b,0],來存一局內2個格的分數
第10局儲[a,b,c]
遇到X,存[-10,0,0],遇到/,存[a,a-10,0] ,負的就可以判斷要加分
'''
n=int(input())
for i in range(0,n):
    x=input().strip().split(" ")
    count=0#加分加幾次
    score=0
    tenth=0
    e=0
    for a in range(0,len(x)):
        if(x[a]=='X'):
            e+=1
        e+=1
        if(e==18):
            tenth=a+1#第10局所在位置
            break
    #print(tenth,x[tenth])
    for a in range(0,tenth):
        if(x[a]=='X'):
            score+=10
            c=x[a+1]
            d=x[a+2]
            if(c=='X'):
                c=10
            if(d=='X'):
                d=10
            if(d=='/'):
                #print(a,x,c,d)
                d=10-int(c)
            score+=int(c)+int(d)
            
        elif(x[a]=='/'):
            score+=10-int(x[a-1])
            if(x[a+1]=='X'):
                score+=10
            else:
                score+=int(x[a+1])
        else:
            score+=int(x[a])
    for a in range(tenth,len(x)):#第十局另外處理
        if(x[a]=="X"):
            score+=10
        elif(x[a]=="/"):
            score+=10-int(x[a-1])
        else:
            score+=int(x[a])
            
    print(score)
