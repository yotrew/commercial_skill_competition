#商科技藝競賽109年problem4-2
#方法2:汽泡排序法&排1個欄位
stus=[]
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        y=int(line[1])*100000+int(line[2])*100+(100-int(line[0]))
        stus.append([int(line[0]),int(line[1]),int(line[2]),y])


for i in range(0,len(stus)-1):#氣泡排序法-round數
    for j in range(i,len(stus)-i-1):
        if(stus[j][3]<stus[j+1][3]):#
            tmp=stus[j]
            stus[j]=stus[j+1]
            stus[j+1]=tmp
             
    
for i in stus:
    print(i)
