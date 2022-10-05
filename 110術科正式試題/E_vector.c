/*
DOMjudge會過版
*/
#include<stdio.h>
#include<string.h>
int main()
{
    char dict[100001][2][11];
    char *in,*k,*v;
    int i=0,cnt=0,flag=0;
    size_t len=0;
    int nread;
    while((nread=getline(&in,&len,stdin))!=-1){
       if(strlen(in)==1 && (int)in[0]<32)
           break;
       if(strlen(in)==0)
           break;
       v=strtok(in," ");
       k=strtok(NULL,"\n");
       strcpy(dict[cnt][0],k);
       strcpy(dict[cnt][1],v);
       cnt++;
    }
    
    while((nread=getline(&in,&len,stdin))!=-1){
       if(strlen(in)==1 && (int)in[0]<32)
           break;
       if(strlen(in)==0)
           break;
       k=strtok(in,"\n");
       flag=0;
       for(i=0;i<cnt;i++){
           if(strcmp(dict[i][0],k)==0){
               printf("%s\n",dict[i][1]);
               flag=1;
               break;
           }
       }
       if(flag==0){
           printf("eh\n");
       }
    }
    
    return 0;
}
