#108商業技藝競賽模擬試題
#Problem 3：子題 1：費氏數列。
#Author:Yotrew
#20210709
'''
大數問題
在python中直接解,VB也有大數的型態,
正規做法是用array來做(選手做法problem3-1.vb)
'''
n=int(input())
for i in range(0,n):
    x=int(input())
    n1=0
    n2=1
    n3=n1
    for i in range(1,x):
        n3=n1+n2
        n1=n2
        n2=n3

    print(n2)

