#include <stdio.h>
#include <stdlib.h>
int cmp(const int* row1,const int* row2){
    if (row1[1]<row2[1])//a<b return -1為asc,a<b return 1為desc,
        return 1;
    else if(row1[1]>row2[1])
        return -1;
    else//a==b
    {
        if (row1[2]<row2[2])//a<b return -1為asc,a<b return 1為desc,
            return 1;
        else if(row1[2]>row2[2])
            return -1;
        else{
            if (row1[0]<row2[0])//a<b return -1為asc,a<b return 1為desc,
                return -1;
            else if(row1[0]>row2[0])
                return 1;
            else
                return 0;
        }

    }
    return 0;
}
int main()
{
    int score[50][3];
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d %d %d",&score[i][0],&score[i][1],&score[i][2]);
    }
         //(array,row,col*sizeof(type),cmp)
    qsort(score,n,3*sizeof(int),cmp);
    for(i=0;i<n;i++){
        printf("%d %d %d\n",score[i][0],score[i][1],score[i][2]);
    }
    return 0;
}
