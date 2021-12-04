#110商業技藝競賽正式試題
#Problem B 閏年 (多列版)
#Author: Yotrew Wing
#2021/12/02

n=int(input())
for i in range(n):
    year=int(input())
    if(year==0):
        break
    if year % 4 != 0:
        print("a normal year")
    elif year% 400 ==0:
        print("a leap year")
    elif year% 4 ==0 and year% 100 !=0:
        print("a leap year")
    else:
        print("a normal year")

