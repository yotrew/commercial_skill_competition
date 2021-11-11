#105商業技藝競賽正式試題
#Problem 1：字串問題 子題 摩斯電碼。(程式執行限制時間: 2 秒) 
#Author:Yotrew
#20210710

'''
直接建表,查表
也可以使用類似羅馬數字(迴圈)方式做
'''
n=int(input())
moose_table={"-----":0,".----":1,"..---":2,"...--":3,"....-":4,".....":5,
      "-....":6,"--...":7,"---..":8,"----.":9}
'''
#沒空格的做法,但此題有
for i in range(0,n):
    x=input().strip()
    for a in range(0,len(x)//3,5):
        print(moose_table[x[a:a+5]],end="")
'''

for i in range(0,n):
    x=input().strip().split(" ")
    for a in x:
        print(moose_table[a],end="")
    print()#換行
