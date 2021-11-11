#107商業技藝競賽正式試題
#Problem 1：子題 2：井字棋
#for loop,就寫程式上,好像沒比較快
n=int(input())
for i in range(0,n):
    game=""
    for a in range(0,3):
        x=input()#.replace("\n","")#把每行最後"換行"拿掉
        game+=x

    winner="0"
    for a in range(0,3):
        if(game[a*3]==game[a*3+1] and game[a*3+1]==game[a*3+2]):
            winner=game[a*3]
    for a in range(0,3):
        if(game[a]==game[a+3] and game[a+3]==game[a+6]):
            winner=game[a]
    
    if(game[0]==game[4] and game[4]==game[8]):
        winner=game[0]
    if(game[2]==game[4] and game[4]==game[6]):
        winner=game[2]
        
    if(winner=="0"):
        winner=3
    print(winner)
    
