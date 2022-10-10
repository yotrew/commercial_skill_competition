#110商業技藝競賽正式試題
#Problem C 所有位數加減加減
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
while True:
    try:
        num=list(map(int,list(input())))
        sum1=num[0]
        s=1
        for i in range(1,len(num)):
            sum1+=(s*num[i])
            s*=-1
        print(sum1)
    except :
        break
