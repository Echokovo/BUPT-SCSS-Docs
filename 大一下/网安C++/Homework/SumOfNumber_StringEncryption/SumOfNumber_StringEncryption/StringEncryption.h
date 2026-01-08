#include<string>
using namespace std;
/*
string s -´ı¼ÓÃÜ×Ö·û´®
int n -¼ÓÃÜÆ«ÒÆÁ¿
*/
inline string StrEncry(string s, int n) {
	string ret;
	for (int i = 0; i < s.size(); i++) {
		ret += (s[i] + n) % 128;
	}
	return ret;
}