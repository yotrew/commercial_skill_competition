#107商業技藝競賽模擬試題
#Problem 2：數學問題 子題 1：排列。
#排序後,最後2個數對調...這麼簡單?_?(因為'排列'順序"第2大"的數,前面排列的說明是用來騙你的XD)

n=int(input())
for i in range(0,n):
    x=input().strip().split(",")
    x=sorted(x,key=lambda y:y,reverse=True)
    tmp=x[-1]
    x[-1]=x[-2]
    x[-2]=tmp
    print("".join(x))
