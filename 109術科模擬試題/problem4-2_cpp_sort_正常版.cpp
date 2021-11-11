#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(int* row1,int* row2){
    if (row1[1]<row2[1])//a<b return -1為asc,a<b return 1為desc,
        return false;
    else if(row1[1]>row2[1])
        return true;
    else//a==b
    {
        if (row1[2]<row2[2])//a<b return -1為asc,a<b return 1為desc,
            return false;
        else if(row1[2]>row2[2])
            return true;
        else{
            if (row1[0]<row2[0])//a<b return -1為asc,a<b return 1為desc,
                return true;
            else if(row1[0]>row2[0])
                return false;
            else
                return true;
        }

    }
    return true;
}

int main()
{
    int** score;
    int n,i;
    cin>>n;
    score=new int*[n];
    for(i=0;i<n;i++){
        score[i]=new int[3];
        cin>>score[i][0]>>score[i][1]>>score[i][2];
    }
    sort(score,score+n,cmp);
    for(i=0;i<n;i++){
        cout<<score[i][0]<<" "<<score[i][1]<<" "<<score[i][2]<<endl;
    }
    return 0;
}
