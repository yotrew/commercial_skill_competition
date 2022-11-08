#111商業技藝競賽模擬試題
#Problem #C2 數字次數
#Author: Yotrew Wing
#2022/11/08
#https://github.com/yotrew/commercial_skill_competition
#使用字串做法
n=int(input())
tnums=[0 for i in range(10)] #temp的次數統計表
for i in range(n):
    nums=tnums.copy() #複製次數統計表
    x=int(input().strip())
    for j in range(1,x+1):#1~N,使用字串的做法就不能多做一次0
        y=str(j)
        for a in y:
            nums[int(a)]+=1
    print(" ".join(map(str,nums)))
   
'''
test data1:
2
3
13
output:
0 1 1 1 0 0 0 0 0 0
1 6 2 2 1 1 1 1 1 1


test data2:
4
2
4122
319
7412

output:
0 1 1 0 0 0 0 0 0 0
1222 2256 2226 2222 1345 1222 1222 1222 1222 1222
61 172 162 82 62 62 62 62 62 62
2181 3285 3282 3281 3194 3181 3181 2594 2181 2181
'''
