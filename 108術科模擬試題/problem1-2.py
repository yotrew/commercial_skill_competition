#108商業技藝競賽模擬試題
#Problem 1：子題 2：鬧鈴時間計算。
#Author:Yotrew
#20210709
'''
#類似109商業技藝競賽正式試題_p2-1時間計算,"最小公倍數問題",(*時鐘跑幾圈,*操場跑幾圈)
解法:就以每天的00:00為起點,看2個時間距離上點多遠(都轉換成分鐘比較好算)
     若第2個時間距離此點比較進就代表繞了一圈(本題隱藏題意就是最多隔一天,不會大於2天)
'''
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    start=x[0]*60+x[1]
    end=x[2]*60+x[3]
    if end < start:
        print((end+24*60)-start)
    else:
        print(end-start)

'''
#一般人第1個想法的解法
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    if x[2]>=x[0] and x[3]>=x[1]:
        print((x[2]-x[0])*60+(x[3]-x[1]))
    elif x[2]>x[0] and x[3]<x[1]:
        print((x[2]-x[0])*60+(x[3]-x[1]))
    elif x[2]==x[0] and x[3]<x[1]:
        print(24*60+x[3]-x[1])
    else:#elif x[2]<x[0] and x[3]<x[1]: #應該所有條件都考慮了吧?_?
        print(24*60+(x[2]-x[0])*60+(x[3]-x[1]))
'''
'''
test data1:
5 
10 23 10 24 
10 23 10 22 
1 5 21 10 
1 30 4 20 
21 33 20 11 

output:
1 
1439 
1205 
170 
1358

#--------
test data2:
7 
2 1 1 12 
3 55 2 11 
1 5 3 5 
21 34 15 32 
23 59 0 34 
21 33 21 10 
13 22 13 21

output:
1391 
1336 
120 
1078 
35 
1417 
1439 
'''


