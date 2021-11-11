#商科技藝競賽109年problem4-2
#方法1:python內建排序-自訂比較函數
stus=[]

#讀入檔案資料
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        stus.append([int(line[0]),int(line[1]),int(line[2])])

#自訂函數
from functools import cmp_to_key 
def compare(A,B):
    #print(A,B)
    if(A[1]<B[1]):
        return 1
    elif(A[1]==B[1]):
        if(A[2]<B[2]):
            return 1
        elif(A[2]==B[2]):
            if(A[0]>B[0]):
                return 1

    return -1

#Calling sorted() in Python 3
stus=sorted(stus,key=cmp_to_key(compare))

