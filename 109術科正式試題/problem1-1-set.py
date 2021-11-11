#Problem 1：
#子題1：找出最大和第二大的數字。(程式執行限制時間: 2 秒)
#使用Python set容器來處理
n=int(input())
import time
# 開始測量
start = time.time()
for i in range(1,n+1):
  data=set(list(map(int,input().split())))
  data=list(sorted(data))
  print(data[-1],end=" ")
  if(len(data)==1):
    print(data[0])
  else:
    print(data[-2])
# 結束測量
end = time.time()
# 輸出結果
print("執行時間：%f 秒" % (end - start))
