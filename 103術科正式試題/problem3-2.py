#103商業技藝競賽正式試題
#Problem 3：其他 子題 2：費氏數列
#Author:Yotrew
#20210713
#建費氏數列表
fib=[]
def gen_fib(n):
    global fib
    f1=0
    f2=1
    f3=0
    s=2
    while f3<=n:
        f3=f1+f2
        f1=f2
        f2=f3
        fib.append(f2)
        s+=1
gen_fib(10000)

#print(fib)
n=int(input())
for i in range(0,n):
    x=int(input().strip())
    y=x
    out=""
    a=len(fib)-1
    while a>=0:
        
        if x >=fib[a]:
            x-=fib[a]
            out+="1"
        else:
            out+="0"
        #print(x,a,fib[a],out)
        a-=1
    print(f"{y}={int(out)}")#轉int,前面的0就會不見   
    
        
