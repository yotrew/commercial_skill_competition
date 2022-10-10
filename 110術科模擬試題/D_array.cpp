//#https://github.com/yotrew/commercial_skill_competition
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int n,a;
    int num[100001],cnt=0;
    memset(num,0,100001*sizeof(int));
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
        num[a]=1;
    }
    for(int i=0;i<100001;i++){
        if(num[i]==1)
            cnt++;
    }
    cout<<cnt;
    return 0;
}