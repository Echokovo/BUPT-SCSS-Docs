#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#define debug(a) cout<<#a<<"="<<a<<endl;
#define N 8
using namespace std;
bool map[9][9];
bool vis[9];
int Start;
void dfs(int S){
    cout<<S<<",";
    for(int i=1;i<=N;i++){
        if(!vis[i]&&map[S][i]){
            vis[i]=1;
            dfs(i);
            //vis[i]=0;
        }
    }
    return;
}
int main(){
    string input[]={"1 2","1 3","2 4","2 5","3 6","3 7","4 8","5 8","6 8","7 8"};
    for(string s:input)
        map[s[0]-'0'][s[2]-'0']=1,map[s[2]-'0'][s[0]-'0']=1;
    cin>>Start;
    vis[Start]=1;
    dfs(Start);
    return 0;
}