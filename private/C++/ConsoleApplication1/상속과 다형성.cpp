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
//	int x, y;
//public:
//	void set(int x, int y) { this->x = x, this->y = y; }
//	void showPoint() {
//		cout << "(" << x << "," << y << ")" << endl;
//	}
//};
//class ColorPoint :public Point {
//	string color;
//public:
//	void setColor(string color) { this->color = color; }
//	void showColorPoint() {
//		cout << color << ":";
//		showPoint();
//	}
//};
//int main() {
//	Point p;
//	ColorPoint cp;
//	cp.set(3, 4);
//	cp.setColor("Red");
//	cp.showColorPoint();
//}
//class Car {
//	int speed;
//public:
//	Car() {
//		cout << "Car 생성자()" << endl;
//	}
//	Car(int a = 0) :speed{ a } {
//		cout << "Car생성자(int a)" << endl;
//	}
//	~Car() { cout << "Car소멸자" << endl; }
//	void setSpeed(int a) {
//		speed = a;
//	}
//	void getSpeed() { cout << speed << endl; }
//};
//
//class SportCar :public Car {
//	int turbo;
//public:
//	SportCar(int a = 0,bool x = false) :Car(a) {
//		x = turbo;
//		cout << "SportCar 생성자" << endl;
//	}
//	~SportCar() { cout << "SportCar소멸자" << endl; }
//	void setTurbo(bool newv) {
//		turbo = newv;
//	}
//	void getTurbo() { cout << turbo  << endl; }
//};
//
//int main() {
//	SportCar p(10, true);
//	p.getSpeed();
//	p.getTurbo();
//}

//class TV {
//	int size;
//public:
//	TV() { size = 20; }
//	TV(int s) { size = s; }
//	int getSize() { return size; }
//};
//class WideTV : public TV {
//	bool videoln;
//public:
//	WideTV(int s, bool v) :TV(s) {
//		videoln = v;
//	}
//	bool getVideoln() { return videoln; }
//};
//class SmartTV : public WideTV {
//	string ipAddr;
//public:
//	SmartTV(int s, bool v, string i) :WideTV(s, v) {
//		ipAddr = i;
//	}
//	string getipAddr() { return ipAddr; }
//};
//
//int main() {
//	SmartTV htv(59, true, "195.225");
//	cout << htv.getipAddr() << endl;
//	cout << htv.getVideoln() << endl;
//	cout << htv.getSize() << endl;
//}
//
//class Adder {
//protected:
//	int add(int a, int b) { return a + b; }
//};
//class Subtractor {
//protected:
//	int minus(int a, int b) { return a - b; }
//};
//class Calculator : public Adder, public Subtractor {
//public:
//	int calc(char op, int a, int b) {
//		int res = 0;
//		switch (op) {
//		case '+': res = add(a, b); break;
//		case '-':res = minus(a, b); break;
//		}
//		return res;
//	}
//};
//int main() {
//	Calculator c;
//	cout << "2+4= " << c.calc('+', 2, 4) << endl;
//	cout << "100-8= " << c.calc('-', 100, 8) << endl;
////	}
//
//class Animal {
//public:
//	void speak() { cout << "Animal Speak" << endl; }
//};
//class Dog :public Animal {
//public:
//	int age;
//	void speak() { cout << "멍멍" << endl; }
//};
//class Cat :public Animal {
//
//public:
//	int age; 
//	void speak() { cout << "야웅" << endl; }
//};
//int main() {
//	Dog* a1 = new Dog();
//	a1->speak();
//	a1->age = 10;
//	cout << a1->age << endl;
//	Animal* a2 = new Cat();
//	a2->speak();
//
//}

