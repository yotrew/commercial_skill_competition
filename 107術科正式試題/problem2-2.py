#107商業技藝競賽正式試題
#Problem 2：子題 2：排列
#求第n個排列組合的值
#*模擬試題有類似題,但那一題只要排序就可以了
n=int(input())

count=0
def recusive(sequence,curr_str,k):#sequence:還有多少數字,
    global count
    ret_str=""
    for i in range(0,len(sequence)):
        temp=sequence.copy()
        temp.pop(i)
        ret_str=recusive(temp,curr_str+sequence[i],k)
        if(count==k):
            return ret_str
    if(len(sequence)==0):
        count+=1
        return curr_str
    else:
        return ret_str;

for i in range(0,n):
    count=0
    x=input().split(",")    
    N=int(x[0])
    k=int(x[-1]) #k=int(x[len(x)-1])
    sequence=x[1:-1].copy() #因為是排列其實可以直接用字串,不用轉Int.
    print(recusive(sequence,"",k))
    

