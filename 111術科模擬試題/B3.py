#111商業技藝競賽模擬試題
#Problem #B3 平行四邊形
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

while True:
    try:
        x1,y1,x2,y2,x3,y3,x4,y4=map(float,input().split())
        vertex=[]
        if x1==x2 and y1==y2:
            vertex=[[x3,y3],[x4,y4],[x1,y1]]
        elif x2==x3 and y2==y3:
            vertex=[[x1,y1],[x4,y4],[x2,y2]]
        elif x3==x4 and y3==y4:
            vertex=[[x1,y1],[x2,y2],[x3,y3]]
        elif x4==x1 and y4==y1:
            vertex=[[x2,y2],[x3,y3],[x1,y1]]
        elif x1==x3 and y1==y3:
            vertex=[[x2,y2],[x4,y4],[x1,y1]]
        elif x2==x4 and y2==y4:
            vertex=[[x1,y1],[x3,y3],[x2,y2]]
        #print(vertex)
        x=vertex[0][0]+vertex[1][0]-vertex[2][0]
        y=vertex[0][1]+vertex[1][1]-vertex[2][1]
        print(f"{x:.3f} {y:.3f}")
    except:
        break
