#111商業技藝競賽正式試題
#Problem #E 重複隨機亂數統計
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#統計
while True:
    try:
        input()
        cnt=[0 for i in range(1000+1)] #0不用,最多就1000個數,且已經排序好
        nums=list(map(int,input().split(" ")))
        for i in nums:
            cnt[i]+=1
        for i in range(1,1000+1):#count不是0就輸出
            if cnt[i]!=0:
                print(i,cnt[i])
    except:
        break
'''
Sample Input 1
11
20 40 32 67 40 20 89 300 404 13 13
Sample Output 1
13 2
20 2
32 1
40 2
67 1
89 1
300 1
404 1
Sample Input 2
4
2221
Sample Output 2
1 1
2 3
'''
