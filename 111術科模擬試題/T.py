#111商業技藝競賽模擬試題
#Problem #T 路徑
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
import math
tree=list(input().split(","))
last_node=len(tree)
height=int(math.log2(last_node))
#print(tree)
def traverse(node,out_str,last_node):
    global tree
    if node >= last_node or tree[node]=="null":
        return
    out_str.append(tree[node])
    if (node*2+1)>last_node or (node*2+2)>last_node:
        print("->".join(out_str))
        return
    if tree[(node*2+1)]=="null" and tree[(node*2+2)]=="null":
        print("->".join(out_str))
        return
    traverse(node*2+1,out_str.copy(),last_node)
    traverse(node*2+2,out_str.copy(),last_node)
    


traverse(0,[],last_node)
