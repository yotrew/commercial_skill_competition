#110商業技藝競賽正式試題
#Problem E 字典
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition


dic={}
while True:
    ins=input()
    if ins.strip()=="":#空白列
        break
    
    a,b=ins.split(" ")
    dic[b]=a
while True:
    try:
        ins=input()
        if ins in dic:
            print(dic[ins])
        else:
            print("eh") #未查到
    except Exception as e:
        break


