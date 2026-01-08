#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
using namespace std;
string s,t;
int main(){
    map<string,char> m;
    m["1010"]='a';
    m["00"]='b';
    m["10000"]='c';
    m["1001"]='d';
    m["11"]='e';
    m["10001"]='f';
    m["01"]='g';
    m["1011"]='h';
    cin>>s;
    for(int i=0;i<s.size();i++){
        t+=s[i];
        if(m.find(t)!=m.end()){
            cout<<m[t];
            t="";
        }
    }
    return 0;
}