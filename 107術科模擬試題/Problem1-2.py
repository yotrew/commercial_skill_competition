#107商業技藝競賽模擬試題
#Problem 1：  子題2：邏輯表示式
n=int(input())
for i in range(0,n):
    x=input().split("==")
    l=x[0].strip().split(" ")#左邊
    r=x[1].strip().split(" ")#右邊
    a=0
    ans=0
    a=float(l[0])*10#因為最多到小數第1位,防止在小數運算上的誤差,ex. 0.2+0.1=0.30000000000000004
    ans=float(r[0])*10
    for i in range(1,len(l),2):
        if l[i] =='+':
            a=a+float(l[i+1])*10
        if l[i] =='-':
            a=a-float(l[i+1])*10
    for i in range(1,len(r),2):
        if r[i] =='+':
            ans=ans+float(r[i+1])*10
        if r[i] =='-':
            ans=ans-float(r[i+1])*10
        
    if(int(a)==int(ans)):
        print("T")
    else:
        print("F")
