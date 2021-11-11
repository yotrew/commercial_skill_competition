#107商業技藝競賽正式試題
#Problem 4：子題 1：樹(找2 節點之間最長路徑的長度)。
'''
推演規則:
就找每個點到另一個點的距離,以這2點為出發點,找到共同的祖先要經過多少edge
*基本上也不用每一點對每一點找

找父親就:int(n/2)
'''
n=int(input())

for i in range(0,n):
    x=input().replace("[","").replace("]","").split(",")

    max_paths=0
    for a in range(0,len(x)):#a,b是index
        
        if(x[a]=="null"):
            continue
        
        for b in range(0,len(x)):#a,b是index
            count=0
            if(x[b]=="null"):
                continue
            if a==b:#自己到自己
                continue

            L=a+1#程式中node 1的index是0,所以計算時要加回來,node 2的index是1
            R=b+1#node 3的index是2
            while L!=R:#找到共同祖先為止
                if(L>R):
                    L=int(L/2)
                    count+=1
                #if(c==d):#找到共同祖先為止
                    #break
                if(L<R):
                    R=int(R/2)
                    count+=1
            if(count>max_paths):
                max_paths=count
    print(max_paths)
