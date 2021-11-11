#106商業技藝競賽正式試題
#Problem 1：子題2：給一個羅馬數字符號，轉為整數數字。(程式執行限制時間: 2 秒)
'''
109商業技藝競賽模擬試題的反解
'''

n=int(input())
roma={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

for i in range(0,n):
    x=input().strip()
    dec=0
    pos=0
    if(len(x)<=0):#應該不會沒有的出現
        continue
    #print(x)
    for a in range(0,len(x)-1):
        #print(roma[x[a]],roma[x[a+1]],a)        
        if roma[x[a]] == roma[x[a+1]] :
            dec+=roma[x[a]]
        if roma[x[a]] < roma[x[a+1]] :
            dec-=roma[x[a]]
        if roma[x[a]] > roma[x[a+1]] :
            dec+=roma[x[a]]
        
    dec+=roma[x[-1]]
    print(dec)
    #print("---")
    
