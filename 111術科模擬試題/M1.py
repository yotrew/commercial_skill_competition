#111商業技藝競賽模擬試題
#Problem #M 矩陣
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
ins=input().replace("[[","[").replace("]]","]").split("],[")

matrix=[]
matrix_out=[]

for i in ins:
    matrix.append(i.replace("[","").replace("]","").split(","))

m=len(matrix)

print("[",end="")

for i in range(m-1):
  print("[",end="")
  for j in range(m-1,0,-1):
    print(matrix[j][i],end=",")
  print(matrix[j-1][i],end="],") #每一列的最後一個

#最後一列
print("[",end="")
for j in range(m-1,0,-1):
  print(matrix[j][i+1],end=",")
print(matrix[j-1][i+1],end="") #每一列的最後一個
print("]]")
