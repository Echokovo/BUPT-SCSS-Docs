#include<iostream>
#ifndef Calculation_H
#define Calculation_H
#include"Calculation.h"
#endif
//防止重复导入头文件
using namespace std;
extern int NumOfStudent;
int main() {
	cout << "Please input the information of students using the form of \"Name Chinese Math English\"\nYou can end with \"#\"\n";
	while (cin >> s[NumOfStudent].Name) {
		if (s[NumOfStudent].Name == "#")
			break;
		//输入#时结束输入
		cin >> s[NumOfStudent].Chinese >> s[NumOfStudent].Math >> s[NumOfStudent].English;
		NumOfStudent++;
		//学生数量计数
	}
	if (NumOfStudent <= 0)
		cout << "Invalid input";
	//特殊情况以防计算平均成绩时出现分母为零的情况
	else {
		cout << "Chinese\nAverage Grade|Maxium Grade|Minium Grade\n";
		cout << GetAverageGrade1() << "         " << GetMaxGrade1() << "         " << GetMinGrade1() << "\n";
		cout << "Math\nAverage Grade|Maxium Grade|Minium Grade\n";
		cout << GetAverageGrade2() << "         " << GetMaxGrade2() << "         " << GetMinGrade2() << "\n";
		cout << "English\nAverage Grade|Maxium Grade|Minium Grade\n";
		cout << GetAverageGrade3() << "         " << GetMaxGrade3() << "         " << GetMinGrade3();
	}
	return 0;
}