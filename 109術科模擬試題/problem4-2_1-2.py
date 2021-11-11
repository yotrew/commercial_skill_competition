#商科技藝競賽109年problem4-2
#方法1:python內建排序
stus=[]
with open("./in1.txt","r") as dataf:
    data=dataf.readlines()
    
    for i in range(1,len(data)):
        line=data[i].replace("\n","").split(" ")
        stus.append([int(line[0]),int(line[1]),int(line[2])])


#Ref:https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes

'''
#錯誤方法
stus=sorted(stus, key = lambda stus : stus[1], reverse = True)
stus=sorted(stus, key = lambda stus : stus[2], reverse = True)
stus=sorted(stus, key = lambda stus : stus[0])

要倒著回來,權重較低的先排
以下為正確方法
'''
stus=sorted(stus, key = lambda stus : stus[0])
stus=sorted(stus, key = lambda stus : stus[2], reverse = True)
stus=sorted(stus, key = lambda stus : stus[1], reverse = True)

'''
方法同上:
#stus=sorted(sorted(sorted(stus, key = lambda x: x[0]), key = lambda x : x[2], reverse = True), key = lambda x : x[1], reverse = True)
'''

for i in stus:
    print(i)
