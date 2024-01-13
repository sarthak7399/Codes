/*
Input: 12345
String length is odd
Output:
1       5
  2   4
    3
  2   4
1       5 
*/
#include<iostream>
#include<string>
using namespace std;
    int main()
        {
            int i=0,j=0,k=0,l;
            string st;
            cout<<"Enter a STRING:";
            cin>>st;
            int len=st.length();
            for(i=0;i<len;i++)
            {
                for(j=0; j<len;j++)
                {
                    if(i==j)
                    {
                        cout<<st.at(i);
                    }
                    else if(j==len-i-1)
                    {
                        cout<<st.at(len-i-1);
                    }
                    else
                    {
                        cout<<" ";
                    }
                }
                cout<<endl;
            }
            return 0;
        }