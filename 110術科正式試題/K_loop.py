#110商業技藝競賽正式試題
#Problem K 求餘數
#Author: Yotrew Wing
#2022/12/05
'''
照題目說明做(同餘),但
(B^P) mod M = (B^(P/2) mod M) × (B^(P/2) mod M)
只需做一次(B^(P/2) mod M),不要一直讓它遞迴下去
ex.
if P%2==1: #奇數
    x=BP(B,P//2,M) #-->不要return (BP(B,1,M)%M)*(BP(B,P//2,M)%M)*(BP(B,P//2,M)%M)
    return (BP(B,1,M)%M)*(x%M)*(x%M)
else:
    x=BP(B,P//2,M)
    return (x%M)*(x%M)

迴圈(loop)解法:
觀察之後會發現
(B^P)%M=((B^P/2)%M)*((B^P/2)%M)
(B^P/2)%M=((B^P/4)%M)*((B^P/4)%M)
做到P/2==1時
(B^1)%M=B%M
也就是會變的是B

ex.
求7^4%M
7^4%M=(7^2%M)*(7^2%M) #偶數次方
7^2%M=(7^1%M)

求7^5%M 
7^5%M=7*(7^2%M)*(7^2%M) #奇數次方
7^2%M=(7^1%M)

求7^7%M
7^7%M=7*(7^3%M)*(7^3%M) #奇數次方
7^3%M=7*(7^1%M)*(7^1%M)  #奇數次方

求7^8%M
7^8%M=(7^4%M)*(7^4%M) #偶數次方
7^4%M=(7^2%M)*(7^2%M) #偶數次方
7^2%M=(7^1%M)

最後一定就是到B的1次方
所以解法就是先求出次方的變化
ex.求7^7%M
7//2=3 --> 7*(x%M)*(x%M)=y
3//2=1 ==> 7%M =x        (由下往上看)
答案就y
ex.求7^8%M
8//2=4 --> (y%M)*(y%M)=z
4//2=2 --> (x%M)*(x%M)=y
2//2=1 ==> 7%M = x        (由下往上看)
答案就z
'''


while True:
    try:
        X=int(input())
        Y=int(input())
        M=int(input())
        p=[]
        y=Y #避免改到輸入,但這一題沒有差
        while y>1:
            p.append(y)
            y=y//2
        #print(p)
        B=X #下面(B%M)*(x%M)*(x%M),也可以直接用X
        x=(B%M)
        for i in p[-1::-1]:
            if i%2==1: #奇數次方
                x=(B%M)*(x%M)*(x%M)
            else: #偶數次方
                x=(x%M)*(x%M)
        print(x%M)
        
        input()#空白行
    except Exception as e:
        #print(e)
        break
