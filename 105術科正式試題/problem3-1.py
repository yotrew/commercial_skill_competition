#105商業技藝競賽正式試題
#Problem 3： 資料結構—樹 子題 1：是否為堆積樹(Heap tree)或二元搜尋樹(Binary search tree)。
#Author:Yotrew
#20210710
'''
題目的輸入是一個完整二元樹,也就是可以直接用Array(List)來存此樹
判斷方式:
1.只要我一個兒子比我小,就不會是最大堆積樹
2.只要我一個兒子比我大,就不會是最小堆積樹
3.我的左子樹比我小,我的右子樹比我大才會是二元樹,反之就不是
所以一開始假設是"最大堆積樹,最小堆積樹,二元樹",只要判斷上面的條件成立就設為不是
'''
import math
n=int(input())

for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    max_heap=True
    min_heap=True
    bintree=True
    #print(math.log(len(x),2))
    x_h=int(math.log(len(x),2))#樹高度
    x_len=len(x)
    #print(x_len)
    c1=0
    c2=0
    for a in range(0,x_h):
        for b in range(2**a-1,2**(a+1)-1):
            c1=b*2+1
            c2=b*2+2
            #print(b,c1,c2)
            if(c1>=x_len):#我沒兒子,有這種情況嗎?因為做到n-1層
                continue
            elif(c2>=x_len):#只有一個兒子(左子樹)
                if(x[b]<x[c1]):#我的兒子比我大就不會是min_heap
                    min_heap=False
                if(x[b]>x[c1]):#我的兒子比我小就不會是max_heap
                    max_heap=False
            else:#有2個兒子
                if(x[b]<x[c1]):#我的兒子比我大就不會是min_heap
                    min_heap=False
                if(x[b]>x[c1]):#我的兒子比我小就不會是max_heap
                    max_heap=False
                if(x[b]<x[c2]):#我的兒子比我大就不會是min_heap
                    min_heap=False
                if(x[b]>x[c2]):#我的兒子比我小就不會是max_heap
                    max_heap=False
                if not (x[b]>x[c1] and x[b]<x[c2]):#如果不是(我的左兒子小於我,我的右兒子大於我),就不是binary tree
                    bintree=False
                
    if(max_heap==False and min_heap==False and bintree==False):
        print("F")
    elif(bintree==True):
        print("B")
    else:
        print("H")
