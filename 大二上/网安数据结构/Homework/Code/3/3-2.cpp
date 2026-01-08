#include <cstdio>
#include <iostream>
using namespace std;

struct Node{
    int left;
    int right;
}a[11];
void solve(int root){
    int q[11];
    int l=0,r=0;
    q[l++]=root;
    bool flag=0;
    while(r!=l){
        int node=q[r++];
        if(a[node].left==-1&&a[node].right==-1){
            if(flag)
                cout<<" ";
            cout<<node;
            flag=1;
        }
        if(a[node].left!=-1)
            q[l++]=a[node].left;
        if(a[node].right!=-1)
            q[l++]=a[node].right;
    }
}
int n,sum;
int main(){
    cin>>n;
    for(int i=0;i<n;i++){
        char c,d;
        cin>>c>>d;
        if(c!='-'){
            a[i].left=c-'0';
            sum+=c-'0';
        }
        else
            a[i].left=-1;
        if(d!='-'){
            a[i].right=d-'0';
            sum+=d-'0';
        }
        else
            a[i].right=-1;
    }
    solve((n*(n-1))/2-sum);
    return 0;
}