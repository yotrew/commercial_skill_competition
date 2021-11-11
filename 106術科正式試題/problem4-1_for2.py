#106商業技藝競賽正式試題
#Problem 4：資料結構—樹、後序法 子題 1：樹。(程式執行限制時間: 2 秒)

#迴圈做法--感覺可能會有錯,但所有測資都會過
import copy
n=int(input())
paths1=[[[0] for j in range(0,21)] for j in range(0,21)]#題目已限制i,j<=20,最多20點
paths=[]#儲存各個邊(path1同path,但為了不用每組測資重新分配,就先建paths1再copy到paths)

for i in range(0,n):
    paths=copy.deepcopy(paths1)#加速用
    vertex=set()#使用set來記錄各個頂點編號,因為set會踢掉重複
    
    in_str=input().strip().split(" ")
    edge_count=len(in_str)

    #讀入所有邊
    for a in in_str:
        x=list(map(int,a.split(",")))
        paths[x[0]][x[1]]=1
        paths[x[1]][x[0]]=1
        vertex.add(x[0])
        vertex.add(x[1])
    
    vertex_list=list(vertex)
    #print(vertex_list)
    if (len(vertex_list)-1)==edge_count: #推論可知,邊數和頂點數-1相等為Tree
        print("T")
    elif (len(vertex_list)-1)>edge_count:#推論可知,頂點數-1 > 邊數為森林(2棵樹以上)
        print("F")
    else:#loop-有loop找出loop所在
        visited=[]
        stack=[]
        max_vertex=vertex_list[-1] #加速用,最大頂點編號
        min_vertex=vertex_list[0] #加速用,最小頂點編號
        loop=-1
        visited.append(vertex_list[0]) #把第1點頂點,最小點加入被拜訪列表中
        for i in range(max_vertex-1,min_vertex-1,-1):#加入此點的鄰居到stack中
            if(paths[visited[-1]][i]==1):
                stack.append(i)
                
        while (loop<0) and len(stack)>0:
            if stack[-1] in visited:#找到loop跳出
                loop=stack[-1]
                break
            
            visited.append(stack[-1])#stack的最後一點加入被拜訪中
            
            for i in range(max_vertex,min_vertex-1,-1):#把stack最後一點當作要被拜訪的點
                if(paths[visited[-1]][i]==1 and i !=visited[-2]):#如果我的鄰居又連回我就不加到stack中<--(i !=visited[-2])
                    stack.append(i)
                    
            while stack[-1]==visited[-1]:#拜訪到盡頭,退回,如DFS中到最深的那一點
                del stack[-1]
                del visited[-1]

        #題目要求編號由小到大,所以用排序                
        visited=sorted(visited[visited.index(loop):],key=lambda x:x)
        print(", ".join(map(str, visited)))
            

