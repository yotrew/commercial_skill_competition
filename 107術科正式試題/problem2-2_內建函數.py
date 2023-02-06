#107商業技藝競賽正式試題
#Problem 2：子題 2：排列
#Author: Yotrew Wing
#2023/02/05
#求第n個排列組合的值
#*模擬試題有類似題,但那一題只要排序就可以了
#使用內建函數,不建議,不是所有程式語言都有內建排列/組合的功能
#比賽時不一定想得起來排列的英文,但IDLE可以用F1查
#https://github.com/yotrew/commercial_skill_competition

from itertools import permutations 
n=int(input())

for i in range(0,n):
    count=0
    x=input().split(",")    
    N=int(x[0])
    k=int(x[-1]) #k=int(x[len(x)-1])
    perm = list( permutations(x[1:-1])  )
    #print(perm)
    sequence = ["".join(i) for i in perm] #
    sequence.sort()  #排序
    print(sequence[k-1])


