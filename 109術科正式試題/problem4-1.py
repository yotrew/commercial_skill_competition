#Problem 4：
#子題1：錄音帶(程式執行限制時間: 2 秒)
#背包問題,使用DP解
data=[]
try:
    while True:
        x=input()
        if(len(x.strip())==0):
            break
        data.append(list(map(int, x.split(" "))))
except :
    pass
for i in range(0,len(data)):
    dp=[0] *(data[i][0]+1) #[x]*n 如果[x]是list會有問題<--參考107商業技藝競賽正式試題 #Problem 4：子題 1。

    for j in range(data[i][1]):
        for k in range(data[i][0],data[i][j+2]-1,-1):
            if dp[k] < (dp[k-data[i][j+2]]+data[i][j+2]):
                dp[k] = (dp[k-data[i][j+2]]+data[i][j+2])
    print(dp[data[i][0]])
