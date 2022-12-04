#111商業技藝競賽正式試題
#Problem #J 質數
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#建質數表,求質數表要一段時間,所以只求到10*6,超過的就直接一個一個判斷是否為質數
import sys
pl=10**6
prime_table2=[True for i in range(pl)] 
prime_table2[0]=prime_table2[1]=False
for i in range(4,pl,2): #2的倍數
    prime_table2[i]=False
for i in range(6,pl,3): #3的倍數
    prime_table2[i]=False

for i in range(6,int(pl**0.5)+1,6):
    x=i-1
    for j in range(x*2,pl,x):
        prime_table2[j]=False
    x=i+1
    for j in range(x*2,pl,x):
        prime_table2[j]=False


n=int(input())

for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split(" ")) #用strip()不然會run-time error
    if a>b:
        a,b=b,a #應該不會出現這種吧...
    if b<pl:
        for i in range(a,b+1):
            if prime_table2[i]==True:
                sys.stdout.write(f"{i}\n") 
    else: #超過pl=10**6,用最簡單方式判斷是否為質數
        for i in range(a,b+1):
            flag=True
            if i==1:
                flag=False
            if i%2==0 and i!=2:
                flag=False
            for j in range(3,int(i**0.5)+1,2):
                if not flag:
                    break
                if i%j==0:
                    flag=False
                    break
            if flag==True:
                sys.stdout.write(f"{i}\n")      
    sys.stdout.write("\n")


'''
Sample Input 1
3
1 10
3 5
1000000 1000090

Sample Output 1
2
3
5
7

3
5

1000003
1000033
1000037
1000039
1000081

Sample Input
1
10000002 10002003

Sample Input
1
9999998 10001043
'''
