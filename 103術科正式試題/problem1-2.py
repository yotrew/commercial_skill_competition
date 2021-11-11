#103商業技藝競賽正式試題
#Problem 1：數學問題 子題 2：買郵票。(程式執行限制時間: 2 秒) 
#Author:Yotrew
#20210713
#就雞兔同籠問題
''''
n=int(input())
for i in range(0,n):
    z=list(map(int,input().strip().split(",")))
    a=z[0]
    b=z[1]
    c=z[2]
    d=z[3]
    x=0
    y=0
    for e in range(0,a+1):
        x=int(((d-c*e)/b))
        y=e
        if x+y==a and x>0 :
            break
    print(f"{x},{y}")#f-string

'''
#方法2:公式解
'''
a=x+y ==> y=a-x
bx+cy=d --代入y=a-x
bx+ca-cx=d--> bx-cx=d-ca --> x(b-c)=d-ca --> x= (d-ca)/(b-c)

a=x+y ==> x=a-y
bx+cy=d --代入x=a-y
ba-by+cy=d--> cy-by=d-ba --> y(c-b)=d-ba --> y= (d-ba)/(c-b)
'''
n=int(input())
for i in range(0,n):
    z=list(map(int,input().strip().split(",")))
    a=z[0]
    b=z[1]
    c=z[2]
    d=z[3]
    x= abs(int((d-c*a)/(b-c)))#有除法就會有小數
    y= abs(int((d-b*a)/(c-b)))
    print(f"{x},{y}")#f-string
