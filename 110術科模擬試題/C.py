#110商業技藝競賽模擬試題
#Problem C 票選動物
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
tiger=0
lion=0
for i in range(9):
    if input()=="Tiger":
        tiger+=1
    else:
        lion+=1
        
if tiger>lion:
    print("Tiger")
else:
    print("Lion")
