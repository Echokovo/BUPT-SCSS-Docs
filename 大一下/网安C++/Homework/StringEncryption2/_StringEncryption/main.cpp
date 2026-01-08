#include<iostream>
#include<string>
#include"Encryption.h"
using namespace std;
int main() {
	Encryption x;
	list l;
	cout << "Please input the keys:\n";
	x.key_input();
	cout << "Please input strings(end with #):\n";
	l.insert();
	cout << "Input strings:\n";
	l.output();
	cout << "Encrypted strings:\n";
	x.StrEncry(l);
	l.hex_output();
	cout << "Decrypted strings:\n";
	x.StrDecry(l);
	l.output();
	return 0;
}