#109商業技藝競賽模擬試題
#Problem 1：子題2：給一個整數數字，轉為羅馬數字符號。(程式執行限制時間: 2 秒)
#Author: wen
#2022/12/26
#https://github.com/yotrew/commercial_skill_competition
'''
使用10進位轉n進位方式解
如:10進位轉2進位
13轉1101(2)

13-8=5  ==>2^3=8位置係數1
5-4=1  ==>2^2=4位置係數1
1減2會變負  ==>2^1=2位置係數0
1-1=0  ==>2^0=1位置係數1
==>1101
'''
n=int(input())
lt=[['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100,],['CD',400],['D',500],['CM',900],['M',1000]]

while n>0:
    num=int(input())
    n-=1
    m=0
    while num > 0:
        for i in range(len(lt)):
            if lt[i][1] > num:
                break
            m=i
        num=num-lt[m][1]
        print(lt[m][0],end="")
    print()
    
