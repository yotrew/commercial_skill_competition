#n個字的排列組合
x=[]
y="你好嗎?"
#y="ABCD"
def perm(n):
    global x,y
    if n==0:
        print("".join(x))
        return
    for i in y:
        if i in x:
            continue
        else:
            x.append(i)
            perm(n-1)
            #print(x)
            x.remove(i)

perm(len(y))
    
