#108商業技藝競賽模擬試題
#Problem 2：子題 1：數字生成元。
#Author:Yotrew
#20210709
'''
abc=a*100+b*10+c
數字生成元的規則(以3位數來看)是 a*100+b*10+c+a+b+c=a*100+a+b*10+2*c
所就每個數字從0~9試各試一次,3位數共要試3*10=30,若從000~999要試1000次

#另一種方式是建表:https://www.itread01.com/content/1542367932.html
'''
import math
n=int(input())
temp=[]
isGenNum=False
def gen_num(n,x,l):#num:要產生的數字串列,x輸入的數字,x的長度
    global isGenNum,temp
    if n>=l:
        k=0
        for a in range(0,l):#計算生成數
            k+=temp[a]*(10**(l-a-1))+temp[a]
        if(k==x):
            isGenNum=True
        return
    
    for i in range(0,10):#從小到大
        temp[n]=i
        gen_num(n+1,x,l)
        if(isGenNum):
            return
for i in range(0,n):
    x=input().strip()
    l=len(x)
    temp=[0 for i in range(0,7)]
    isGenNum=False
    display=False
    num=gen_num(0,int(x),l)
    
    if(isGenNum):
        for a in range(0,l):
            if(display==False and temp[a]>0):
                display=True
            if(display):
                print(temp[a],end="")
        print()
    else:
        print(0)
    
    
   
