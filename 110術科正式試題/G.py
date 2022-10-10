#110商業技藝競賽正式試題
#Problem G 猜數字
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
'''
要處理不同條件(狀況)
'''

nums=list(map(int,input().split(" ")))
n=int(input())
for i in range(n):
    A,B=0,0
    guess=list(map(int,input().split(" ")))
    Avisited=[] #比對過的就不會再被比了
    Bvisited=[]
    for j in range(4):
        if nums[j]==guess[j]:
            A+=1
            Avisited.append(j)
            Bvisited.append(j)
    for k in range(4):
        if k in Bvisited :#那個位置被比對過了
            continue
        for j in range(4):
            if j in Avisited :#那個位置被比對過了
                continue
            if k in Bvisited :#那個位置被比對過了
                continue
            if nums[j]==guess[k]:
                B+=1
                Avisited.append(j)
                Bvisited.append(k)
    print(f"{A}A{B}B")
