#Problem 2：
#子題1：時間計算
#使用內建時間變數/函數來做處理
#因為只提供days的計算,所以要考慮閏年的問題
import datetime

N=int(input())

for i in range(0,N):
    a=input().strip()
    b=input().strip()
    #print(a,b)
    d1 = datetime.datetime.strptime(a, '%d/%m/%Y')
    d2 = datetime.datetime.strptime(b, '%d/%m/%Y')
    delta=d1-d2
    #print(int(delta.days/365))#不考慮閏年,所以會有問題
    #計算閏年
    c=int(a.split("/")[2])
    d=int(b.split("/")[2])
    e=int(a.split("/")[1])
    cnt=0
    for i in range(d,c+1):
        if(i==c and e<=2):
            continue#其實break也是一樣,最後一年是閏年,但月份未超過2月,就不計
        if i%400==0:
            cnt+=1
        elif i%4==0 and i%100!=0:
            cnt+=1
    #print(cnt,delta.days,(delta.days-cnt))
    print(int((delta.days-cnt)/365))#不考慮閏年,所以會有問題
'''
4
01/01/2020
01/01/2019
01/11/2020
02/11/2019
02/11/2020
01/11/2019
01/11/2020
01/11/2019
'''
