/*
#111商業技藝競賽模擬試題
#Problem #A2 MOD
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
*/
#include <iostream>

using namespace std;

int main()
{
    int x,y,t;
    cin>>x>>y;
    if(x>y){
        t=y;
        y=x;
        x=t;
    }
    //cout<<x<<":"<<y;
    for(int i=x+1;i<y;i++){
        if(i%5==2 || i%5==3)
            cout<<i<<endl;
    }

    return 0;
}
/*
test data1:
10
18
output:
12
13
17

test data2:
19
12

output:
13
17
18

*/
