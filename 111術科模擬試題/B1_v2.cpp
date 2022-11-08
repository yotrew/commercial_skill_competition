/*
#111商業技藝競賽模擬試題
#Problem #B1 好友滿天下
#Author: Yotrew Wing
#2022/11/08
#https://github.com/yotrew/commercial_skill_competition
'''
本題名字不會重覆,所以只需要統計國家出現次數
'''
*/
#include <iostream>
#include <map>
#include <set>
using namespace std;

int main()
{
    int n;
    cin>>n;
    string ins;
    string delimiter = " ";
    size_t end;
    map<string, int> dic;
    cin.get();
    for(int i=0;i<n;i++){
        getline(cin,ins);
        end=ins.find(delimiter);
        dic[ins.substr(0, end)]++;
    }
    for (auto &item :dic) {
        cout << item.first << " " << item.second << endl;
    }
    return 0;
}
