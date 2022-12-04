#111商業技藝競賽正式試題
#Problem O 硬幣
#Author:Yotrew Wing
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#動態規劃,背包問題變形

n,value=map(int,input().split(" "))
coin=list(map(int,input().split(" ")))
c=[0 for i in range(value+1)]
c[0]=1
for i in range(n):
    for j in range(coin[i],value+1):
        c[j]+=c[j-coin[i]]
print(c[value])
'''
Sample Input 1
3 9
2 3 5
Sample Output 1
3
Sample Input 2
3 10
2 3 5
Sample Output 2
4
Sample Input 3
3 6
2 3 5
Sample Output 3
2

'''
