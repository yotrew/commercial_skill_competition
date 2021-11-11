#107商業技藝競賽模擬試題
#Problem 3： 子題 1：集合
#使用Array(List)做法
n=int(input())

def union(a,b):#聯集
    tmp=a.copy()
    for i in b:
        if i not in tmp:#C語言要自己for loop來做比較
            tmp.append(i)

    tmp=sorted(tmp,key=lambda x:x)#因為不知道順序是不是亂的,在數學上set應該是沒順序,但輸出結果不能有不一樣
    #print(a,len(a))
    out_str="{"
    for i in range(0,len(tmp)-1):
        out_str+=tmp[i]+", "
    if(len(tmp)>0):
        out_str+=tmp[-1]+"}"
    else:
        out_str="N"
    #print("union",out_str)
    return out_str

def intersection(a,b):#交集
    tmp=[]
    for i in b:
        if i in a:
            tmp.append(i)
    tmp=sorted(tmp,key=lambda x:x)
    out_str="{"
    #print("intersection",tmp)
    for i in range(0,len(tmp)-1):
        out_str+=tmp[i]+", "
    if(len(tmp)>0):
        out_str+=tmp[-1]+"}"
    else:
        out_str="N"
    #print("intersection",out_str)
    return out_str

def difference(a,b):#差集
    tmp=a.copy()
    for i in b:
        if i in a:
            tmp.remove(i)
    tmp=sorted(tmp,key=lambda x:x)
    out_str="{"
    for i in range(0,len(tmp)-1):
        out_str+=tmp[i]+", "
    if(len(tmp)>0):
        out_str+=tmp[-1]+"}"
    else:
        out_str="N"
    #print("difference",out_str)
    return out_str

def symmetric_difference(a,b):#對稱差集
    tmp=a.copy()
    for i in b:
        if i not in tmp:#C語言要自己for loop來做比較
            tmp.append(i)
        else:
            tmp.remove(i)

    tmp=sorted(tmp,key=lambda x:x)#因為不知道順序是不是亂的,在數學上set應該是沒順序,但輸出結果不能有不一樣
    #print(a,len(a))
    out_str="{"
    for i in range(0,len(tmp)-1):
        out_str+=tmp[i]+", "
    if(len(tmp)>0):
        out_str+=tmp[-1]+"}"
    else:
        out_str="N"
    #print("symmetric_difference",out_str)
    return out_str

for i in range(0,n):
    x=input().replace("},",";").replace("{","").replace("}","").replace(" ","").split(";")#小技巧
    #print(x)
    a=x[0].split(",")
    b=x[1].split(",")
    if(x[0]==""):#防止有空字串,但依測資來看,不必理它
        a=[]
    if(x[1]==""):
        b=[]
    #print(x[0],x[1],"--",a,b)
    out_str=union(a,b)+", "+intersection(a,b)+", "+difference(a,b)+", "+symmetric_difference(a,b)

    print(out_str)
