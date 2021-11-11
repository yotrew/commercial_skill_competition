#106商業技藝競賽正式試題
#Problem 2：子題 1：信用卡卡號
'''
'''

n=int(input())
    
for i in range(0,n):
    x=list(map(int,input()))
    ans=0
    for a in range(0,len(x)):
        if(a%2==0):
            if(x[a]*2>=10):
                ans+=x[a]*2-9
            else:
                ans+=x[a]*2
        else:
            ans+=x[a]

    if((ans%10)==0):
        print("T")
    else:
        print("F")
    
