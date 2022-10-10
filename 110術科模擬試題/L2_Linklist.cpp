/*
#104商業技藝競賽正式試題
#Problem 4：資料結構—樹 子題 1：輸出二元樹的後序拜訪的結果。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210711
#110商業技藝競賽模擬試題
#Problem L 二元樹的前序拜訪/二元樹的後序拜訪
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
*/
#include <iostream>
#include <vector>
#include <string>     // std::string, std::stoi
#include <sstream>
using namespace std;
vector<int> tr(30);//trversal

class Node{
public:
    int data=0;
    Node *l=NULL;
    Node *r=NULL;
};


void postfix(Node *p){
    if(p->l!=NULL)//#L
        postfix(p->l);
	if(p->r!=NULL)//R
        postfix(p->r);
	tr.push_back(p->data); //D
}
int main(){
    int n;
    cin>>n;
    string in;
    string x;
    Node* root=NULL;
    for(int i=0;i<n;i++){
			int node_cnt;
            cin>>node_cnt;
            root=NULL;
            tr.clear();
            cin>>in;
            stringstream ss(in);
            while(getline(ss, x, ',')){
                int a=stoi(x);
                Node* p=root;
                if(root==NULL){
                    root=new Node();
                    root->data=a;
                }else{
                    while(p!=NULL){
                        if(a>p->data){
                            if(p->r!=NULL)
                                p=p->r;
                            else{
                                p->r=new Node();
                                p->r->data=a;
                                break;
                            }
                        }else{
                            if(p->l!=NULL)
                                p=p->l;
                            else{
                                p->l=new Node();
                                p->l->data=a;
                                break;
                            }
                        }
                    }
                }
            }


			/*for(int []c:tree){//print Tree
				cout<<c[0]<<","<<c[1]<<","<<c[2]+","<<c[3];
			}*/
			postfix(root);//trversal-postfix
			for(int a=0;a<tr.size()-1;a++){
				cout<<tr[a]<<" ";
			}
			cout<<tr[tr.size()-1]<<endl;//last one
		}
    return 0;
}
