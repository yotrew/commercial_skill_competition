/*
#111商業技藝競賽模擬試題
#Problem #A1 內積
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
*/
#include <iostream>

using namespace std;

int main()
{
    int x1,x2,x3,y1,y2,y3;
    cin>>x1>>x2>>x3;
    cin>>y1>>y2>>y3;
    cout<<(x1*y1+x2*y2+x3*y3)<<endl;
    return 0;
}
/*
'''
test data1:
1 2 3
2 3 4
output:
20

test data2:
1 2 3
4 5 6

output:
32
'''
*/
