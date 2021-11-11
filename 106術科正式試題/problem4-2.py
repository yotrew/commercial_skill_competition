#106商業技藝競賽正式試題
#Problem 4：資料結構—樹、後序法 子題 2：後序運算式(postfix)。(程式執行限制時間: 2 秒)
'''
這一題直接用stack
'''
n=int(input())
for i in range(0,n):
    in_str=input().strip().split(" ")
    stack=[]#python list的好處
    for i in in_str:
        #print(stack)
        if(i=="+"):
            stack[-2]=stack[-2]+stack[-1]
            stack.pop()
        elif(i=="-"):
            stack[-2]=stack[-2]-stack[-1]#順序要對(-2,-1),不然答案會錯
            stack.pop()
        elif(i=="*"):
            stack[-2]=stack[-2]*stack[-1]
            stack.pop()
        elif(i=="/"):
            stack[-2]=int(stack[-2]/stack[-1])#順序要對(-2,-1),不然答案會錯
            stack.pop()
        else:#為數字
            stack.append(int(i))
    print(int(stack[-1]))
            
