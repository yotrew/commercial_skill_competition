//#https://github.com/yotrew/commercial_skill_competition
#include <iostream>
#include <vector>
#include <string>     // std::string, std::stoi
#include <sstream>
using namespace std;

int main() {
	int a,b,c,d;
	int t;
	while(cin>>a>>b>>c>>d){
		if(b!=c)//這情況不應該發生
			break;
		int** AB=new int*[a];
		//cout<<a<<";"<<b<<";"<<c<<";"<<d<<endl;
		for(int i=0;i<a;i++){
            AB[i]=new int[d];
		}
		//reset AB matrix to 0 ,可以用memset()
		for(int i=0;i<a;i++){
            for(int j=0;j<d;j++)
                AB[i][j]=0;
		}
		int** A=new int*[a];
		for(int i=0;i<a;i++){
            A[i]=new int[b];
		}
		//reset A matrix
		for(int i=0;i<a;i++){
            for(int j=0;j<b;j++)
                A[i][j]=0;
		}
		int** B=new int*[b];
		for(int i=0;i<b;i++){
            B[i]=new int[d];
		}
		//reset B matrix
		for(int i=0;i<b;i++){
            for(int j=0;j<d;j++)
                B[i][j]=0;
		}
		int* tmp=new int[a*b+b*d];
		int cnt=0;
		//System.out.println(a+":"+b+":"+c+":"+d);
		while (cnt<(a*b+b*d)){
			cin>>t;
			tmp[cnt++]=t;
		}
		cnt=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++)
                A[i][j]=tmp[cnt++];
		}
		for(int i=0;i<b;i++){
			for(int j=0;j<d;j++)
                B[i][j]=tmp[cnt++];
		}
		for(int i=0;i<a;i++)
			for(int j=0;j<d;j++)
				for(int k=0;k<b;k++)
					AB[i][j]+=A[i][k]*B[k][j];

		for(int i=0;i<a;i++){
			for(int j=0;j<(d-1);j++)
				cout<<AB[i][j]<<" ";
			cout<<(AB[i][d-1])<<endl;
        }
	}
	return 0;
}

