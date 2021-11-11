#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(int* row1,int* row2){
    return (row1[3]>row2[3]);
}

int main()
{
    int** score;
    int n,i;
    cin>>n;
    score=new int*[n];
    for(i=0;i<n;i++){
        score[i]=new int[4];
        cin>>score[i][0]>>score[i][1]>>score[i][2];
        score[i][3]=score[i][1]*100000+score[i][2]*100+(100-score[i][0]);
    }
    sort(score,score+n,cmp);
    for(i=0;i<n;i++){
        cout<<score[i][0]<<" "<<score[i][1]<<" "<<score[i][2]<<endl;
    }

    return 0;
}
