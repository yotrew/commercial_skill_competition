#109商業技藝競賽模擬試題
#Problem 2：子題1：找出最大的數字。(程式執行限制時間: 2 秒)
'''
使用for loop,時間複雜度O(n),排序一般應該為O(nlon)
'''

n=int(input())

for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    max_num=x[0]
    for a in range(1,len(x)):
        if max_num < x[a]:
            max_num=x[a]
    
    print(max_num)
    
