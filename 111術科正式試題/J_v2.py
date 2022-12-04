#111商業技藝競賽正式試題
#Problem #J 質數
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#直接使用最簡單判斷質數方式求
import sys
n=int(input())

for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split(" "))
    if a>b:
        a,b=b,a #應該不會出現這種吧...
    for i in range(a,b+1):
        flag=True
        if i==1:
            flag=False
        if i%2==0 and i!=2:
            flag=False
        for j in range(3,int(i**0.5)+2,2): #+1不放心,就多做一個+2
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
