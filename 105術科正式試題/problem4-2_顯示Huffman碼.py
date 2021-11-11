#105商業技藝競賽正式試題
#Problem 4：其它 子題 2：霍夫曼編碼（Huffman Coding）
#Author:Yotrew
#20210710
'''
為了不想建Tree,想要以簡單迴圈方式解決(會有很多判斷),
反而寫出又臭又長又會有問題的程式(problem4-2_不完整_某些條件未考慮清楚.py)
用樹追蹤方式反而是最簡單
*本題最多只有26個相異點,且至少2個
'''
'''
在python建樹的方法:
class Node:
    def __init__(self,data=None):
        self.data=data
        self.l=None #左兒子
        self.r=None #右兒子
        
a=Node()
a.r=Node("b")
#print(a.data,a.r.data)
'''
n=int(input())

tree=[]
huffman=[]
#樹深度追蹤
def Tree_Lv(node,lv,code):
    global tree,huffman    
    node[2]=lv
    if(node[3]>=0):#左兒子
        Tree_Lv(tree[node[3]],lv+1,code+"0")
    if(node[4]>=0):#右兒子
        Tree_Lv(tree[node[4]],lv+1,code+"1")
    if(node[3]==-1 and node[4]==-1):#leaf
        #print(node[0],code)
        huffman.append([node[0],code])
        
    
for i in range(0,n):
    x=list(map(int,input().strip().split(",")))
    #print(x)
    node=[]
    tree=[]
    huffman=[]
    
    for a in range(0,len(x)):
        node.append([a,x[a],0,-1,-1]) #用list來模擬樹的node
        #[編號,出現次數,在樹的第幾層,兒子1編號,兒子2編號],編號>len(node)為中繼點
    node=sorted(node,key=lambda x:x[1])
    
    num=len(node)#
    max_num=num

    #建樹,num>=len(tree)為中繼點
    while len(node)>1:
        a=node[0]
        b=node[1]
        if(a[1]>=b[1]):
            c=[num,a[1]+b[1],0,a[0],b[0]]#合併為中繼點
        else:
            c=[num,a[1]+b[1],0,b[0],a[0]]#合併為中繼點
        num+=1
        tree.append(a)
        tree.append(b)
        node[1]=c#合併後存回node串列中,再做排序
        node.remove(a)
        node=sorted(node,key=lambda x:x[1])
        #不做排序的方法就是自行比較合併後前3個
        #但因最多是25個中繼點+26個原始點,51個排序花不了多少時間
 
    tree.append(node[0])#最後一個
    tree=sorted(tree,key=lambda x:x[0])#做編號的排序
    
    #print(tree)
    Tree_Lv(node[-1],0,"")#root,level
    #print(tree)
    for i in range(0,max_num-1):#印0~max_num-2,最後一個沒逗號另外處理,max_num之後都是中繼點
        print(tree[i][2],end=",")#
    print(tree[max_num-1][2])#

    #顯示Huffman code
    print("Huffman code:")
    huffman=sorted(huffman,key=lambda x:x[0])#做編號的排序
    #print(huffman)
    for i in range(0,max_num):#印0~max_num-2,最後一個沒逗號另外處理,max_num之後都是中繼點
        print("{}:{}".format(huffman[i][0],huffman[i][1]))
    print("------")


