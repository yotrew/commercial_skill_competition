#107商業技藝競賽正式試題
#Problem 2：子題 2：排列
#Author: Yotrew Wing
#2021/10/31
#求第n個排列組合的值
#*模擬試題有類似題,但那一題只要排序就可以了
#https://github.com/yotrew/commercial_skill_competition
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
    count=0
    x=input().split(",")    
    N=int(x[0])
    k=int(x[-1]) #k=int(x[len(x)-1])
    #sequence=list(map(int,x[1:-1])) #因為是排列其實可以直接用字串,不用轉Int.
    sequence=x[1:-1].copy() #因為是排列其實可以直接用字串,不用轉Int.
    #print(len(sequence))
    print(recusive(sequence,"",k))
    

