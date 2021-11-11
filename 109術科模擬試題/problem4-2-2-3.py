#商科技藝競賽109年problem4-2
#方法2:python內建排序&排1個欄位
stus=[]
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        stus.append([int(line[0]),int(line[1]),int(line[2])])

stus=sorted(stus, key= lambda x: x[1]*100000+x[1]*100+(100-x[0]),reverse=True )

    
for i in stus:
    print(i)
