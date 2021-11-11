#105商業技藝競賽正式試題
#Problem 2：數學問題 子題 2：最大公約數計算
#Author:Yotrew
#20210710
'''
最多5個數字做GCD,共有5!=120種組合

'''

def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)
    
n=int(input())

for i in range(0,n):
    in_str=list(map(int,input().strip().split(",")))
    ans=0
    for a in range(0,len(in_str)-1):
        for b in range(a+1,len(in_str)):#比過就不用重複比,如GCD(x[0],x[1])-->GCD(x[1],x[0])
            ans=max(GCD(in_str[a],in_str[b]),ans)
    print(ans)
    
    
