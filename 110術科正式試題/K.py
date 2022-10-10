#110商業技藝競賽正式試題
#Problem K 求餘數
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
'''
照題目說明做,但
(B^P) mod M = (B^(P/2) mod M) × (B^(P/2) mod M)
只需做一次(B^(P/2) mod M),不要一直讓它遞迴下去
ex.
if P%2==1: #奇數
    x=BP(B,P//2,M) #-->不要return (BP(B,1,M)%M)*(BP(B,P//2,M)%M)*(BP(B,P//2,M)%M)
    return (BP(B,1,M)%M)*(x%M)*(x%M)
else:
    x=BP(B,P//2,M)
    return (x%M)*(x%M)
'''

def BP(B,P,M):
    #print(B,P,M)
    if P==1:
        return B
    if P%2==1: #奇數
        x=BP(B,P//2,M) #-->不要return (BP(B,1,M)%M)*(BP(B,P//2,M)%M)*(BP(B,P//2,M)%M)
                       #    這樣就少掉一次的遞迴
        return (BP(B,1,M)%M)*(x%M)*(x%M)
    else:
        x=BP(B,P//2,M)
        return (x%M)*(x%M)
    
while True:
    try:
        X=int(input())
        Y=int(input())
        M=int(input())
        print(BP(X,Y,M)%M)
        input()#空白行
    except Exception as e:
        break
