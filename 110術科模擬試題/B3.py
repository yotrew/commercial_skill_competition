#110商業技藝競賽模擬試題
#Problem B3 閏年
#Author: Yotrew Wing
#2021/10/18

n=int(input())
year=[]
for i in range(n):
    year.append(int(input()))
for i in range(n):
    if year[i] % 4 != 0:
        print("Case %d: a normal year"%(i+1))
    elif year[i] % 400 ==0:
        print("Case %d: a leap year"%(i+1))
    elif year[i] % 4 ==0 and year[i] % 100 !=0:
        print("Case %d: a leap year"%(i+1))
    else:
        print("Case %d: a normal year"%(i+1))
