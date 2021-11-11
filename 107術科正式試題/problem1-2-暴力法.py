#107商業技藝競賽正式試題
#Problem 1：子題 2：井字棋
#暴力法(硬解)
n=int(input())
for i in range(0,n):
    game=""
    for a in range(0,3):
        x=input()#.replace("\n","")#把每行最後"換行"拿掉
        game+=x

    #暴力法,寫程式求快,只要copy&paste
    winner="0"
    if(game[0]==game[1] and game[1]==game[2]):
        winner=game[0]
    if(game[3]==game[4] and game[4]==game[5]):
        winner=game[3]
    if(game[6]==game[7] and game[7]==game[8]):
        winner=game[6]
    if(game[0]==game[3] and game[3]==game[6]):
        winner=game[0]
    if(game[1]==game[4] and game[4]==game[7]):
        winner=game[1]
    if(game[2]==game[5] and game[5]==game[8]):
        winner=game[2]
    if(game[0]==game[4] and game[4]==game[8]):
        winner=game[0]
    if(game[2]==game[4] and game[4]==game[6]):
        winner=game[2]
        
    if(winner=="0"):
        winner=3
    print(winner)
    
