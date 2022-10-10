//https://github.com/yotrew/commercial_skill_competition
#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<string, string> dict;
    string in,k,v;
    int pos=0;
    while(1){
        getline(cin,in);
        pos=in.find(" ");
        v=in.substr(0,pos );
        k=in.substr(pos+1,in.find("\n"));
        if(k==""){
            break;
        }
        dict[k]=v;
    }
    while(1){
        getline(cin,in);
        k=in.substr(0,in.find("\n"));
        v=dict[k];
        if(v!=""){
            cout<<v<<endl;
        }else{
            cout<<"eh"<<endl;
        }
        if(std::cin.eof()){ 
            break;
        }
    }
    return 0;
}
