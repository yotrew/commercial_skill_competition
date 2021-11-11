#107商業技藝競賽模擬試題
#Problem 4： 子題 1：最長共同子序列(Longest common subsequence)。
#按照題目給於的說明應該就可以推出規則
#因為只要輸出最長有多長,因此使用DP方式來解
#Author:Yotrew
#20210628
import pprint

n=int(input())

for i in range(0,n):
    x=input().strip()#測資應該沒那麼OOXX吧,給的第1個字串應該都會比第2個長
    y=input().strip()

    #(y,x):len(y)列,len(x)行,所以要倒著來
    d=[[0 for i in range(0,len(x)+1)] for j in range(0,len(y)+1)  ]

    for a in range(0,len(y)):
        for b in range(0,len(x)):
            if y[a]==x[b] :
                d[a+1][b+1]=d[a][b]+1
            else:
                d[a+1][b+1]=max(d[a+1][b],d[a][b+1])
    #print(d[a+1][b+1])
	print(d[len(y)][len(x)])
