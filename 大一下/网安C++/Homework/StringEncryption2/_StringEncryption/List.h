#include<string>
using namespace std;
class Encryption;
class node {
public:
	string str;
	node* next;
	node(string str, node* next) {
		this->next = next;
		this->str = str;
	}
	//构造函数以便初始化
};
class list {
	node* head;
public:
	list() {
		head = NULL;
	}
	void insert();
	void output();
	void hex_output();
	friend class Encryption;
	//使用友元类使head能被Encryption类内函数访问
};
void list::insert() {
	string input;
	node* p;
	node* tail = head;
	cin >> input;
	while (input != "#") {
		p = new node(input, NULL);
		if (head==NULL)
			head = tail = p;
		else
			tail->next = p, tail = p;
		cin >> input;
	}
	//尾节点插入法创建单向链表
}
void list::output() {
	node* p = head;
	while (p) {
		cout << p->str << "\n";
		p = p->next;
	}
}
void list::hex_output() {
	node* p = head;
	while (p) {
		for (int i = 0; i < p->str.size(); i++) {
			cout.fill('0');
			cout.width(2);
			cout << hex << int(p->str[i]);
		}
		//以16进制输出密文
		cout << "\n";
		p = p->next;
	}
}