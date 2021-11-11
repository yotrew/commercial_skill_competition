#103商業技藝競賽正式試題
#Problem 1：數學問題 子題 1：判斷二個數字是否為孿生質數。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210713
#建表比較快(建質數表)
prime_table=[1 for i in range(0,65536)]#一開始假設全部為質數
prime_table[0]=0#0是質數嗎?但本題不會有0,和1
prime_table[1]=0#1是質數嗎?但本題不會有0,和1
for i in range(4,65536,2):
    prime_table[i]=0#2的倍數不會是質數
    
for i in range(3,65536,2):
    #print(i,int(i**0.5)+1)
    for a in range(3,int(i**0.5)+1,2):#有更快的方式,像6n-1,6n+1的方式跳,因為2*3=6,6的倍數也不會是質數
        if(i%a==0):
            prime_table[i]=0
            break
#print(prime_table)
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    if(x[1]-x[0]!=2):
        print("N")
    elif(prime_table[x[1]]==1 and prime_table[x[0]]==1):
        print("Y")
    else:
        print("N")
