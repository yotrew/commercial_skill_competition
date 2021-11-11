#107商業技藝競賽模擬試題
#Problem 3： 子題 1：集合
#偷懶做法就直接使用python內建功能
#Ref:https://wenyuangg.github.io/posts/python3/python-set.html
'''
VB也有內建集合?LINQ
https://docs.microsoft.com/zh-tw/dotnet/visual-basic/programming-guide/concepts/linq/set-operations

'''
n=int(input())

for i in range(0,n):
    x=input().replace("},","};").split(";")#小技巧
    a=eval(x[0])
    b=eval(x[1])
    out_str=""
    if(len(a|b)==0):
        out_str+="N, "
    else:
        out_str+=str(a|b)+", "
    if(len(a&b)==0):
        out_str+="N, "
    else:
        out_str+=str(a&b)+", "
    if(len(a-b)==0):
        out_str+="N, "
    else:
        out_str+=str(a-b)+", "
    if(len(a^b)==0):
        out_str+="N"
    else:
        out_str+=str(a^b)+""
    print(out_str)
