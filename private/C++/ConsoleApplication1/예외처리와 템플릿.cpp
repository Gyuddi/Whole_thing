#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <array>
using namespace std;
//
//int main() {
//	int a, b;
//	cout << "두개의 숫자 입력:";
//	cin >> a >> b;
//	try {
//		if (b == 0)
//			throw b;
//		cout << "a/b의 몫 : " << a / b << endl;
//		cout << "a/b의 나머지 : " << a % b << endl;
//	}
//	catch (int exception) {
//		cout << exception << " 입력." << endl;
//		cout << "입력오류!" << "다시 입력하세요" << endl;
//	}
//	return 0;
//}
//
//template<typename T1,T2>
//double get_max(T1 x, T2 y) {
//	if (x > y) return x;
//	else return y;
//}
//int main() {
//	cout << get_max(1, 3) << endl;
//	cout << get_max(12.6, 30.5) << endl;
//}
//class Box2{
//	T1 f_data;
//	T2 s_data;
//public:
//	Box2() {}
//	T1 get_f() { return f_data; }
//	T2 get_s() { return s_data; }
//	void set_f(T1 value) {
//		f_data = value;
//	}
//	void set_s(T2 value) {
//		s_data = value;
//	}
//};
//int main() {
//	Box2<int, double> b;
//	b.set_f(10);
//	b.set_s(3.5);
//	cout << b.get_f() << b.get_s();
//}
//
//class Circle {
//	int radius;
//public:
//	Circle(int a=1) { radius = a; }
//	int getRadius() { return radius; }
//};
//template<class T>
//void myswap(T & a,T & b) {
//	T tmp;
//	tmp = a;
//	a = b;
//	b = tmp;
//}
//
//int main() {
//	Circle donut(5), pizza(20);
//	cout << donut.getRadius() << endl;
//	cout << pizza.getRadius() << endl;
//	myswap(donut, pizza);
//	cout << donut.getRadius() << endl;
//	cout << pizza.getRadius() << endl;
//}
//int main() {
//	int a, b;
//	cin >> a >> b;
//	try {
//		if (b == 0) throw b;
//		cout << a / b << endl;
//	}
//	catch (int b) {
//		cout << "입력 오류 입니다." << endl;
//	}
//}
//template <class T>
//class MyStack {
//	T data[5];
//	int top;
//public:
//	MyStack() :top(-1) {}
//	void push(T n)throw(char*) {
//		if (top >= 4) throw "stack is full";
//		top++;
//		data[top] = n;
//	}
//	T pop()throw(char*) {
//		if (top == -1) throw "stack is empty";
//		T t = data[top--];
//		return t;
//	}
//};
//int main() {
//	MyStack<int> st;
//	try {
//		st.push(1);
//		st.push(2);
//		cout << st.pop() << endl;
//		cout << st.pop() << endl;
//		cout << st.pop() << endl;
//	}
//	catch (const char*s) {
//		cout << s << endl;
//	}
//}