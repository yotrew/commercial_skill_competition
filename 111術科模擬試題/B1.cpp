/*
#111商業技藝競賽模擬試題
#Problem #B1 好友滿天下
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition
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
    string token="";
    size_t end;
    size_t start=0;
    string country="";
    map<string, set<string>> dic;
    cin.get();
    for(int i=0;i<n;i++){
        getline(cin,ins);
        //cout<<"test"<<ins<<endl;
        start=0;
        end=ins.find(delimiter);
        country=ins.substr(start, end-start);
        token=ins.substr(end+delimiter.size());
        dic[country].insert(token);
    }
    for (auto &item :dic) {
        cout << item.first << " " << item.second.size() << endl;
    }
    return 0;
}