//class Base {
//public:
//	virtual void f() = 0; /*{
//		cout << "Base::f() called" << endl;
//	}*/
//};
//class Derived :public Base {
//public:
//	virtual void f() {
//		cout << "Derived::f() called" << endl;
//	}
//};
//int main() {
//	Base* q;
//	Derived a, * p;
//	p = &a;
//	q = &a;
//	p->f();
//	q->f();
//}
//
//class Calculator {
//public:
//	virtual int add(int a, int b) = 0;
//	virtual int subtract(int a, int b) = 0;
//	virtual double average(int a[], int size) = 0;
//};
//class Goodcalc :public Calculator {
//public:
//	int add(int a, int b) { return a + b; }
//	int subtract(int a, int b) { return a - b; }
//	double average(int a[], int size) {
//		double sum = 0;
//		for (int i = 0; i < size; i++) {
//			sum += a[i];
//		}
//		return sum / size;
//	}
//};
//int main() {
//	int a[] = { 1,2,3,4,5,6,7,8,9 };
//	Goodcalc* p = new Goodcalc;
//	cout << p->add(2, 3) << endl;
//	cout << p->average(a, 9);
////}
//class Shape {
//protected:
//	int x, y;
//public:
//	Shape(int x, int y) :x(x), y(y) {}
//	virtual void draw() {
//		cout << "Shape Draw" << endl;
//	}
//};
//class Rect :public Shape {
//	int width, height;
//public:
//	Rect(int x, int y, int w, int h) :Shape(x, y), width(w), height(h) {}
//	void draw() {
//		cout << "Rectangle Draw" << endl;
//	}
//};
//int main() {
//	Shape* ps = new Rect(0, 0, 100, 200);
//	ps->draw();
//	delete ps;
//}
//
//class Shape {
//public:
//	virtual void draw() {
//		cout << "--Shape--" << endl;
//	}
//};
//class Circle : public Shape {
//public:
//	virtual void draw() {
//		Shape::draw();
//		cout << "Circle" << endl;
//	}
//};
//int main() {
//	Circle circle;
//	Shape* pshape = &circle;
//	pshape->draw();
//	pshape->Shape::draw();
//}
//
//class String {
//	char* s;
//public:
//	String(char* p) {
//		cout << "String 생성자" << endl;
//		s = new char[strlen(p) + 1];
//		strcpy(s, p);
//	}
//	~String() {
//		cout << "String 소멸자" << endl;
//		delete[] s;
//	}
//	virtual void display() {
//		cout << s;
//	}
//};
//class MyString :public String {
//	char* header;
//public:
//	MyString(char* h, char* p) :String(p) {
//		cout << "MyString 생성자" << endl;
//		header = new char[strlen(h) + 1];
//		strcpy(header, h);
//	}
//	~MyString() {
//		cout << "MyString 소멸자" << endl;
//		delete[] header;
//	}
//	void display() {
//		cout << header;
//		String::display();
//		cout << header << endl;
//	}
//};
//
//int main() {
//	String* p = new MyString("----", "Hello World");
//	p->display();
//	delete p;
//	return 0;
//}
//class Converter {
//protected:
//	double r;
//	virtual double convert(double src) = 0;
//	virtual string getSource() = 0;
//	virtual string getDest() = 0;
//public:
//	Converter(double r) { this->r = r; }
//	void run() {
//		double src;
//		cout << getSource() << "을" << getDest() << "으로 바꿉니다" << endl;
//		cout << getSource() << "을 입력하세요";
//		cin >> src;
//		cout << "변화 결과: " << convert(src) << getDest() << endl;
//	}
//};
//class WontoDollar :public Converter {
//protected:
//	virtual double convert(double src) {
//		return src / r;
//	}
//	virtual string getSource() { return "원"; }
//	virtual string getDest() { return "달러"; }
//public:
//	WontoDollar(double r) :Converter(r) {}
//};
//class KmToMile :public Converter {
//protected:
//	virtual double convert(double src) { return src / r; }
//	virtual string getSource() {
//		return "KM";
//	}
//	virtual string getDest() {
//		return "Mile";
//	}
//public:
//	KmToMile(double r) :Converter(r) {}
//};
//
//int main() {
//	KmToMile km(1.62);
//	WontoDollar wd(1200);
//	Converter* p;
//	p = &km;
//	p->run();
//	p = &wd;
//	p->run();
//}