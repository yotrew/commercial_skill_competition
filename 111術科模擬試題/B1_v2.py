#111商業技藝競賽模擬試題
#Problem #B1 好友滿天下
#Author: Yotrew Wing
#2022/11/08
#https://github.com/yotrew/commercial_skill_competition
'''
本題名字不會重覆,所以只需要統計國家出現次數
'''
n=int(input())
#stat=[{"",set()} for i in range(n)]
stat=dict()
for i in range(n):
    
    ins=input().split(" ",1)
    if not ins[0] in stat:
        stat[ins[0]]=1
    else:
        #if ins[1] not in stat[ins[0]]: #<---名字不會重覆不用做
        stat[ins[0]]+=1
stat_key=sorted(stat)
for i in stat_key:
    print(i,stat[i])
