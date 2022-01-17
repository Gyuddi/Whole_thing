//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <cstring>
//#include <ctime>
//#include <cstdlib>
//#include <vector>
//#include <algorithm>
//#include <array>
//using namespace std;
//
//class Point {
//public:
//	int x, y;
//	Point(int a = 0, int b = 0) { x = a, y = b; }
//	/*Point operator+(const Point& p);*/
//};
//Point operator+(const Point& p1, const Point& p2) {
//	Point tmp;
//	tmp.x = p1.x + p2.x;
//	tmp.y = p1.y + p2.y;
//	return tmp;
//}
//int main() {
//	Point p1(1, 2);
//	Point p2(2, 3);
//	Point p3 = p1 + p2;
//	cout << p3.x << p3.y;
//}
//class Power {
//	int kick;
//	int punch;
//public:
//	Power(int k = 0, int p = 0) {
//		kick = k;
//		punch = p;
//	}
//	void show() {
//		cout << "kick= " << kick << " " << "punch" << punch << endl;
//
//	}
//	Power& operator++();
//	bool operator!();
//};
//
//Power& Power :: operator++() {
//	kick++;
//	punch++;
//	return *this;
//}
//bool Power :: operator!() {
//	if (kick == 0 && punch == 0) { return true; }
//	else { return false; }
//}
//int main() {
//	Power a(10, 20), b;
//	b = ++a;
//	b.show();
//	cout << !b;
//}
//class Rect;
//class RectManager {
//public:
//	bool equals(Rect c, Rect s);
//};
//
//class Rect {
//	int width, height;
//public:
//	Rect(int w, int h) { width = w, height = h; }
//	friend RectManager;
//};
//
//bool RectManager :: equals(Rect c, Rect s) {
//	if (c.width == s.width && c.height == s.height) {
//		return true;
//	}
//	else { return false; }
//}
//int main() {
//	Rect a(3, 4), b(4, 5);
//	RectManager man;
//	cout << man.equals(a, b);
//	return 0;
//}
//
//class MyVector {
//	double x, y;
//public:
//	MyVector(double a = 0, double b = 0) :x{ a }, y{ b }{}
//	friend ostream& operator <<()
//};
//
//
//class Power {
//	int kick;
//	int punch;
//public:
//	Power(int k = 0, int p = 0) {
//		kick = k;
//		punch = p;
//	}
//	void show() {
//		cout << "kick= " << kick << " " << "punch" << punch << endl;
//
//	}
//	friend Power& operator++(Power& op);
//	friend Power operator==(Power op1, Power op2);
//
//};
//int main() {
//	Power a(3, 4), b(4, 6), c;
//	c = a++;
//	cout << a << " ," << b << " ," << endl;
//	c = ++b;
//	cout << a << " ," << b << " ," << endl;
//	cout << c << endl;
//	if (a == b) cout << "power가 같다. ";
//	else cout << "power가 같지 않다.";
//	return 0;
//}
