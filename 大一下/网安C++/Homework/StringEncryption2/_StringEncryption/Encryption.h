#include<string>
#include"List.h"
using namespace std;
class Encryption {
	string key;
	int k_len;
	//ÃÜÔ¿ÓëÃÜÔ¿³¤¶È
public:
	Encryption() {
		k_len = 0;
	}
	void key_input() {
		cin >> key;
		k_len = key.size();
	}
	void StrEncry(list l) {
		node* p = l.head;
		while (p) {
			int s_len = p->str.size();
			for (int i = 0; i < s_len; i++) {
				p->str[i] ^= key[i % k_len];
			}
			p = p->next;
		}
	}
	void StrDecry(list l) {
		node* p = l.head;
		while (p) {
			int s_len = p->str.size();
			for (int i = 0; i < s_len; i++) {
				p->str[i] ^= key[i % k_len];
			}
			p = p->next;
		}
	}
};