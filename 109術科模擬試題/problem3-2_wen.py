#109商業技藝競賽模擬試題
#Problem 3：子題2：時間計算
#Author: wen
#2022/12/26
#https://github.com/yotrew/commercial_skill_competition
'''

'''
def leap(y): #判斷閏年函數
    if y%4==0 and y%100!=0:
        return True
    if y%400==0:
        return True
    return False
    
month=[0,31,28,31,30,31,30,31,31,30,31,30,31] #每個月的天數,0不用
n=int(input())
while n>0:
    c=int(input())
    n-=1
    y=1970 #

    #年
    while c>366: 
        if leap(y):
            c-=366
        else:
            c-=365
        y+=1
    
            
    m=1
    if leap(y):
        month[2]=29

    #月
    while c>month[m]:
        m+=1
        c-=month[m]

    #日 
    d=1+c
    
    print(f"{y}-{m:02d}-{d:02d}")
    
    month[2]=28 #因為有多筆輸入,因此重設2月的天數
