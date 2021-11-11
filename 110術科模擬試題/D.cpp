#include <iostream>
#include <set>
using namespace std;

int main()
{
    int n,a;
    std::set<int>  aset;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
        aset.insert(a);
    }
    cout<<aset.size();
    return 0;
}
