#111商業技藝競賽模擬試題
#Problem #A2 MOD
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition


x=int(input())
y=int(input())
if x>y:
    x,y=y,x

for i in range(x+1,y):
    if i%5==2 or i%5==3:
        print(i)
