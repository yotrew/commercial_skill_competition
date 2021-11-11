#107商業技藝競賽正式試題
#Problem 1：子題 1：計算字數及含有s 或 S 字母的字數
#同106商業技藝競賽正式試題Problem 1：子題 1
n=int(input())
for i in range(0,n):
    tmp=input().split(" ")
    count=0
    for i in tmp:
        if "s" in i or "S" in i:
            count+=1
    print("%d,%d"%(len(tmp),count))
