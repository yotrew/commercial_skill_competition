#Problem 1：
#子題1：找出最大和第二大的數字。(程式執行限制時間: 2 秒)

n=int(input())
for i in range(1,n+1):
  data=list(map(int,input().split()))
  data.sort(reverse=True) #直接使用排序...XD
  print(data[0],end=" ")
  y=data[0]
  flag=True
  for x in data:
    if(y!=x):
      print(x)
      flag=False
      break
  if flag:
    print(y)
