#110商業技藝競賽正式試題
#Problem N 字串編輯距離
#Author: Yotrew Wing
#2021/12/02
'''
LCS的變形
'''

x=input().strip()
y=input().strip()

#(y,x):len(y)列,len(x)行,所以要倒著來
d=[[0 for i in range(0,len(x)+1)] for i in range(0,len(y)+1)  ]#為了避免指到同一個list,還是用for迴圈
for i in range(len(x)+1):
    d[0][i]=i
for i in range(len(y)+1):
    d[i][0]=i
for a in range(0,len(y)):
    for b in range(0,len(x)):
        if y[a]==x[b] :
            d[a+1][b+1]=d[a][b]
        else:
            d[a+1][b+1]=min(d[a+1][b]+1,d[a][b+1]+1,d[a][b]+1) #min(插入+1,刪除+1,取代+1)

print(d[len(y)][len(x)])

