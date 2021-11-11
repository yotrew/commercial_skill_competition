#110商業技藝競賽模擬試題
#Problem B2 閏年
#Author: Yotrew Wing
#2021/10/18

n=int(input())
year=[]
for i in range(n):
    year.append(int(input()))
for i in range(n):
    if year[i] % 4 != 0:
        print("a normal year")
    elif year[i] % 400 ==0:
        print("a leap year")
    elif year[i] % 4 ==0 and year[i] % 100 !=0:
        print("a leap year")
    else:
        print("a normal year")
