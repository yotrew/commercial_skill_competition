#106商業技藝競賽正式試題
#Problem 2：子題2：幾A 幾B。(程式執行限制時間: 2 秒)
#109商業技藝競賽模擬試題Problem 2：子題2和
#107商業技藝競賽正式試題"Problem 2：子題 2：排列"的組合
'''
使用for loop,時間複雜度O(n),排序一般應該為O(nlon)
'''

n=int(input())
count=0
def recusive(sequence,curr_str,k):#sequence:還有多少數字,
    global count
    ret_str=""
    #print(sequence,x)
    
    for i in range(0,len(sequence)):
        temp=sequence.copy()
        temp.pop(i)
        ret_str=recusive(temp,curr_str+sequence[i],k)
        if(count==k):
            return ret_str
    if(len(sequence)==0):
        count+=1
        #print(curr_str,count)
        return curr_str
    else:
        return ret_str;
    
for i in range(0,n):
    x=input().split(",")#有空白要處理
    count=0 #<---要reset全域變數,不然會錯
    p1=recusive(list(x[0]),"",int(x[1]))
    #print(list(x[0]),count)
    count=0
    p2=recusive(list(x[0]),"",int(x[2]))
    #print(p1,p2)
    A=0
    B=0
    #print(x[0],len(x[0]),x[1],len(x[1]))
    for a in range(0,len(p1)):
        for b in range(0,len(p2)):
            if(a==b and p1[a]==p2[b]):
                A=A+1
                continue
            if(a!=b and p1[a]==p2[b]):
                B=B+1
                continue
    print("{}A{}B".format(A,B))
    

