//#include <iostream>
//#include <string>
//#include <ctime>
//#include <cstdlib>
//using namespace std;
//
//int max(int x, int y);
//
//int main() {
//	int n = max(4, 16);
//	cout << n;
//	return 0;
//}
//int max(int x, int y) {
//	if (x > y) {
//		return x;
//	}
//	else {
//		return y;
//	}
//}

// ������
//int swap(int& a, int& b) {
//	int _tmp;
//	_tmp = a;
//	a = b;
//	b = _tmp;
//	return a, b;
//}
//int main() {
//	int a = 100, b = 200;
//	swap(a, b);
//	cout << a<<" "<<b;
//	return 0;
//}

//�ߺ��Լ�
//+������ ��
//+�ζ��� �Լ� - �Լ� ���� ���� ���� ����ִ´�!
//int square(int i = 5) {
//	return i * i;
//}
//inline double square(double i) {
//	return i * i;
//}
//
//int main() {
//	cout << square() << endl;
//	cout << square(3.5) << endl;
//	return 0;
//}
//
//inline int odd(int x) {
//	return x % 2;
//}
//int main() {
//	int sum = 0;
//	for (int i= 1; i <= 100000; i++) {
//		sum += i;
//	}
//	cout << sum;
//}