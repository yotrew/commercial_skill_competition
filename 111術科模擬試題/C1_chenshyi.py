#111商業技藝競賽模擬試題
#Problem #C1 質數
#Author: chenshyi
#2023/04/20
#https://github.com/yotrew/commercial_skill_competition

m=[1 if i%2!=0 else 0 for i in range(2**15+1)]
m[2]=1
m[1]=0
for i in range(3,257,2):
    for j in range(i*2,2**15+1,i):
        m[j]=0
while True:
    l=[]
    n=int(input())
    if n==0:break
    for i in range(2,n):
        if m[i] and m[n-i]:
            al={i,n-i}
            if not 1 in al and not al in l:   
                l.append({i,n-i})
    print(len(l))
    
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
