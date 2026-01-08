#include<string>
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)>(b)?(b):(a)
//定义宏实现求最大值、最小值
using namespace std;
int NumOfStudent = 0;
struct Student {
	string Name;
	double Chinese, Math, English;
	Student() {
		Name = "";
		Chinese = Math = English = 0;
	}
	//初始化
};
//定义学生结构体
Student s[100];
extern double GetAverageGrade1() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret += s[i].Chinese;
	return ret / NumOfStudent;
}
extern double GetAverageGrade2() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret += s[i].Math;
	return ret / NumOfStudent;
}
extern double GetAverageGrade3() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret += s[i].English;
	return ret / NumOfStudent;
}
extern double GetMaxGrade1() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MAX(ret, s[i].Chinese);
	return ret;
}
extern double GetMinGrade1() {
	double ret = 1000;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MIN(ret, s[i].Chinese);
	return ret;
}
extern double GetMaxGrade2() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MAX(ret, s[i].Math);
	return ret;
}
extern double GetMinGrade2() {
	double ret = 1000;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MIN(ret, s[i].Math);
	return ret;
}
extern double GetMaxGrade3() {
	double ret = 0;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MAX(ret, s[i].English);
	return ret;
}
extern double GetMinGrade3() {
	double ret = 1000;
	for (int i = 0; i < NumOfStudent; i++)
		ret = MIN(ret, s[i].English);
	return ret;
}