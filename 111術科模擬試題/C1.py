#111商業技藝競賽模擬試題
#Problem #C1 質數
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

prime_table=[2] 
prime_table2=[False for i in range(32769+1)] 
ftable=[False for i in range(32769+1)] #記錄是否被找過,加速用的
prime_table2[2]=True 

for i in range(2,32769):
    flag=True
    if i%2==0:
        flag=False
    for j in range(3,int(i**0.5)+1):
        if flag==False: #如果是偶數就直接break
            break
        if i%j==0:
            flag=False
            #break
    if flag==True:
        prime_table2[i]=True
        prime_table.append(i)
plen=len(prime_table)
while True:
    n=int(input().strip())
    if n==0:
        break
    cnt=0
    ft=ftable.copy()
    for i in range(plen):
        x=n-prime_table[i]
        if prime_table2[x]==True and ft[x]!=True:
            cnt+=1
        if prime_table[i]>n:
            break
        ft[x]=True
        ft[prime_table[i]]=True
    print(cnt)
'''
test data1:
8 
20
42
10
12
4
0
output:
1
2
4
2
1
1

'''
