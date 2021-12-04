#110商業技藝競賽正式試題
#Problem F 抱怨值問題

#Author: Yotrew Wing
#2021/12/02

n=int(input())
while True:
    try:
        nums=list(map(int,input().split(" ")))
        cnt=0
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]<nums[j]:
                    cnt+=1
        print(cnt)
    except Exception as e:
        break


