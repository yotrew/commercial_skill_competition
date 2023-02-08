#107商業技藝競賽模擬試題
#Problem 1：  子題2：邏輯表示式
#Author: Yotrew Wing
#2023/02/08
#偷懶做法,only for python
#會不會有測資不會過??
#https://github.com/yotrew/commercial_skill_competition

n=int(input())
for i in range(0,n):
    x=input().split("==")
    l=x[0].strip()#左邊
    r=x[1].strip()#右邊
    #print(eval(l),eval(r))
    if round(eval(l),1)==round(eval(r),1): #數字或含小數後一位數
        print("T")
    else:
        print("F")
    #print(a,ans)
