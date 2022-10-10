#110商業技藝競賽模擬試題
#Problem E所有位數和--數學除法運算做法
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
while True:
    try:
        sum=0
        n=int(input())
        while n>0:
            sum+=n%10
            n=n//10 # n=int(n/10)
        print(sum)
        
    except EOFError:
        break
