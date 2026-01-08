#include<iostream>
using namespace std;
int main() {
	double UpperBottom=11.4,Bottom=51.4,Height=1919,Area;
	//定义上底、下底、高和梯形面积
	Area = (UpperBottom + Bottom) / 2.0 * Height;
	//计算梯形面积
	cout << "Area of the Trapezoid is " << Area << endl;
	//输出梯形面积
	return 0;
}