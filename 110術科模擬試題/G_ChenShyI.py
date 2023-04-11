#110商業技藝競賽模擬試題
#Problem G 格雷碼（Gray Code）
#Author: ChenShyI
#2023/04/11
#https://github.com/yotrew/commercial_skill_competition

l=int(input())
s=["0","1"]
if l>1:
    for j in range(l-1):
        s+=s[::-1]
        for i in range(len(s)):
            if i+1<=len(s)/2:
                s[i]="0"+s[i]
            else:
                s[i]="1"+s[i]
for i in s:
    print(i)
