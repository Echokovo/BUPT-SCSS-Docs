#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;
string s,p;
int n,t;
void getNex(string p,int nex[]){
    nex[0]=0;
    int j=0;
    for(int i=1;i<p.size();i++){
        while(j>0&&p[i]!=p[j])
            j=nex[j-1];
        if(p[i]==p[j])
            j++;
        nex[i]=j;
    }
}
int kmp(string s,string p){
    if(p.size()>s.size())
        return -1;
    int j=0;
    int nex[100010]={};
    getNex(p,nex);
    for(int i=0;i<s.size();i++){
        while(j>0&&s[i]!=p[j])
            j=nex[j-1];
        if(s[i]==p[j])
            j++;
        if(j==p.size())
            return i+1-p.size();
    }
    return -1;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    cin>>s>>n;
    while(n--){
        cin>>p;
        t=kmp(s,p);
        if(t!=-1){
            for(int i=t;i<s.size();i++)
                cout<<s[i];
            cout<<"\n";
        }
        else{
            cout<<"Not Found\n";
        }
    }
    return 0;
}