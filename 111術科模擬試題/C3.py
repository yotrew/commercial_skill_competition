#111商業技藝競賽模擬試題
#Problem #C3 加法進位
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

while True:
    a,b=map(int,input().split(" "))
    if a==0 and b==0:
        break
    c=0
    cnt=0
    while a>0 or b>0:
        a1=a%10
        b1=b%10
        if (a1+b1+c)>10:  
            c=(a1+b1+c)//10
        else:
            c=(a1+b1+c)//10
        a=a//10
        b=b//10
        if c>0:
            cnt+=1
    
    if cnt==0:
        print(f"No carry operation.")
    elif cnt==1:
        print(f"{cnt} carry operation.")
    else:
        print(f"{cnt} carry operations.")

