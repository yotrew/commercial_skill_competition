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


void prefix(Node *p){
	tr.push_back(p->data); //D
    if(p->l!=NULL)//#L
        prefix(p->l);
	if(p->r!=NULL)//R
        prefix(p->r);
	
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
			prefix(root);//trversal-prefix
			for(int a=0;a<tr.size()-1;a++){
				cout<<tr[a]<<" ";
			}
			cout<<tr[tr.size()-1]<<endl;//last one
		}
    return 0;
}
