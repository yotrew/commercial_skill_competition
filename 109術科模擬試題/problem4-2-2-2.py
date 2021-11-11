#商科技藝競賽109年problem4-2
#方法2:python內建排序&排1個欄位
stus=[]
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        y=int(line[1])*100000+int(line[2])*100+(100-int(line[0]))
        stus.append([int(line[0]),int(line[1]),int(line[2]),y])

stus=sorted(stus, key = lambda stus: stus[3],reverse=True)

    
for i in stus:
    print(i)
