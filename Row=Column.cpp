/*  1
    1
    22
    22
    333
    333
    4444
    4444
    55555
    55555
*/
#include<iostream>
using namespace std;
int main()
{
    int i,j,c;
    for( i=1; i<=5; i+=1 ){
        c=i;
        for( j=1; j<=c; j++ ){
            cout<<i;
        }
        cout<<endl;
        for( j=1; j<=c; j++ ){
            cout<<i;
        }
        cout<<endl;
    }
}