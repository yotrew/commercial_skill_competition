#include <stdio.h>
#include <stdlib.h>
int cmp(const int* row1,const int* row2){
    if (row1[3]<row2[3])//a<b return -1¬°asc,a<b return 1¬°desc,
        return 1;
    else if(row1[3]>row2[3])
        return -1;
    else//a==b
        return 0;

}
int main()
{
    int score[50][4];
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d %d %d",&score[i][0],&score[i][1],&score[i][2]);
        score[i][3]=score[i][1]*100000+score[i][2]*100+(100-score[i][0]);
    }
         //(array,row,col*sizeof(type),cmp)
    qsort(score,n,4*sizeof(int),cmp);
    for(i=0;i<n;i++){
        printf("%d %d %d\n",score[i][0],score[i][1],score[i][2]);
    }
    return 0;
}
