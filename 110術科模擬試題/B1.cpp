#include <iostream>
using namespace std;
int main(){
    int year;
    cin>>year;
    if(year % 400 == 0)
			cout<<"a leap year"<<endl;
		else if( year % 4 ==0 && year % 100 !=0)
			cout<<"a leap year"<<endl;
		else
			cout<<"a normal year"<<endl;
    
}