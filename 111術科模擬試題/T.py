#111商業技藝競賽模擬試題
#Problem #T 路徑
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
'''
資料讀入就是一個完整二元樹
直接使用計算方式就可以travese:
某個node的左兒子為node*2+1,右兒子為node*2+2 (*因為root是0開始:list的第一個元素為0)
某個node的parent=node//2 #<--取商數  (此處的node為節點的索引)
'''
tree=list(input().split(","))
last_node=len(tree)

def traverse(node,out_str): #DFS-traverse
    global tree,last_node
    if node >= last_node or tree[node]=="null":
        return
    out_str.append(tree[node])

    
    if (node*2+1)>last_node or (node*2+2)>last_node:
        print("->".join(out_str))
        return
    
    if (node*2+2)>=last_node:
        if tree[(node*2+1)]=="null":
            print("->".join(out_str))
            return
    else:
        if tree[(node*2+1)]=="null" and tree[(node*2+2)]=="null":
            print("->".join(out_str))
            return
    
    #拜訪左子樹
    traverse(node*2+1,out_str.copy())
    #拜訪右子樹
    traverse(node*2+2,out_str.copy())
    
traverse(0,[]) #從root開始traverse
