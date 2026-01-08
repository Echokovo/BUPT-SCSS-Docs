#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#define debug(a) cout<<#a<<"="<<a<<endl;
#define INF 0x3f3f3f3f
using namespace std;
int n;
int num[30];
void print(){
    for(int i=1;i<=n;i++)   cout<<num[i]<<',';
    cout<<endl;
}
int main(){
    cin>>n;
    char t;
    for(int i=1;i<=n;i++)   cin>>num[i]>>t;
    for(int i=2;i<=n;i++){
        int t=num[i];
        int j=i-1;
        while(j>=1&&num[j]>t){
            num[j+1]=num[j];
            j--;
        }
        num[j+1]=t;
        print();
    }
    return 0;
}