#include <iostream>
#include <vector>
#include <string>     // std::string, std::stoi
#include <sstream>
using namespace std;
vector<int *> tree(30);
vector<int> tr(30);//trversal

void postfix(int node){
    if(tree[node][2]!=-1)//#L
	postfix(tree[node][2]);
	if(tree[node][3]!=-1)//R
	postfix(tree[node][3]);
	tr.push_back(tree[node][1]); //D
}

int main(){
    int n;
    cin>>n;
    char in_str[100];
    string x[50]; //存放分割後的資料 
    char ch;  //定義一個字元變數
    string in;
    for(int i=0;i<n;i++){
			int node_cnt;
            cin>>node_cnt;
            int xs=0;//x字串長度
            //cout<<"node cnt:"<<node_cnt<<"----"<<endl;


            //讀入整行,使用,號拆字串
            cin>>in;
            stringstream ss(in);
            while(getline(ss, x[xs], ','))
              xs++;

			int num=1;
			tree.clear(); //清空
			int *tmp1=new int[4];
			tmp1[0]=0;
			tmp1[1]=stoi(x[0]);
			tmp1[2]=-1;
			tmp1[3]=-1;
			tree.push_back(tmp1);
			tr.clear();
			for(int b=1;b<node_cnt;b++){

				int a=stoi(x[b]);
				int node=0;
				while(true){
					if(a>tree[node][1]){
						if(tree[node][3]!=-1){
							node=tree[node][3];
						}else{
							int* tmp=new int[4];
							tmp[0]=num;
                            tmp[1]=a;
                            tmp[2]=-1;
                            tmp[3]=-1;
							tree.push_back(tmp);
							tree[node][3]=num;
							num+=1;
							break;
						}
					}
					else{
						if(tree[node][2]!=-1){
							node=tree[node][2];
						}else{
							int* tmp=new int[4];
							tmp[0]=num;
                            tmp[1]=a;
                            tmp[2]=-1;
                            tmp[3]=-1;
							tree.push_back(tmp);
							tree[node][2]=num;
							num+=1;
							break;
						}
					}
				}
			}
			/*for(int []c:tree){//print Tree
				cout<<c[0]<<","<<c[1]<<","<<c[2]+","<<c[3];
			}*/
			postfix(0);//trversal-postfix
			for(int a=0;a<tr.size()-1;a++){
				cout<<tr[a]<<" ";
			}
			cout<<tr[tr.size()-1]<<endl;//last one
		}
    return 0;
}
