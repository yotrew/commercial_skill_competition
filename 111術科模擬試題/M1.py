#111商業技藝競賽模擬試題
#Problem #M 矩陣
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
'''
轉90度
欄變列,列變欄,因為只轉90度,所以從最後一列開始當做欄輸出
'''

matrix=eval(input()) #輸入字串是python串列格式,所以直接使用eval

m=len(matrix)

print("[",end="")

for i in range(m-1): #從最後一列開始
  print("[",end="")
  for j in range(m-1,0,-1): #
    print(matrix[j][i],end=",") #<--列當做欄輸出,[i,j]交換成[j,i]
  print(matrix[j-1][i],end="],") #每一列的最後一個

#最後一列
print("[",end="")
for j in range(m-1,0,-1):
  print(matrix[j][i+1],end=",")
print(matrix[j-1][i+1],end="") #每一列的最後一個
print("]]")
'''


test data1:
[[1,2,3],[4,5,6],[7,8,9]]

output:
[[7,4,1],[8,5,2],[9,6,3]]


test data2:
[[20,19,18,17],[16,15,14,13],[12,11,10,9],[8,7,6,5]]

output:
[[8,12,16,20],[7,11,15,19],[6,10,14,18],[5,9,13,17]]
[[8,12,16,20],[7,11,15,19],[6,10,14,18],[5,9,13,17]]
'''
