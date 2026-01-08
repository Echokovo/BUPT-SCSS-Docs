#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <sstream>
#define debug(a) cout<<#a<<"="<<a<<endl;
#define INF 0x3f3f3f3f
using namespace std;
vector<int> parseInput(const string& input1, const string& input2) {
    vector<int> nums;
    stringstream s1(input1);
    string temp;
    while (getline(s1, temp, ',')) {
        nums.push_back(stoi(temp));
    }
    stringstream s2(input2);
    while (getline(s2, temp, ',')) {
        nums.push_back(stoi(temp));
    }
    return nums;
}
void Merge(vector<int>& nums, int l, int le, int r, int re){
    vector<int> temp;
    int _l=l;
    while(l<=le&&r<=re){
        if(nums[l]<=nums[r]){
            temp.push_back(nums[l++]);
        }else{
            temp.push_back(nums[r++]);
        }
    }
    while(l<=le)
        temp.push_back(nums[l++]);
    while(r<=re)
        temp.push_back(nums[r++]);
    for(int i=0;i<temp.size();i++)
        nums[_l+i]=temp[i];
    return ;
}
void MergeSort(vector<int>& nums, int l, int r){
    int m;
    if(l<r){
        m=(l+r)/2;
        MergeSort(nums,l,m);
        MergeSort(nums,m+1,r);
        Merge(nums,l,m,m+1,r);
    }
    return ;
}
int main(){
    string s1,s2;
    cin>>s1>>s2;
    vector<int> nums = parseInput(s1,s2);
    MergeSort(nums,0,nums.size()-1);
    for(int i:nums)
        cout<<i<<",";
    return 0;
}