#include<iostream>
#include<random>
#include<ctime>
using namespace std;
const int MAX = 100;
//防止随机数过大
unsigned long long Generate(int depth) {
	if (!depth) {
		return 1;
	}
	//递归出口
	unsigned long long ret = 1;
	ret *= (rand()%MAX);
	ret *= Generate(depth - 1);
	return ret;
}
int main() {
	int num = 0;
	srand(time(nullptr));
	//定义递归深度并初始化随机数种子
	cout << "Please input the number of the depth ";
	cin >> num;
	if (num <= 0) {
		cout << "Invalid number" << endl;
	}
	//特判递归深度为负数的特殊情况
	else {
		cout <<"The product of the number is " << Generate(num) << endl;
	}
	return 0;
}