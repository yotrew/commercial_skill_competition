#111商業技藝競賽模擬試題
#Problem #B2 四邊形
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

n=int(input())
for i in range(n):
    edge=list(map(int,input().split(" ")))
    edge.sort()
    if sum(edge[0:3])<=edge[3]:
        print("banana")
    elif edge[0]==edge[1] and edge[1]==edge[2] and edge[2]==edge[3]:
        print("square")
    elif edge[0]==edge[1] and edge[2]==edge[3] and edge[2]!=edge[1]:
        print("rectangle")
    else:
        print("quadrangle")
        
'''
test data1:
4
10 8 7 6
9 1 9 1
29 29 29 29
5 12 30 7
output:
quadrangle
rectangle
square
banana


test data2:
8
65535 65535 65535 65535
5647 2948 5647 2948
67 34 90 12
657 354 23 189
546 387 987 234
675 354 987 254
12 45 36 27
78 56 47 39

output:
square
rectangle
quadrangle
banana
quadrangle
quadrangle
quadrangle
quadrangle

'''
