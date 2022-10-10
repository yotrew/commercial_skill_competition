#110商業技藝競賽正式試題
#Problem I 123
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
n=int(input())
for i in range(n):
    word=input().strip()
    
    if len(word)==3:
        if word[-2:]=="ne" or word[0:2]=="on" or (word[0]=="o" and word[2]=="e"):
            print("1")
        else:
            print("2")
    else:
        print("3")


