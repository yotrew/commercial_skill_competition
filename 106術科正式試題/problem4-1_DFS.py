#106商業技藝競賽正式試題
#Problem 4：資料結構—樹、後序法 子題 1：樹。(程式執行限制時間: 2 秒)
'''
1. 邊數>=點數,則有loop,要進一步找出loop點
2. 點數>邊數-1 5點>3邊,一定是森林
3. 點數=邊數-1 樹,(題目的輸出說有說,"任一樹狀結構的總邊數等於其總節點數減1")
*應該有考慮到各種情況了吧?_?-->當有5個點,3個點形成loop,另外2個點形成tree,5點,4點-->錯,還是要用DFS
'''
import copy#Ref:https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list


#加速用
paths1=[[] for j in range(0,21)]#題目已限制i,j<=20,最多20點
vertex1=[0 for i in range(0,21)]
visited=[]
paths=[]
loop_list=[]#形成loop的點
Loop=-1
def DFS(v):
    global paths,visited,loop_list,Loop
    count=0
    if visited[v]==1:#代表被拜訪過了
        Loop=v
        return -1#形成loop傳回 1
    
    visited[v]=1
    count=1
    for i in paths[v]:
        paths[i].remove(v)#把回來的路拿掉
        y=DFS(i)
        
        if y==-1 and Loop!=-1:
            loop_list.append(v)#記錄loop的點
            if(v==Loop):#V和Loop同一點代表Loop都找完了,之後的不用加到List裡面去了
                Loop=-1
                '''
                要注意這種圖形:4,0 5,1 6,2 7,3 4,5 5,7 7,2 2,4
                因為起點可能不會包含在Loop中
                '''
            return -1
        count+=y
        
    return count#傳回拜訪幾個點了
    
n=int(input())
for i in range(0,n):
    paths=copy.deepcopy(paths1)
    vertex=copy.deepcopy(vertex1)
    visited=copy.deepcopy(vertex1)
    in_str=input().strip().split(" ")
    #print(in_str)
    
    vertex_list=[]
    for a in in_str:
        x=list(map(int,a.split(",")))
        paths[x[0]].append(x[1])
        paths[x[1]].append(x[0])

        if(vertex[x[0]]==0):
            vertex_list.append(x[0])
        if(vertex[x[1]]==0):
            vertex_list.append(x[1])
        vertex[x[0]]=1#加速用,記錄點是否有存在
        vertex[x[1]]=1#加速用,記錄點是否有存在

    vertex_list=sorted(vertex_list,key=lambda a:a)

    for a in range(0,vertex_list[-1]):
        paths[a]=sorted(paths[a],key=lambda a:a)#對每個點的路徑做排序

    
    #print(vertex_list)
    #print(paths)

    loop_list=[]
    count=0
    count=DFS(vertex_list[0])
    #print(count)
    #print(loop_list)
    if(len(loop_list)>0):
        loop_list=sorted(loop_list,key=lambda a:a)
        for a in range(0,len(loop_list)-1):
            print(loop_list[a],end=", ")#和problem3-2一樣,要注意逗號後面的空白
        print(loop_list[-1])#印出最後一點
    else:
        
        if count==len(vertex_list):#點的個數與追蹤點的個數一樣多
            print("T")
        else:
            print("F")
'''
#錯誤的想法,不過在本題測資應該會過
for i in range(0,n):
    paths=copy.deepcopy(paths1)
    vertex=copy.deepcopy(vertex1)
    visited=copy.deepcopy(vertex1)
    #print(vertex)
    in_str=input().strip().split(" ")
    #print(in_str)
    edge_count=len(in_str)
    for a in in_str:
        x=list(map(int,a.split(",")))
        paths[x[0]][x[1]]=1
        paths[x[1]][x[0]]=1
        vertex[x[0]]=1
        vertex[x[1]]=1
    
    vertex_list=[]
    for a in range(0,len(vertex)):
        if(vertex[a]==1):
            vertex_list.append(a);
    #print(vertex_count,edge_count)
    if (len(vertex_list)-1)==edge_count:
        print("T")
    elif (len(vertex_list)-1)>edge_count:
        print("F")
    else:
        print("Loop")

'''
