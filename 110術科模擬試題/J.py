#110商業技藝競賽模擬試題
#Problem J 約瑟夫斯問題
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
while True:
    try:
        a,b=tuple(map(int,input().split(" ")))
        c=[i for i in range(1,a+1)]
        b=b-1  
        d=b
        
        while len(c)>1:
            if d >= len(c):
                d=d%len(c)
            c.pop(d)
            d+=b
        print(c[0])
    except:
        break
