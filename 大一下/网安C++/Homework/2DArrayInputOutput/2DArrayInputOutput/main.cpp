#include<iostream>
#define NUM 51
//预处理二维数组的大小
using namespace std;
void ArrayInput(int _Array[][NUM], int x, int y) {
	cin >> _Array[x][y];
}
int ArrayOutput(int _Array[][NUM], int x, int y) {
	return _Array[x][y];
}
int main() {
	int Array[NUM][NUM] = {};
	//定义二维数组并初始化
	cout << "Please input the " << NUM - 1 << "*" << NUM - 1 << " array\n";
	for (int i = 1; i < NUM; i++) {
		for (int j = 1; j < NUM; j++) {
			ArrayInput(Array, i, j);
		}
	}
	//输入二维数组
	for (int i = 1; i < NUM; i++) {
		for (int j = 1; j < NUM; j++) {
			cout << ArrayOutput(Array, i, j) << " ";
		}
		cout << "\n";
	}
	//输出二维数组
	return 0;
}