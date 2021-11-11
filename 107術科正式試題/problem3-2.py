#107商業技藝競賽正式試題
#Problem 3：子題 2：模數 (Modulo)
'''
暴力法,但暴力法為n^3,會太慢嗎?(但通常商科技藝競賽不太會有限制時間,即使限制,也2秒)
看起來有點慢-->AC (0.9s, 3.4MB)
應該可以推去規則,每多少個跳
'''
n=int(input())

for i in range(0,n):
    x=list(map(int,input().split(" ")))
    count=0
    for a in range(x[0],x[1]+1):
        for b in range(x[2],x[3]+1):
            for m in range(x[4],x[5]+1):
                if ((a+b) % m)==((a-b) % m):
                    count+=1
    print(count)
    

