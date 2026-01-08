#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#define debug(a) cout<<#a<<"="<<a<<endl;
#define INF 0x3f3f3f3f
#define N 10
using namespace std;
int map[10][10];
int dis[10];
int ans[20],p;
bool vis[10];
void prim(){
    vis[0]=1;
    for(int i=0;i<N;i++)
        dis[i]=min(dis[i],map[0][i]);
    for(int i=1;i<N;i++){
        int m=INF;
        int n=-1;
        for(int j=1;j<N;j++){
            if(!vis[j]&&m>dis[j]){
                m=dis[j];
                n=j;
            }
        }
        if(n==-1)
            return;
        vis[n]=1;
        ans[p++]=dis[n];
        for(int i=1;i<N;i++)
            dis[i]=min(dis[i],map[n][i]);
    }
    sort(ans,ans+N-1);
    for(int i=0;i<N-1;i++)
        cout<<ans[i]<<",";
    return;
}
int main(){
    memset(map,INF,sizeof(map));
    memset(dis,INF,sizeof(dis));
    string input[]={"AB","BC","AD","AE","BE","BF","CF","CG","DE","EF","FG","DH","EH","EI","FI","FJ","GJ","HI","IJ"};
    int _input[]={3,10,4,4,2,3,6,1,5,11,2,6,2,1,3,11,8,4,7};
    for(int i=0;i<=18;i++){
        map[input[i][0]-'A'][input[i][1]-'A']=_input[i];
        map[input[i][1]-'A'][input[i][0]-'A']=_input[i];
    }
    char A,B,t;
    int n;
    cin>>A>>t>>B>>t>>n;
    map[A-'A'][B-'A']=n;
    for(int i=0;i<N;i++)
        map[i][i]=0;
    prim();
    return 0;
}