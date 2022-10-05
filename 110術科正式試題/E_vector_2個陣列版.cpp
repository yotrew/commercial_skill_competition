#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<string> dict_k;
    vector<string> dict_v;
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
        dict_k.push_back(k);
        dict_v.push_back(v);

    }

    while(1){
        getline(cin,in);


        k=in.substr(0,in.find("\n"));

        v="";
        for(int i=0;i<dict_k.size();i++)
            if(dict_k[i]==k){
                v=dict_v[i];
            }
        if(k=="")
            break;
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
