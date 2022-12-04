#111商業技藝競賽正式試題
#Problem #A2 閏年(0結束)
#110商業技藝競賽模擬試題
#Problem B4 閏年
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition

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
'''
Sample Input 1
1992
1991
1700
2400
0
Sample Output 1
a leap year
a normal year
a normal year
a leap year
'''
