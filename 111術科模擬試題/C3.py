#111商業技藝競賽模擬試題
#Problem #C3 加法進位
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
#
'''
1.讀入後轉成整數
2.使用%取餘數方式取得2數的最後一個數字,做相加(並加上進位數),若有進位count+1
  並取得進位數,做到2數都為0時停止
'''
while True:
    
    a,b=map(int,input().split(" "))
    if a==0 and b==0:
        break
    c=0   #進位數,最大為1,最小為0,因為2個個位數相加再加上進位數,不會超過19
    cnt=0 #count
    while a>0 or b>0:
        a1=a%10
        b1=b%10
        c=(a1+b1+c)//10
        a=a//10
        b=b//10
        if c>0:
            cnt+=1
    
    if cnt==0:
        print("No carry operation.")
    elif cnt==1:
        print(f"1 carry operation.")
    else:
        print(f"{cnt} carry operations.")

