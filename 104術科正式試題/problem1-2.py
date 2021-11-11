#104商業技藝競賽正式試題
#Problem 1：生活問題 子題 2：子題 2：樂透。
#Author:Yotrew
#20210711
'''
本題為排列組合的組合問題:
方法1:就爆力法,1個一個去比對-->想法最簡單,程式碼最長(如problem1-2.vb)
方法2:查表法,答案就固定5種,找出最中最多號碼
      -->比方法3容易想,但要推出中3個號碼的答案
      -->雖然偷吃步,但比賽就是求快,而從題目中找尋關鍵答案也是一種技巧
      1:0,0,0,0
      2:4,0,0,0
      3:3,3,0,0
      4:0,4,2,0
      5:0,0,5,1
方法3:數學的組合-->選手有辦法在比賽中想出來嗎?
      若最多有中4種
      中2種:
      C(4,2)*C(6-4,5-2)  <--C(4,2)中4碼中取出2種共有多少種,
                          C(2,3):因為不能重複,自選6碼中只剩2碼,要做3碼變化
                                 這是不可能,所以0種
      中3種:
      C(4,3)*C(6-4,5-3)  <--C(4,3)中4碼中取出3種共有多少種,
                          C(2,2):因為不能重複,自選6碼中只剩2碼,要做2碼變化
                                 總共4*1=4種                    
'''
def C(n,k):
    if k>n:
        return 0
    if n==k:
        return 1
    f=1
    a=n-k
    if(k<a):
        k,a=a,k
        
    for i in range(k+1,n+1):
        f=f*i
    for i in range(2,a+1):
        f=f/i
    return int(f)
    
#print(C(4,3))
n=int(input())
l=list(map(int,input().strip().split(",")))

for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    
    cnt=0
    for a in x:
        if a in l:
            cnt+=1
    #print(cnt)
    for b in range(2,5):
        print(C(cnt,b)*C(6-cnt,5-b),end=",")
    print(C(cnt,5)*C(5,5-5))

'''
#方法2:
table=["0,0,0,0","0,0,0,0","4,0,0,0","3,3,0,0","0,4,2,0","0,0,5,1"]
n=int(input())
l=list(map(int,input().strip().split(",")))

for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    
    cnt=0
    for a in x:
        if a in l:
            cnt+=1
    print(table[cnt])
'''

    
