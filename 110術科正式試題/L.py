#110商業技藝競賽正式試題
#Problem L 質數
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition

'''
1.建質數表(比較不會TLE)
2.取中間C*2個:
  因為從1~K取中間C*2,所以就是 K/2找出中間,以中間取前C個,和後C個
  所以就是起始點:K/2-C 終止點 K/2+C(起始點+2*C)
  但要判斷K是奇數還是偶數(若不判斷就用計算的:K%2=1 or 0)
'''
table=[1 for i in range(1001)]
prime=[1]#質數表
for i in range(4,1001,2):
    table[i]=0
for i in range(3,32,2):#1000^0.5=31.x
    for j in range(i*2,1001,i):
        table[j]=0
for i in range(2,1001):
    if(table[i]==1):
        prime.append(i)

while True:
    try:
        N,C=map(int,input().split(" "))
        pos=0

        for i in range(len(prime)):
            if prime[i]<=N:
                pos=i                
            else:
                break
        print(f"{N} {C}: ",end="")
        K=len(prime[0:pos+1])
        s=K//2-C+K%2
        e=s+2*C-K%2
        #print(s,e)
        if s<0:
            s=0
        if e>K:
            e=K
        for i in range(s,e-1):
            print(f"{prime[i]}",end=" ")

        print(f"{prime[e-1]}\n")
    except Exception as e:
        break


