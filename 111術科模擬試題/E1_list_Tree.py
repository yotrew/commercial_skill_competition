#111商業技藝競賽模擬試題
#Problem #E1 二元樹
#Author: Yotrew Wing
#2022/10/18
#https://github.com/yotrew/commercial_skill_competition
#UVa122:Trees on the level
'''
題目說最多256個node,不一定是完滿二完樹,也可能是歪斜樹
所以要用list來模擬樹,建完樹後再用BFS來做拜訪
'''
tree=[[None,None,None]] #先建一個root
complete=0
while True:
    try:
        #L用1取代,R用2,因為模擬樹,一個node存的是[value,# of Left,# of Right]
        ins=input().replace("(","").replace(")","").replace("L","1").replace("R","2").split(" ")
        for i in ins:
            data=i.split(",")
            
            if len(data)<=1: #()代表一棵樹的結束,開始traverse
                #traverse-BFS
                current_node=0
                out_str=[]
                if tree[current_node][0]!=None: #有root
                    q=[current_node]
                    
                while len(q)>0:
                    current_node=q[0]
                    if tree[current_node][0]!=None:
                        out_str.append(tree[current_node][0])
                    q.pop(0)
                    if tree[current_node][1]!=None:
                        q.append(tree[current_node][1])
                    if tree[current_node][2]!=None:
                        q.append(tree[current_node][2])

                if complete==0 and len(out_str)==len(tree):
                    print(" ".join(out_str))
                else:
                    print("not complete")
                tree=[[None,None,None]]
                #cnt=0
                complete=0
                continue #traverse完後繼續讀資料
            if data[1]=='': #root
                tree[0][0]=data[0]
            else:
                pos=0
                for i in range(len(data[1])):
                    direct=int(data[1][i])
                    if tree[pos][direct]==None:
                        tree.append([None,None,None])
                        tree[pos][direct]=len(tree)-1

                    pos=tree[pos][direct]
                if tree[pos][0]!=None:
                    complete=1 #輸入重複點
                tree[pos][0]=data[0]   
    except:
        break
        
'''
test data1:
(11,LL) (7,LLL) (8,R)
(5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R)
(5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(4,L) (2,LL) ()
(5,) (4,L) (2,LLL) ()
(5,) (4,L) (2,LL) ()
output:
5 4 8 11 13 4 7 2 1
not complete
not complete
not complete
5 4 2
'''
