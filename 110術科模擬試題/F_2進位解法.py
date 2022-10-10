#110商業技藝競賽模擬試題
#Problem F 漢明距離（Hamming distance）
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
n=int(input())

for j in range(n):
    a=int(input(),2)
    b=int(input(),2)
    c = a ^ b #a xor b
    dist=0
    while c !=0:
        if c&1==1:
            dist+=1
        c=c>>1 #向右位移
        
    print(dist)
