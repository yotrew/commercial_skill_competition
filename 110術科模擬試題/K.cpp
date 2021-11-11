#include <iostream>
#include <cstring>
using namespace std;
int main(){
    string a1;
    string b1;
    int n,a,b;
    int d[100][100];
    cin>>n;
    for(int i=0;i<n;i++){
        memset(d,0,100*100*sizeof(char));
        cin>>a1;
        const char *x=a1.c_str();
        cin>>b1;
        const char *y=b1.c_str();
        
        for(a=0;a<strlen(y);a++){
			for(b=0;b<strlen(x);b++){
				if(y[a]==x[b])
					d[a+1][b+1]=d[a][b]+1;
				else
					d[a+1][b+1]=max(d[a+1][b],d[a][b+1]); 
			}
		}
        cout<<(d[strlen(y)][strlen(x)])<<endl;
    }
    return 0;
}