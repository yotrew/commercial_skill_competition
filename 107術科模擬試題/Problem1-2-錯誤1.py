#107商業技藝競賽模擬試題
#子題2：邏輯表示式

n=int(input())
for i in range(0,n):
    x=input().split("==")
    a=eval(x[0].strip()) #這不是一個好方法,因為不是所有語言都有,且會有浮點數的問題
    ans=eval(x[1])
    if(a==ans):
        print("T")
    else:
        print("F")
    print(a,ans)
