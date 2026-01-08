#include<iostream>
#include<cstring>

using namespace std;
//0 1 2 3 4 5 6 7 8 9    10
//A B C D E F G H I S(J) T(K)
int node[11][11];
int in[11];
int queue[20];
int head,tail;
int main(){
    memset(queue,-1,sizeof(queue));
    string input[21]={"DA","AE","AB","BC","EC","FC","DE","EF","GD","GE","HE","EI","IF","GH","HI","JA","JD","JG","CK","FK","IK"};
    for(string s:input){
        node[s[0]-'A'][s[1]-'A']=1;
        in[s[1]-'A']++;
    }
    /*
    for(int i=0;i<11;i++){
        for(int j=0;j<11;j++)
            cout<<node[i][j]<<" ";
        cout<<"\n";
    }
    */
    string t;
    cin>>t;
    if(node[t[0]-'A'][t[2]-'A']){
        node[t[0]-'A'][t[2]-'A']=0;
        in[t[2]-'A']--;
    }
    queue[tail++]=9;
    for(int i=0;i<11-2;i++)
        if(!in[i])
            queue[tail++]=i;
    while(head<tail){
        int index=queue[head];
        for(int i=0;i<11;i++){
            if(node[index][i]){
                node[index][i]=0;
                in[i]--;
                if(!in[i]){
                    queue[tail++]=i;
                }
            }
        }
        if(index==9)
            cout<<"S,";
        else if(index==10)
            cout<<"T,";
        else
            cout<<(char)('A'+index)<<",";
        head++;
    }
    return 0;
}