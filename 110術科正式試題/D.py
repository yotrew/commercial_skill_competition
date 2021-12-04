#110商業技藝競賽正式試題
#Problem D 最⼤偶數和
#Author: Yotrew Wing
#2021/12/02
'''
排序與總和
'''
n=input()
'''while True:
    try:'''
num=list(map(int,list(input().split(" "))))
num.sort()
sum1=sum(num)
i=0
while True:
    if sum1%2==0: #總和是偶數就直接跳掉
        break
    if num[i]%2==1:#總和是奇數就減掉最小奇數
        sum1-=num[i]
        break
    i+=1
print(sum1)

'''except :
        break'''
'''
test data:
5
2 3 1 4 5

5
2 3 4 1 5
'''
