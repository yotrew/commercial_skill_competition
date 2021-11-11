#106商業技藝競賽正式試題
#Problem 3：數學問題 子題 2：大數排序問題。(程式執行限制時間: 2 秒)
'''
因為Python可以直接處理大數問題,所以這種考題未來應該很少出現
對於其他語言來說,處理這個問題的想法,就是使用字串來存,
先比長度,再來若長度一樣,就一個一個字元比

'''

n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(", ")))
    #print(x)
    x1=sorted(x,key=lambda a:a)
    #print(x1)
    for a in range(len(x)-1):
        print(x1.index(x[a])+1,end=", ")#Ref:https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
        #和problem4-1一樣,要注意逗號後面的空白
    print(x1.index(x[-1])+1)


        
