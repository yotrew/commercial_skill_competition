#111商業技藝競賽模擬試題
#Problem #C3 加法進位
#Author: wen
#2022/11/16
#https://github.com/yotrew/commercial_skill_competition
'''
字串做法
1.讀入測資後,找2數最大長度,把短的數補到和長的一樣長
2.一個一個數字從後面拆出來,
拆出來後2個數做相加並加上進位數,若有進位count+1,且保留進位數
'''
while True:
    n=list(input().split(" "))
    if n[0]=='0' and n[1]=='0':
        break
    c=0 #count
    a=max(len(n[0]),len(n[1]))
    n[0]='0'*(a-len(n[0]))+n[0]
    n[1]='0'*(a-len(n[1]))+n[1]
    
    b=0 #進位數,不是0就是1,2個個位數相加再加前一個進位,不會超過19
    for i in range(a-1,-1,-1):
        if int(n[0][i])+int(n[1][i])+b >= 10:
            #print(n[0][i],n[1][i])
            c+=1
            b=1
        else:
            b=0
    if c>1:
        print(f"{c} carry operations.")
    if c==1:
        print("1 carry operation.")
    if c==0:
        print("No carry operation.")
