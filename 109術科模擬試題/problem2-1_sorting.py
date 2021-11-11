#109商業技藝競賽模擬試題
#Problem 2：子題1：找出最大的數字。(程式執行限制時間: 2 秒)
'''
倒著排序,第1個值就最大值
'''

n=int(input())

for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    x=sorted(x,key=lambda x:x,reverse=True)
    print(x[0])
    
