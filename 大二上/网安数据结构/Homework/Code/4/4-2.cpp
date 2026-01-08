#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#define debug(a) cout<<#a<<"="<<a<<endl;
#define INF 0x3f3f3f3f
#define N 7
int map[10][10],dis[10],path[10];
bool vis[10];
int Start,Target;
using namespace std;
void dijkstra(int S,int T){
	dis[S]=0;vis[S]=1;
	for(int i=1;i<=N;i++){
		map[i][i]=0;
		dis[i]=min(dis[i],map[S][i]);
		path[i]=dis[i]<INF?S:-1;
	}
	for(int i=1;i<=N-1;i++){
		int m=INF;
		for(int j=1;j<=N;j++){
			if(!vis[j]&&m>dis[j]){
				m=dis[j];
				S=j;
			}
		}
		vis[S]=1;
		for(int j=1;j<=N;j++){
			if(dis[j]>dis[S]+map[S][j]){
				dis[j]=dis[S]+map[S][j];
				path[j]=S;
			}
		}
	}
	if(dis[Target]!=INF){
		int ans[10]={-1,},p=0;
		while(path[T]!=Start){
			ans[p++]=path[T];
			T=path[T];
		}
		cout<<Start<<",";
		for(int i=p-1;i>=0;i--)
			cout<<ans[i]<<",";
		cout<<Target<<",";
	}else{
		cout<<-1;
	}
	return;
}
int main(){
	memset(map, INF, sizeof(map));
    memset(dis, INF, sizeof(dis));
	memset(path,-1,sizeof(path));
	string input[] = {"1 2 2", "1 4 1", "2 4 3", "2 5 10", "4 5 2", "3 1 4", "4 3 2", "3 6 5", "4 6 8", "4 7 4", "5 7 6", "7 6 1"};
    for (string s : input)
        map[s[0] - '0'][s[2] - '0'] = (int)(s[4] - '0');
    map[2][5] = 10;
    char t;
    cin >> Start >> t >> Target;
	dijkstra(Start,Target);
    return 0;
}