#include<iostream>
#include "Encryption.h"
using namespace std;

Encryption operator+(const Encryption& p, const std::string& q)
{
	Encryption ret;
	ret.str.resize(p.str.size());
	//初始化ret.str
	for (int i = 0; i < p.str.size(); i++) {
		ret.str[i] = p.str[i] ^ q[i % q.size()];
	}
	return ret;
}

Encryption operator-(const Encryption& p, const std::string& q)
{
	Encryption ret;
	ret.str.resize(p.str.size());
	//初始化ret.str
	for (int i = 0; i < p.str.size(); i++) {
		ret.str[i] = p.str[i] ^ q[i % q.size()];
	}
	return ret;
}

Encryption::Encryption()
{
	str = "";
}

void Encryption::output()
{
	cout << str << "\n";
}

void Encryption::output_hex()
{
	for (int i = 0; i < str.size(); i++) {
		cout.fill('0');
		cout.width(2);
		cout << hex << int(str[i]);
	}
	//以16进制输出密文
	cout << "\n";
}

void Encryption::operator=(const Encryption& p)
{
	str = p.str;
}

void Encryption::operator=(const std::string& p)
{
	str = p;
}

char& Encryption::operator[](int i)
{
	if (i >= str.size() || i<0) {
		cout << "Index error";
		return str[0];
	}
	//防止下标溢出
	return str[i];
}