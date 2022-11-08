/*
#111�ӷ~�����v�ɼ������D
#Problem #E1 �G����
#Author: Yotrew Wing
#2022/11/08
#https://github.com/yotrew/commercial_skill_competition
##UVa122:Trees on the level
'''
�D�ػ��̦h256��node,���@�w�O�����G����,�]�i��O�n�׾�
�ҥH�n��list(vector)�Ӽ�����,�ا����A��BFS�Ӱ����X
'''
*/
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <limits>

using namespace std;
int INFINITY = std::numeric_limits<int>::max(); //���ꤤ���ȷ|���t��???
int main()
{
    string ins="";
    string delimiter = ",";
    size_t end;
    int val;
    string direct;
    map<char, int> dic; //�d��,�t�Xvector(tree)==>tree[x][]={val,left,right}
    dic['L']=1;
    dic['R']=2;

    vector<vector<int>> tree;
    vector<int> root = {-INFINITY,-INFINITY,-INFINITY};
    int pos=0,current_node=0;
    tree.push_back(root);
	
    int complete=0;
    while(cin>>ins){
		
		//traverse--BFS
        if(ins=="()"){
            current_node=0;
            string out_str="";
            vector<int> q; //��vector����queue,�u�O��node���s��
            int cnt=0;

            if(tree[current_node][0]!=-INFINITY){//��root
                q.push_back(current_node);
            }
            while(q.size()>0){
                current_node=q[0];
                if(tree[current_node][0]!=-INFINITY){
                    out_str+= std::to_string(tree[current_node][0])+" ";
                    cnt++;
                }
                q.erase(q.begin());
                if(tree[current_node][1]!=-INFINITY) //���l��
                    q.push_back(tree[current_node][1]);
                if(tree[current_node][2]!=-INFINITY)//�k�l��
                    q.push_back(tree[current_node][2]);
            }
            if(complete==0 && tree.size()==cnt)
                cout<<out_str.substr(0,out_str.size()-1)<<endl;
            else{
                cout<<"not complete"<<endl;
            }

            //reset the variables
            tree.clear();
            vector<int> root = {-INFINITY,-INFINITY,-INFINITY};
            pos=0;
            tree.push_back(root);
            complete=0;
            continue;
        }
		
		//�B�z��J
        end=ins.find(delimiter);
        try{
            val=stoi(ins.substr(1, end-1));
        }catch(...){
            break;
        }

        direct=ins.substr(end+1,ins.size()-end-2);
        if(direct==""){ //root
            tree[0][0]=val;
        }else{
            pos=0;
            for (int i=0; i<direct.length(); ++i)
            {
                if(tree[pos][dic[direct[i]]]==-INFINITY){
                    vector<int> newnode = {-INFINITY,-INFINITY,-INFINITY};
                    tree.push_back(newnode);
                    tree[pos][dic[direct[i]]]=tree.size()-1;
                }
                pos=tree[pos][dic[direct[i]]];
            }
            if(tree[pos][0]!=-INFINITY){
                complete=1; //��J�����I
            }
            tree[pos][0]=val;
        }
    }
    return 0;
}
