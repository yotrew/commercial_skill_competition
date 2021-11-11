n=int(input("輸入n:"))
table=[1 for i in range(n+1)]
sqrt_n=int(n**0.5)+1
#ref:https://zh.wikipedia.org/wiki/%E8%B3%AA%E6%95%B8%E5%88%97%E8%A1%A8
for i in range(4,n+1,2):
    table[i]=0
for i in range(6,n+1,3):
    table[i]=0
for a in range(1,sqrt_n//6+1):
    for i in range((6*a-1)*2,n+1,6*a-1):
        table[i]=0
    for i in range((6*a+1)*2,n+1,6*a+1):
        table[i]=0
cnt=0
for i in range(2,n+1):
    if(table[i]==1):
        cnt+=1
        print(i)
print("-"*10)
print(f"{cnt}個")
