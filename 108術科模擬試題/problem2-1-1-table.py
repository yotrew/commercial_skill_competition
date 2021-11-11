#108商業技藝競賽模擬試題
#Problem 2：子題 1：數字生成元。
#Author:Yotrew
#20210709
'''
abc=a*100+b*10+c
數字生成元的規則(以3位數來看)是 a*100+b*10+c+a+b+c=a*100+a+b*10+2*c
所就每個數字從0~9試各試一次,3位數共要試3*10=30,若從000~999要試1000次

#另一種方式是建表:https://www.itread01.com/content/1542367932.html
#反過來求,如同質數建表一樣
建表0~100000只需0.1sec
剩下的不管幾筆幾乎就幾ms以內
'''
import math

temp=[0 for i in range(0,100011)]
for i in range(0,100001):
    x=0#各個數字之和,如198==>1+9+8=18
    y=i
    while y>0:
        x+=y%10
        y=y//10
    #print(i+x)
    try:
        if(temp[i+x]==0 or temp[i+x]>i):#要取最小值
            temp[i+x]=i  #[(各個數字和x)+i]的生成數 = i ==>  [198+18=216]=198
    except IndexError:
        #print(i,x)
        '''以下會爆
            99992 9
            99993 9
            99994 9
            99995 9
            99996 9
            99997 9
            99998 9
            99999 9
        '''
        
n=int(input())
for i in range(0,n):
    x=int(input().strip())
    print(temp[x])
