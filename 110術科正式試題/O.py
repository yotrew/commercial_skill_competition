#110商業技藝競賽正式試題
#Problem O 最長共同子序列LCS(Longest common subsequence)
#Author: Yotrew Wing
#2021/12/02
#按照題目給於的說明應該就可以推出規則
#因為只要輸出最長有多長,因此使用DP方式來解
#https://github.com/yotrew/commercial_skill_competition

x=input()
y=input()
z=input()

d= [[[0 for k in range(0,len(z)+1)] for i in range(0,len(y)+1)] for j in range(0,len(x)+1)] #為了避免指到同一個list,還是用for迴圈

for a in range(0,len(x)):
    for b in range(0,len(y)):
        for c in range(0,len(z)):
            if x[a]==y[b] and y[b]==z[c] :
                d[a+1][b+1][c+1]=d[a][b][c]+1
            else:
                d[a+1][b+1][c+1]=max(d[a][b+1][c+1],d[a+1][b][c+1],d[a+1][b+1][c])

print(d[len(x)][len(y)][len(z)])
