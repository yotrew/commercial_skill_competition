#107商業技藝競賽模擬試題
#Problem 3： 子題 1：集合
#二進位做法做法

#只有10個數字     
nums=[2**i for i in range(0,11)]
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

n=int(input())

import math
def out_str(a):
    if a==0:
        return "N"
    out_str="{"
    #for i in range(1,11):
    #print(a,int(math.log(a,2)))
    for i in range(1,int(math.log(a,2))+1):
        if(a&(2**i)>0):
            out_str+=str(i)+", "
        
    out_str+="}"
    
    return out_str.replace(", }","}")
for i in range(0,n):
    x=input().replace("},",";").replace("{","").replace("}","").replace(" ","").split(";")#小技巧
    #print(x)
    a=x[0].split(",")
    b=x[1].split(",")
    
    if(x[0]==""):#防止有空字串,但依測資來看,不必理它
        a=[]
    if(x[1]==""):
        b=[]
    a=list(map(int,a))
    b=list(map(int,b))
    a_num=0
    b_num=0
    for i in a:
        a_num+=nums[i]
    for i in b:
        b_num+=nums[i]
    
    #print(out_str(a_num|b_num)+", "+out_str(a_num&b_num)+", "+out_str((a_num|b_num)^b_num)+", "+out_str(a_num^b_num))
    #差集==> (A聯集B)對稱差集B  或是 (A交集B)對稱差集A
    print(out_str(a_num|b_num)+", "+out_str(a_num&b_num)+", "+out_str((a_num&b_num)^a_num)+", "+out_str(a_num^b_num))
    #print(x[0],x[1],"--",a,b)
