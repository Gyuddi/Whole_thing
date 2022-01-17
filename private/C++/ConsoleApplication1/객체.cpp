//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <cstring>
//#include <ctime>
//#include <cstdlib>
//#include <vector>
//#include <algorithm>
//#include <array>
//using namespace std;


//class Circle {
//	int radius;
//public:
//	Circle() { radius = 1; }
//	Circle(int r) { radius = r; }
//	void setRadius(int a) { radius = a; }
//	double getRadius() { return radius; }
//	double getArea() { return 3.14 * radius * radius; }
//
//};
//
//void upgrade(Circle* a) {
//	a->setRadius(20);
//}
//int main() {
//	Circle c(10);
//	upgrade(c);
//	cout<<c.getRadius();

//}
//int main() {
//	int n = 2;
//	int& a = n;
//		cout << a;
//}

// 얕은 복사, 깊은 복사
//
//class Circle {
//	int radius;
//public:
//	Circle(const Circle& c);
//	Circle() { radius = 1; }
//	Circle(int r) { radius = r; }
//	void setRadius(int a) { radius = a; }
//	double getRadius() { return radius; }
//	double getArea() { return 3.14 * radius * radius; }
//};
//Circle::Circle(const Circle& c) {
//	this->radius = c.radius;
//	cout << "복사 생성자 실행 radius = " << radius << endl;
//}
//int main() {
//	Circle a(30);
//	Circle copy_a(a);
//	cout << a.getArea() << endl;
//	cout << copy_a.getArea() << endl;
//	return 0;
//}
//
//class Person {
//	char* name;
//	int id;
//public:
//	Person(const Person& p);
//	Person(const char* n, int i) {
//		id = i;
//		int len = strlen(n);
//		name = new char[len + 1];
//		strcpy(name,n);
//	}
//	~Person() {
//		delete[] name;
//	}
//	void changeName(const char* name) {
//		strcpy(this->name, name);
//	}
//	void show() {
//		cout << id << "," << name << endl;
//	}
//};
//Person::Person(const Person& p) {
//	this->id = p.id;
//	int len = strlen(p.name);
//	this->name = new char[len + 1];
//	strcpy(this->name, p.name);
//}
//int main() {
//	Person father("Han", 2 );
//	Person son(father);
//	cout << "son 객체 생성 직후______" << endl;
//	father.show();
//	son.show();
//	son.changeName("Que");
//	cout << "이름 변경 후______" << endl;
//	father.show();
//	son.show();
//	return 0;
//}
//
//
//class Circle {
//	int radius;
//	
//public:
//	static int count;
//	Circle() {
//		radius = 1;
//		count++;
//	}
//	Circle(int r) {
//		radius = r;
//		count++;
//	}
//	void setRadius(int a) { radius = a; }
//	double getRadius() { return radius; }
//	double getArea() { return 3.14 * radius * radius; }
//	static int getCount() {
//		return count;
//	}
//
//};
//int Circle::count = 0;
//int main() {
//	Circle a;
//	Circle b;
//	cout << a.getCount();
//}