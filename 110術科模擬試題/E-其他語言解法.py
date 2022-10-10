#110商業技藝競賽模擬試題
#Problem E所有位數和--Array做法
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
while True:
    try:
        sum=0
        n=input()
        for i in range(len(n)):
            sum+=int(n[i])
        print(sum)
        
    except EOFError:
        break
