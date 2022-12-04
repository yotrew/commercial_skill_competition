#111商業技藝競賽正式試題
#Problem #D 不重複隨機亂數產生器
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition

while True:
    try:
        input()
        a=set(map(int,input().split())) #因為要按數字大小排序,所以要轉成int,用set把重複的拿掉
        b=list(a) #轉回list
        b.sort()  #做排序
        print(len(b))
        print(" ".join(map(str,b)))
    except:
        break
'''
Sample Input 1
11
20 40 32 67 40 20 89 300 404 13 13

Sample Output 1
8
13 20 32 40 67 89 300 404
Sample Input 2
3
222
Sample Output 2
1
2
'''
