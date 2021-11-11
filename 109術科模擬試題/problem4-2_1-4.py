#商科技藝競賽109年problem4-2
#方法1:python內建排序-自訂比較函數
stus=[]

#讀入檔案資料
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        stus.append([int(line[0]),int(line[1]),int(line[2])])

stus=sorted(stus, key = lambda x : (x[1],x[2],100-x[0]), reverse = True) #用key

for i in stus:
    print(i)
