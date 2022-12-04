#111商業技藝競賽正式試題
#Problem #B 壞掉的遙控器
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition

while True:
    try:
        a,b=map(int,input().split(" "))
        print((b-a)%200)  #共有200台,循環概念
    except:
        break
'''
Sample Input 1
5 11
Sample Output 1
6
Sample Input 2
199 2
Sample Output 2
3
'''
