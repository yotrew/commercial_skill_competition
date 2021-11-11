#Problem 3：
#子題2：最大子數列問題
#暴力法
N=int(input())
num=[]

for i in range(0,N):
    x=input().strip().split(" ")#有時候最後一行的最後一個空白會影響,python的問題
    #print(x)
    num.append(list(map(int,x)))

for i in range(0,N):
    max1=-65536
    for a in range(0,len(num[i])):
        count=0
        for b in range(a,len(num[i])):
            count=count+num[i][b]
            if max1<count:
                max1=count
    print(max1)
