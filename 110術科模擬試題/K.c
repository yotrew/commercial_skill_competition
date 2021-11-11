#include <stdio.h>
#include <string.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
int main(){
    char x[100];
    char y[100];
    int d[100][100];
    int n=0,i=0,a,b;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        memset(d,0,100*100*sizeof(char));
        scanf("%s",x);
        scanf("%s",y);
        for(a=0;a<strlen(y);a++){
			for(b=0;b<strlen(x);b++){
				if(y[a]==x[b])
					d[a+1][b+1]=d[a][b]+1;
				else
					d[a+1][b+1]=MAX(d[a+1][b],d[a][b+1]);
			}
		}
        printf("%d\n",(d[strlen(y)][strlen(x)]));
    }
   
}
