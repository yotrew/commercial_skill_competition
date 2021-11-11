#109商業技藝競賽模擬試題
#Problem 4： 子題1：關節點(程式執行限制時間: 2 秒)
'''
此題在題目中已提供方法:

方法2:使用DFS/BFS,拿掉此點,剩下的點中,
      只要有一點不能連到其他全部的點,此點則為關節點
      此法比較容易理解,但效率不好.
'''
import pprint
#paths_tmp=[[0 for i in range(0,22)] for j in range(0,22)]#加速
import copy#Ref:https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list
           #其他題目不用改--->因為其他的為一維
while True:
    n=int(input())
    if n==0:#結束
        break

    paths=[[0 for i in range(0,n+1)] for j in range(0,n+1)]
    AP=[]#記錄誰是關節點,本題目沒有要求,只是列出來看看
    while True:#讀入Paths
        x=list(map(int,input().strip().split(" ")))
        if(x[0]==0):
            break
        for i in range(1,len(x)):
            #print(i)
            paths[x[0]][x[i]]=1
            paths[x[i]][x[0]]=1
    cnt=0
    visited1=[0 for i in range(0,n+1)]#加速
	
    for i in range(1,n+1):
        visited=visited1.copy()
        BFS=[]
        pos=i%n+1#任取一點為起點,簡單的做法就以下一點為起點,但最後一點的下一點就是第1點
        BFS.append(pos)
        #print(i,BFS)
        while len(BFS):
            pos=BFS[0]
            BFS.pop(0)#移除第1個 
            visited[pos]=1
            
            for j in range(1,n+1):
                if(j==i):#拿掉那一點,要跳掉不做
                    continue
                if visited[j]==0 and paths[pos][j]==1:
                    BFS.append(j)
                #print(i,j,pos,BFS,visited)
        for j in range(1,n+1):
            if visited[j]==0 and i!=j:
                cnt+=1
                AP.append(i)
                break
    print(cnt)
    print("關節點:",AP)
        
