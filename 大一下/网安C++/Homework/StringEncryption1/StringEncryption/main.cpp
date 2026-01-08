#include<iostream>
#include<algorithm>
#include<string>
#include"StringEncryption.h"
#define NUM 100
using namespace std;
bool cmp(string p, string q) {
	if (p.size() != q.size())
		return p.size() < q.size();
	return p < q;
}
//字符串排序函数，使字符串先以字符串长度为关键字排序
int main() {
	int num, k_len = 0, t;
	int key[NUM] = {};
	//初始化密钥数组
	cout << "Please input the number of strings:";
	cin >> num;
	cout << "Please input the keys(end with -1):\n";
	while (cin >> t) {
		if (t == -1)
			break;
		key[k_len++] = t;
	}
	//输入密钥并计数
	cout << "Please input the strings:\n";
	string* str = new string[NUM];
	//申请空间存放字符串
	for (int i = 1; i <= num; i++) {
		cin >> *(str + i);
	}
	sort(str, str + num, cmp);
	//对字符串进行自定义排序
	cout << "The sorted strings:\n";
	for (int i = 1; i <= num; i++) {
		cout << *(str+i) << "\n";
	}
	cout << "The encrypted strings:\n";
	for (int i = 1; i <= num; i++) {
		encryption(str+i, key, k_len);
		for (int j = 0; j < (str + i)->size(); j++) {
			cout.fill('0');
			cout.width(2);
			cout << hex << int((*(str + i))[j]);
			//以十六进制输出加密后的字符串
		}
		cout << "\n";
	}
	cout << "The decrypted strings:\n";
	for (int i = 1; i <= num; i++) {
		decryption(str+i, key, k_len);
		cout << *(str+i) << "\n";
	}
	return 0;
}