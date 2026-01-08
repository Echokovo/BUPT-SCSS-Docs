#include<string>
using namespace std;
void encryption(string* s, int key[], int k_len) {
	/*
	string* s:待加密字符串指针
	int key[]:密钥数组
	int k_len:密钥数组长度
	*/
	int s_len = s->size();
	for (int i = 0; i < s_len; i++) {
		(*s)[i] ^= key[i % k_len];
	}
}
void decryption(string* s, int key[], int k_len) {
	/*
	string* s:待解密字符串指针
	int key[]:密钥数组
	int k_len:密钥数组长度
	*/
	int s_len = s->size();
	for (int i = 0; i < s_len; i++) {
		(*s)[i] ^= key[i % k_len];
	}
}