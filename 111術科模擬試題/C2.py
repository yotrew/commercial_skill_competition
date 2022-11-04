#111商業技藝競賽模擬試題
#Problem #C2 數字次數
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

n=int(input())
tnums=[0 for i in range(10)]
for i in range(n):
    nums=tnums.copy()
    x=int(input().strip())
    for j in range(x+1):
        y=j
        while y>0:
            nums[y%10]+=1
            y=y//10
    print(" ".join(map(str,nums)))
