#111商業技藝競賽正式試題
#Problem N 進步獎
#111年TQC資訊月 五、最長遞增子序列的長度判斷
#2020來恩盃:第 3 題 以遞增取數由一亂數數列取出最多個整數

#Author:Yotrew Wing
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#LIS最長遞增子字串

n=int(input())
nums=list(map(int,input().split(" ")))
dp=[1 for i in range(len(nums))]
max_cnt=0
for i in range(len(nums)-1,0,-1):
    for j in range(i-1,-1,-1):
        if nums[i]>nums[j] and (dp[i]+1)>dp[j]:
            dp[j]=dp[i]+1
            #rint(dp,i,j)
print(max(dp))

'''
Sample Input 1
11
20 40 32 67 40 20 89 300 404 13 13
Sample Output 1
6
說明 6 -: 20 32 40 89 300 404
Sample Input 2
3
222
Sample Output 2
1
'''
'''
動態規劃解法:
DP存的是目前這個數字之前有多少個連續遞增數字
如果第i個數字比第j個數字還要大,且第j個的DP個數+1比第i個還要大,
第i個DP更新為第j個的DP個數+1
如:
num=[1 3 5 4 10]
dp= [1 1 1 1 1] #初始化為1,自己要算進去
第1 round
i=0
nums[0]=1
dp=[1] 不動

第2 round
i=1
nums[i]=3
從第i-1個往前看
j=0
nums[j]=1 < nums[i]=3
dp[i]<dp[j]+1
dp[i]=dp[j]+1=2

第3 round
i=2
nums[2]=5
從第i-1個往前看
j=1
nums[j]=3 < nums[i]=5
dp[i]<dp[j]+1
dp[i]=dp[j]+1=3

j=0
nums[j]=1 < nums[i]=5
dp[i]<dp[j]+1,不動
'''
