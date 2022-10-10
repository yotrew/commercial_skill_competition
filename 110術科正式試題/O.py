#110商業技藝競賽正式試題
#Problem O 最長共同子序列LCS(Longest common subsequence)
#Author: Yotrew Wing
#2021/12/02
#按照題目給於的說明應該就可以推出規則
#因為只要輸出最長有多長,因此使用DP方式來解
#https://github.com/yotrew/commercial_skill_competition

x=input().strip()#測資應該沒那麼OOXX吧,給的第1個字串應該都會比第2個長
y=input().strip()
z=input().strip()

#(y,x):len(y)列,len(x)行,所以要倒著來
d= [[[0 for k in range(0,len(z)+1)] for i in range(0,len(x)+1)] for j in range(0,len(y)+1)] #為了避免指到同一個list,還是用for迴圈

for c in range(0,len(z)):
    for a in range(0,len(y)):
        for b in range(0,len(x)):
            if y[a]==x[b] and z[c]==y[a] :
                d[a+1][b+1][c+1]=d[a][b][c]+1
            else:
                d[a+1][b+1][c+1]=max(d[a][b+1][c+1],d[a+1][b][c+1],d[a+1][b+1][c])

print(d[len(y)][len(x)][len(z)])
