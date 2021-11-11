#108商業技藝競賽正式試題
#Problem 4： 子題 1：著色問題(程式執行限制時間: 2 秒)
'''
只要看與我相連的vertex是否被著色過,
若與我相連的vertex著不同顏色就False(反之就是都要著一樣的顏色)

'''
n=int(input())
for i in range(0,n):
    v=int(input())
    vertex=[-1 for a in range(0,v)]#節點要著的色,-1代表還沒著色,為了方便,以0代表著第1個顏色,1代表著第2個顏色
    e=int(input())
    edge=[]
    for a in range(0,e):
        y=list(map(int,input().strip().split(" ")))
        edge.append([y[0],y[1]])

    coloring=True
    for a in range(0,v):
        if vertex[a]!=-1:#被著色過了,應該不會
            continue
        color=[0,0]
        for b in range(0,e):
            if edge[b][0]==a and vertex[edge[b][1]]!=-1:
                color[vertex[edge[b][1]]]=1
            if edge[b][1]==a and vertex[edge[b][0]]!=-1:
                color[vertex[edge[b][0]]]=1

        if color[0]==1 and color[1]==1:
            coloring=False
            break
        if color[0]==0:
            vertex[a]=0
            continue
        if color[1]==0:
            vertex[a]=1
    if(coloring):
        print("T")
    else:
        print("F")
