#108商業技藝競賽正式試題
#Problem 3： 子題 1：出現的次數最多的DNA 序列
'''
此題範例,要直的看,由上而下
'''
import pprint
n=int(input())
for i in range(0,n):
    x=list(map(int,input().split(" ")))
    A,B=x[0],x[1]
	
    DNA_list={"A":0,"C":1,"G":2,"T":3}#查表法
    DNA_list2=["A","C","G","T"]#反查
    DNA=[]
    for a in range(0,A):
        DNA.append(input())
    for b in range(0,B):
        count=[0,0,0,0]
        for a in range(0,A):
            count[ DNA_list[ DNA[a][b]  ]    ]+=1
        print(DNA_list2[count.index(max(count))],end="") #找最出現最多次,其他程式語言一般來說就寫for loop找
    print()
