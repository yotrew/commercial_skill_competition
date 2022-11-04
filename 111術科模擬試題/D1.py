#111商業技藝競賽模擬試題
#Problem #D1 字串
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition


at=[0 for i in range(27)] #0~26,0不用
#bt=[0 for i in range(27)]
while True:
    try:
        a=list(input())
        b=list(input())
        a_times=at.copy()
        b_times=at.copy()
        #print(a,b)
        for i in a:
            a_times[ord(i)-96]+=1
            
        for i in b:
            b_times[ord(i)-96]+=1
        
        for i in range(1,27):
            if a_times[i]>0 and b_times[i]>0:
                print(chr(i+96)*min(a_times[i],b_times[i]),end="")
        print()
    except:
        break
        
'''
test data1:
pretty
women
walking
down
the
street

output:
e
nw
et


test data2:
inging
singing
abc

efg


ghi
a
a

output:
ggiinn



a
'''
