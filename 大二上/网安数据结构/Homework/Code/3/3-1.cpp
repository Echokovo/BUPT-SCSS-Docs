#include <cstdio>
#include <iostream>
using namespace std;
int n;
int bo[50],mo[50],ans[50000];
void solve(int l,int r,int m){
    if(l>r)
        return;
    int i;
    for(i=l;i<r;i++)
        if(mo[i]==bo[m])
            break;
    cout<<" "<<bo[m];
    solve(l,i-1,m-1-r+i);
    solve(i+1,r,m-1);
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>bo[i];
    for(int i=0;i<n;i++)
        cin>>mo[i];
    cout<<"Preorder:";
    solve(0,n-1,n-1);
    return 0;
}