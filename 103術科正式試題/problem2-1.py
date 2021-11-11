#103商業技藝競賽正式試題
#Problem 2：字串 子題 1：在兩字串中，共同出現的英文字母。
#Author:Yotrew
#20210713

n=int(input())
for i in range(0,n):
    s1=input().strip()
    s2=input().strip()
    letter=[]
    if len(s1) < len(s2):
        s1,s2=s2,s1 #對調
    for a in s2:
        if a in s1:
            if not a in letter:
                letter.append(a)
    letter=sorted(letter,key=lambda x:x)
    if(len(letter)>0):
        print("".join(letter))
    else:
        print("N")
