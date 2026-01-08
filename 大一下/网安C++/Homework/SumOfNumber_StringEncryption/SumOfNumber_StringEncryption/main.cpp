#include<iostream>
#include"GetSum.h"
#include"StringEncryption.h"
#define F(a) a=(a+2)%128
using namespace std;
int main() {
	int n[10] = { 5,6,19,89,69 };
	cout <<"求和结果为" << GetSum(n, 4) << "\n";
	string str = "I am fine";
	cout << "函数加密结果为" << StrEncry(str, 2) << "\n";
	for (int i = 0; i < str.size(); i++) {
		F(str[i]);
	}
	cout << "宏预处理加密结果为" << str;
	return 0;
}