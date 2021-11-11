#107商業技藝競賽模擬試題
#Problem 2：數學問題 子題 1：排列。
#排序後,最後2個數對調...這麼簡單?_?(因為'排列'順序"第2大"的數,前面排列的說明是用來騙你的XD)

'''
n=int(input())
for i in range(0,n):
    x=input().strip().split(",")
    x=sorted(x,key=lambda y:y,reverse=True)
    tmp=x[-1]
    x[-1]=x[-2]
    x[-2]=tmp
    print("".join(x))

'''
'''
#正確做法應該如下:
'''
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

n=int(input())
for i in range(0,n):
    count=0
    x=input().strip().split(",")
    x=sorted(x,key=lambda y:y)#都要sorting了,就上面的做法比較快
    n = len(x)
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    print(recusive(x,"",fact-1))
