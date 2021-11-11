stus=[]
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        stus.append([int(line[0]),int(line[1]),int(line[2])])


for i in range(0,len(stus)-1):#氣泡排序法-round數
    for j in range(0,len(stus)-i-1):
        flag=False
        if(stus[j][1]<stus[j+1][1]):#先比數學
            flag=True
        elif(stus[j][1]==stus[j+1][1]):#數學一樣
            if(stus[j][2]<stus[j+1][2]):#比程式
                flag=True
            elif(stus[j][2]==stus[j+1][2]):#程式一樣
                if(stus[j][0]>stus[j+1][0]):#座號
                    flag=True

        if(flag==True):
            tmp=stus[j]
            stus[j]=stus[j+1]
            stus[j+1]=tmp
             
    
for i in stus:
    print(i)
