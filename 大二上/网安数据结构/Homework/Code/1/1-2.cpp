#include<iostream>
using namespace std;
int num[10000];
int main(){
	int n;
	char c;
	while(cin>>n>>c){
		num[++num[0]]=n;
	}
	bool flag=0;
	for(int i=1;i<=num[0]/2;i++){
		if(num[i]!=num[num[0]-i+1]){
			cout<<"No"<<endl;
			return 0;
		}
	}
	cout<<"Yes"<<endl;
    return 0;
}