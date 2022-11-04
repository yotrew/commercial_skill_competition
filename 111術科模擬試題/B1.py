#111商業技藝競賽模擬試題
#Problem #B1 好友滿天下
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

n=int(input())
#stat=[{"",set()} for i in range(n)]
stat=dict()
for i in range(n):
    
    ins=input().split(" ",1)
    if not ins[0] in stat:
        stat[ins[0]]=[ins[1]]
    else:
        if ins[1] not in stat[ins[0]]:
            stat[ins[0]].append(ins[1])
stat_key=sorted(stat)
for i in stat_key:
    print(i,len(stat[i]))
