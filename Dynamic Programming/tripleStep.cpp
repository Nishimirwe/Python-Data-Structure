#include <iostream>

using namespace std;
int dynamic(int n)
{
    int* arr;
    arr=new int[n+1];
    arr[0]=arr[1]=1;
    arr[2]=2;
    for(int i=3;i<(n+1);i++)
    {
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3];
        if(i==n)
        {
            return arr[i];
        }
    }
}
int main()
{
    cout << dynamic(4) << endl;
    return 0;
}
