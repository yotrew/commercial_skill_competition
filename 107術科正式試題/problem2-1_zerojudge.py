#107商業技藝競賽正式試題
#Problem 2：子題 1：快樂數字。
#由給的範例推測,unhappy number應該最後會產生"20"-->"4"
#               happy number最後會產生"1",所以只有2種情況
#丟給UVa10591 https://zerojudge.tw/ShowProblem?problemid=d442程式
n=int(input())
for i in range(0,n):
    a=int(input())
    c=a
    happy="is an Unhappy number."
    while happy=="is an Unhappy number.":
        b=0
        while(a>0):
            b=b+(a%10)**2
            a=int(a/10)
        a=b
        if(a==1):
            happy="is a Happy number."
            break
        if(a==4):
            break
    print(f"Case #{i+1}: {c} {happy}")

