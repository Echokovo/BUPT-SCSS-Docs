/*
int num[] -待求和数组
int depth -待求和数组长度
*/
inline long long GetSum(int num[],int depth) {
	if (depth < 0) {
		return 0;
	}
	//递归跳出条件
	return num[depth] + GetSum(num, depth - 1);
}