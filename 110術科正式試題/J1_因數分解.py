#110商業技藝競賽正式試題
#Problem J 噁爛數
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
'''
除以2,3,5後若為1就是噁爛數
若不是就有不是2,3,5的因數且應該也為質數
(1應該不是噁爛數吧??---1竟然是噁爛數,在J2的測資有1)
'''
prime=[2,3,5]
while True:
    try:
        n=int(input())
        nums=list(map(int,input().split(" ")))
        for i in range(len(nums)):
            flag=False
            x=0
            t=nums[i]
            #print(t,flag)
            while True:
                if t%prime[x]==0:
                    t=t/prime[x]
                else:
                    x+=1
                if x>=len(prime):
                    if t==1:
                        flag=True
                    break
            print(str(flag))
                
    except Exception as e:
        break


