#108商業技藝競賽正式試題
#Problem 1：子題 1：統計答案得分
#此題應該是為了下一題熱身的
n=int(input())
for i in range(0,n):
    x=input()
    count=0
    score=0
    for a in x:
        if a=="O":
            score=score+count+1
            count+=1
        else:
            count=0
    print(score)
