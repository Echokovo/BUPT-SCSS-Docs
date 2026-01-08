#include<iostream>
using namespace std;
int main() {
	double Score[3] = {}, TotalScore = 0;
	//定义三个学生的成绩与成绩和
	cout << "Please input the scores of the students:";
	for (int i = 0; i <= 2; i++) {
		cin >> Score[i];
		TotalScore += Score[i];
		//循环输入各学生成绩并求和
	}
	cout << "The average score of the three students is " << TotalScore / 3 << endl;
	//输出三个学生的平均成绩
	return 0;
}