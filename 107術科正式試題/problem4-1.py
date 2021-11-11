#107商業技藝競賽正式試題
#Problem 4：子題 1：樹(找2 節點之間最長路徑的長度)。
'''
推去規則,每多少個跳.
此去遇到某一邊是沒有的,會有問題
[1,2,null,4,5,null,null,8,9,10,11]
這個會出問題
'''
n=int(input())

for i in range(0,n):
    x=input().replace("[","").replace("]","").split(",")
    L=0 #左子樹深度
    R=0 #右子樹深度
    for l in range(1,7):#最深7層
        #print(l,(2**l-1),(2**l-1+2**(l-1)),(2**l-1+2**(l-1)),(2**l-1+2**(l)))
        for j in range(2**l-1,2**l-1+2**(l-1)):
            if j >= len(x):
                break
            if x[j]!="null":
                L=L+1
                break
        for j in range(2**l-1+2**(l-1),2**l-1+2**(l)):
            if j >= len(x):
                break
            if x[j]!="null":
                R=R+1
                break
    print(L+R)
    

