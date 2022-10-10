#110商業技藝競賽模擬試題
#Problem F 漢明距離（Hamming distance）--字串比對法
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
n=int(input())

for j in range(n):
    a=input()
    b=input()
    dist=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            dist+=1
    print(dist)
