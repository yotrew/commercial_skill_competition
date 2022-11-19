#商科技藝競賽109年problem4-2
#Author: Yotrew Wing
#2022/11/19
#https://github.com/yotrew/commercial_skill_competition
'''
#方法1:python內建排序及tuple做多欄位排序
#要倒著排序的欄位值,加上一個負號就會倒著排
'''
stus=[]
n=int(input())
for _ in range(n):
    stus.append(list(map(int,input().strip().split(" "))))

'''
#錯誤方法
#Python中使用多欄位排序(使用tuple)
#stus=sorted(stus, key = lambda stus : (stus[0],-stus[2],-stus[1]))
要倒著回來,權重較低的先排
以下為正確方法
'''

#Python中使用多欄位排序(使用tuple),依照第1個欄位stus[1]排,再排第2個欄位-stus[2],最後排第3個欄位stus[0]
stus=sorted(stus, key = lambda stus : (-stus[1],-stus[2],stus[0])) #加上負號為倒著排

for i in stus:
    print(" ".join(map(str,i)))

'''
test data1:
9 
1 90 100
2 75 60
3 90 100
4 75 70
5 75 60
6 85 90
7 80 95
8 62 78
9 65 73
'''
