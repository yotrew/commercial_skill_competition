#111商業技藝競賽正式試題
#Problem #K 質因數
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#UVa10699
#建質數表
#第1版的修改版,建表做加速的動作
import sys


pl=10**6+1
prime_table2=[True for i in range(pl)] 

for i in range(4,pl,2):
    prime_table2[i]=False
for i in range(3,int(pl**0.5)+1,2):
    if prime_table2[i]==False:
        continue
    for j in range(i*2,pl,i):
        prime_table2[j]=False
prime_table=[2]
for i in range(3,pl):
    if prime_table2[i]==True:
        prime_table.append(i)
#print(prime_table[-100:])
ptl=len(prime_table)

for line in sys.stdin.readlines():
    cnt=0
    i=0
    n=int(line)
    a=n
    if n==0:
        break
    while i<ptl and a>=prime_table[i]:
        if a%prime_table[i]==0:
            cnt+=1
            a=a//prime_table[i] #//加速用
        i+=1
    print(f"{n} : {cnt}")

        
'''
Sample Input 1
7
8
45
289384
930887
692778
636916
747794
238336
885387
760493
516650
641422
999999
0
Sample Output 1
7 : 1
8 : 1
45 : 2
289384 : 3
930887 : 2
692778 : 5
636916 : 4
747794 : 3
238336 : 3
885387 : 2
760493 : 2
516650 : 3
641422 : 3
999999 : 5
'''
