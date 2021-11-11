#103商業技藝競賽正式試題
#Problem 2：字串 子題 2：計算兩個人之間共同朋友的數量。
#Author:Yotrew
#20210713
#同題1
n=int(input())
for i in range(0,n):
    s1=input().strip().split(" ")
    s2=input().strip().split(" ")
    s1.remove(s1[0])
    s2.remove(s2[0])
    letter=[]
    for a in s2:
        if a in s1:
           letter.append(a)
    print(len(letter))
    
