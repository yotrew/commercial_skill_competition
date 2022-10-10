#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 1：輸出二元樹的後序拜訪的結果。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210711
#110商業技藝競賽模擬試題
#Problem L 二元樹的前序拜訪/二元樹的後序拜訪
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
n=int(input())
tree=[]
tr=[]
def postfix(node):
    global tree,tr
    
    #print(tree[node])
    if(tree[node][2]!=-1):#L
        postfix(tree[node][2])
    if(tree[node][3]!=-1):#R
        postfix(tree[node][3])
    tr.append(tree[node][1])
for i in range(0,n):
    input()#使用python,VB(有字串split的程式語言)可以不case此數
    x=list(map(int,input().strip().split(",")))

    #  0   1     2        3
    #[編號,值,左子樹編號,右子樹編號]
    num=1
    tree=[[0,x[0],-1,-1]]
    tr=[]

    #資料輸入處理
    for a in range(1,len(x)):
        node=0
        while True:
            if(x[a]>tree[node][1]):
                if(tree[node][3]!=-1):
                    node=tree[node][3]
                else:                    
                    tree.append([num,x[a],-1,-1])
                    tree[node][3]=num
                    num+=1
                    break
            else:
                if(tree[node][2]!=-1):
                    node=tree[node][2]
                else:                    
                    tree.append([num,x[a],-1,-1])
                    tree[node][2]=num
                    num+=1
                    break
    #print(tree)
    postfix(0)#樹追蹤-後序
    for a in range(0,len(tr)-1):
        print(tr[a],end=" ")
    print(tr[-1])
