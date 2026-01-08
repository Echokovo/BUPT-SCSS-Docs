#include<string>
#include<iostream>
#include"Encryption.h"
using namespace std;
int main() {
	Encryption x;
	string input,key;
	cout << "Please input plaintext:\n";
	cin >> input;
	cout << "Please input key:\n";
	cin >> key;
	x = input;
	x = x + key;
	cout << "Ciphertext:\n";
	x.output_hex();
	x = x - key;
	cout << "Plaintext:\n";
	x.output();
	cout << "New plaintext:\n";
	for (int i = 0; i < input.size(); i++) {
		x[i] = key[i % key.size()];
		cout << x[i];
	}
	//验证下标运算符重载
	return 0;
}