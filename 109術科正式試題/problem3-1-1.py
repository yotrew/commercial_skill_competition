#Problem 3：
#子題1：迴文
#使用字串處理
N=int(input())
num=[]
for i in range(0,N):
    num.append(input().strip()) #去除字串前後空白:字串有前後空白問題

for i in range(0,N):
    A=num[i]
    while True:
        re_str=True #假設是迴文
        str_len=len(A)
        for j in range(0,int(str_len/2.0+0.5)):
            if A[j]!=A[str_len-j-1]:#只要第j個和第-j個不同就不是迴文
                re_str=False #只要
                A=str(int(A)+int(A[str_len::-1]))#不是迴文就A加上A的反轉
                
                break
        #print(A)
        if(re_str):#是迴文時印出字
            print(A)
            break
