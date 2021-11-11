#109商業技藝競賽模擬試題
#Problem 3：子題1：西洋棋
'''
本題看是很難,但只要推論下去就知道只有4種情況,3種答案
(*如果會玩西洋棋的人,應該就馬上解出來*)
推論出來的結論:
1.同列同欄就同一位置,就0
2.2者有共同列或共同欄就1步
3.列相減絕對值與欄相減絕對值相同就在同一斜線上,就1步
4.其他情況就2,其實就先斜再直或先直再斜.
'''

n=int(input())
import datetime
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    if(x[0]==x[2] and x[1]==x[3]):#同位置
        print(0)
    elif(x[0]==x[2] or x[1]==x[3]):#同列或同欄
        print(1)
    elif(abs(x[0]-x[2])==abs(x[1]-x[3])):#同斜線
        print(1)
    else:
        print(2)
