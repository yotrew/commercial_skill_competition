#110商業技藝競賽正式試題
#Problem P 錢幣
#Author: Yotrew Wing
#2021/12/02

'''
背包問題:
ex.
4 2 2 5
把所有的錢幣總和當作背包的負重: 4+2+2+5=13
然後一個一個coin當做一個一個背包的item放到背包中
             0  1  2  3  4  5  6  7  8  9 10 11 12 13
item(0)      0  0  0  0  0  0  0  0  0  0  0  0  0  0
item(1)      0  0  0  0  4  4  4  4  4  4  4  4  4  4
item(1,2)    0  0  2  2  4  4  6  6  6  6  6  6  6  6
item(1,2,3)  0  0  2  2  4  4  6  6  8  8  8  8  8  8
item(1,2,3,4)0  0  2  2  4  5  6  7  8  9  9 11 11 13

時間複雜度最大為: 100(個錢幣)*1000(每個最大面額)*N(輸入錢幣個數,假設最大為100)
100*10000*100=10,000,000(1千萬)
N*1000*N=1000N^2

'''
n=int(input())
coins=list(map(int,input().split(" ")))
load=sum(coins)
cost=[0 for i in range(load+1)]

for i in coins:
    for j in range(load,i-1,-1):
        if cost[j-i]+i <= j & cost[j-i]+i > cost[j]:
            cost[j]=cost[j-i]+i

cost.sort()
out=(set(cost))
out.remove(0)#移掉0
print(len(out))
print(" ".join(map(str,out)))
