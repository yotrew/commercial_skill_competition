#110商業技藝競賽模擬試題
#Problem B4 閏年
#Author: Yotrew Wing
#2021/10/18

while True:
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
