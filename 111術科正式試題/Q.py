#111商業技藝競賽正式試題
#Problem Q 二元樹資訊

#Author:Yotrew Wing
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#DFS
'''
*節點0為根
'''
import pprint
n=int(input())

#一個node記錄的資訊[val,L,R,parent,degree,depth,height]
#一個node記錄的資訊[0:val,1:L,2:R,3:parent,4:degree,5:depth,6:height]
tree=[[0,-1,-1,-1,0,0,0,-1]]

def DFS(node,parent,depth):
    global tree
    
    tree[node][3]=parent
    tree[node][5]=depth
    #print(node,parent,depth)
    max_h1=-1
    max_h2=-1
    if tree[node][1]!=-1: #往左子樹
        max_h1=DFS(tree[node][1],node,depth+1)
        tree[node][4]+=1
        
    if tree[node][2]!=-1: #往右子樹
        max_h2=DFS(tree[node][2],node,depth+1)
        tree[node][4]+=1

    tree[node][7]=1
    tree[node][6]=max(max_h1,max_h2)+1
    return tree[node][6]

for i in range(n):
    val,L,R=map(int,input().split(" "))
    if val==0:
        tree[0][1]=L
        tree[0][2]=R
    else:
        tree.append([val,L,R,-1,0,0,0,-1])
DFS(0,-1,0)       
#pprint.pprint(tree)
for i in tree:
    print(f"node {i[0]}: parent = {i[3]}, degree = {i[4]}, depth = {i[5]}, height = {i[6]},")
'''
Sample Input 1
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
Sample Output 1
node 0: parent = -1, degree = 2, depth = 0, height = 3,
node 1: parent = 0, degree = 2, depth = 1, height = 1,
node 2: parent = 1, degree = 0, depth = 2, height = 0,
node 3: parent = 1, degree = 0, depth = 2, height = 0,
node 4: parent = 0, degree = 2, depth = 1, height = 2,
node 5: parent = 4, degree = 2, depth = 2, height = 1,
node 6: parent = 5, degree = 0, depth = 3, height = 0,
node 7: parent = 5, degree = 0, depth = 3, height = 0,
node 8: parent = 4, degree = 0, depth = 2, height = 0,


Sample Input 2
6
0 3 -1
1 -1 5
2 -1 -1
3 4 -1
4 2 1
5 -1 -1

Sample Output 2
node 0: parent = -1, degree = 1, depth = 0, height = 4,
node 1: parent = 4, degree = 1, depth = 3, height = 1,
node 2: parent = 4, degree = 0, depth = 3, height = 0,
node 3: parent = 0, degree = 1, depth = 1, height = 3,
node 4: parent = 3, degree = 2, depth = 2, height = 2,
node 5: parent = 1, degree = 0, depth = 4, height = 0,
'''
