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
    for(int i=1;i<=n-1;i++){
        int m=INF;
        int index=-1;
        for(int j=i;j<=n;j++){
            if(num[j]<m){
                m=num[j];
                index=j;
            }
        }
        if(index!=-1){
            swap(num[index],num[i]);
        }
        print();
    }
    return 0;
}