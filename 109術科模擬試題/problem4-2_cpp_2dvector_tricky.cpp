/*
2D vector版
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(vector<int> row1,vector<int> row2){
    return (row1[3]>row2[3]);
}

int main()
{
    int n,i;
    cin>>n;
    vector<vector<int> > score(n, vector<int>(4)); //二維vector n列4欄

    for(i=0;i<n;i++){
        cin>>score[i][0]>>score[i][1]>>score[i][2];
        score[i][3]=score[i][1]*100000+score[i][2]*100+(100-score[i][0]);
    }
    sort(score.begin(),score.end(),cmp);
    for(i=0;i<n;i++){
        cout<<score[i][0]<<" "<<score[i][1]<<" "<<score[i][2]<<endl;
    }

    return 0;
}
