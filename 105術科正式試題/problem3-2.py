#105商業技藝競賽正式試題
#Problem 3： 資料結構—樹 子題 2：二元樹的走訪
#Author:Yotrew
#20210710
'''
prefix: NLR
infix:  LNR
postfix:LRN
以prefix的N找出此N在infix的哪個地方,就可以將infix切成L N R
那再調換順序變成L R N求出postfix
'''
n=int(input())

prefix=[]
infix=[]

def travesal(n,ls,rs):
    global prefix,infix
    postfix=[]
    #print(n,ls,rs,pos,prefix[n])
    if(ls==rs):
        return [prefix[n]]
    if(ls>rs):
        return []
    pos=infix.index(prefix[n])

    #print(pos)
    N=[prefix[n]]
    L=travesal(n+1,ls,pos-1)
    R=travesal(n+(pos-ls)+1,pos+1,rs)
    if R==None:#有可能沒右子樹,那就不會執行travesal
        R=[]
    if L==None:
        L=[]
    for a in L:
        postfix.append(a)
    for a in R:
        postfix.append(a)
    for a in N:
        postfix.append(a)
    return postfix
    
for i in range(0,n):
    infix=input().strip().split(",")
    prefix=input().strip().split(",")
    #print(infix)
    #print(prefix)
    y=travesal(0,0,len(prefix)-1)
    for a in range(0,len(y)-1):
        print(y[a],end=",")
    print(y[-1])
    #print(prefix)
