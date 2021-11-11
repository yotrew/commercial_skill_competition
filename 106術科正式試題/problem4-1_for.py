#106商業技藝競賽正式試題
#Problem 4：資料結構—樹、後序法 子題 1：樹。(程式執行限制時間: 2 秒)

#迴圈做法
import copy
n=int(input())
paths1=[[[0] for j in range(0,21)] for j in range(0,21)]#題目已限制i,j<=20,最多20點
vertex1=[0 for i in range(0,21)]
visited=[]
paths=[]
for i in range(0,n):
    paths=copy.deepcopy(paths1)
    vertex=copy.deepcopy(vertex1)
    
    #print(vertex)
    in_str=input().strip().split(" ")
    #print(in_str)
    edge_count=len(in_str)
    #讀入邊
    for a in in_str:
        x=list(map(int,a.split(",")))
        paths[x[0]][x[1]]=1
        paths[x[1]][x[0]]=1
        vertex[x[0]]=1
        vertex[x[1]]=1
    #print(paths)
    vertex_list=[]
    for a in range(0,len(vertex)):
        if(vertex[a]==1):
            vertex_list.append(a);
    #print(vertex_count,edge_count)
    if (len(vertex_list)-1)==edge_count:
        print("T")
    elif (len(vertex_list)-1)>edge_count:
        print("F")
    else:#loop
        visited=[]
        stack=[]
        max_vertex=vertex_list[-1]
        min_vertex=vertex_list[0]
        loop=-1
        visited.append(vertex_list[0])
        for i in range(max_vertex-1,min_vertex-1,-1):
            if(paths[visited[-1]][i]==1):
                stack.append(i)
        while (loop<0) and len(stack)>0:
            if stack[-1] in visited:
                loop=stack[-1]
                break
            visited.append(stack[-1])

            for i in range(max_vertex,min_vertex-1,-1):
                if(paths[visited[-1]][i]==1 and i !=visited[-2]):
                    stack.append(i)
            while stack[-1]==visited[-1]:
                del stack[-1]
                del visited[-1]
        #print(visited.index(loop))
        visited=sorted(visited[visited.index(loop):],key=lambda x:x)
        print(", ".join(map(str, visited)))
            

