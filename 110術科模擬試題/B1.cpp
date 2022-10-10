/*
#110商業技藝競賽模擬試題
#Problem B1 閏年
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
*/
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