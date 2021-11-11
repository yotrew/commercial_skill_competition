#105商業技藝競賽正式試題
#Problem 1：字串問題 子題 1：計算字數。
#同106商業技藝競賽模擬試題Problem 1：子題 1
#類似106商業技藝競賽正式試題Problem 1：子題 1
#類似107商業技藝競賽正式試題Problem 1：子題 1
#Author:Yotrew
#20210710

'''
#python做法
n=int(input())
for i in range(0,n):
    tmp=input().split(" ")
    #print(tmp)
    print(len(tmp))
'''
n=int(input())
for i in range(0,n):
    tmp=input().strip()
    cnt=0
    flag=False
    for a in range(0,len(tmp)):
        if(tmp[a]==" ") or (tmp[a]==".") or (tmp[a]=="!") or (tmp[a]==";"):
            if(flag):
                cnt+=1
            flag=False
        if(tmp[a]!=" ") and (tmp[a]!=".") and (tmp[a]!="!") and (tmp[a]!=";"):
            flag=True

    if(flag==True):#有可能沒有以上4個符號做為結束
        cnt+=1
    print(cnt)
