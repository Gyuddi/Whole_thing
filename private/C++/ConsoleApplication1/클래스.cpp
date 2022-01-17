// 
//class Circle {
//public:
//	int radius;
//	string color;
//
//	double calcArea() {
//		return 3.14 * radius * radius;
//	}
//};
//
//int main() {
//	Circle pizza1, pizza2;
//	pizza1.radius = 120;
//	pizza2.radius = 150;
//	cout << pizza1.calcArea() << endl;
//	cout << pizza2.calcArea() << endl;
//	return 0;
//
//}

//class Car {
//public:
//	int speed;
//	int gear;
//	string color;
//	void speedUp() { //void는 반환 값이 없는 함수에서 사용된다.
//		speed += 10;
//	}
//	void speedDown() {
//		speed -= 10;
//	}
//};
//
//int main() {
//	Car myCar;
//	myCar.speed = 15;
//	myCar.gear = 2;
//	myCar.color = "red";
//	myCar.speedDown();
//	cout << myCar.speed << endl;
//	myCar.speedUp();
//	cout << myCar.speed << endl;
//
//	return 0;
//}

//class None {
//public:
//	void Print();
//};
//void None::Print() {
//	cout << "오오 신기방기";
//}
//int main(){
//	None q;
//	q.Print();
//	return 0;
//} // 클래스 밖에서 함수 정의가 가능하다.

//class Circle {
//public:
//	int radius;
//	string color;
//	Circle();
//	Circle(int r);
//
//	double calcArea() {
//		return 3.14 * radius * radius;
//	}
//};
//Circle::Circle() {
//	radius = 1;
//	cout << "반지름" << radius << "인 원 생성" << endl;
//}Circle::Circle(int r) {
//	radius = r;
//	cout << "반지름" << radius << "인 원 생성" << endl;
//}
//
//int main() {
//	Circle donut;
//	double area = donut.calcArea();
//	cout << "도넛 면적은 " << area << endl;
//	cout << area;
//
//	Circle pizza(30);
//	area = pizza.calcArea();
//	cout << "피자 면적은 " << area << endl;
//	cout<< area;
//}
//class Point {
//	int x, y;
//public:
//	Point();
//	Point(int a, int b);
//	void show() { cout << x << " " << y << endl; }
//};
//Point::Point() :Point(0, 0) {}
//Point::Point(int a, int b)
//	: x(a), y(b) {}
//
//int main() {
//	Point origin;
//	Point target(10, 20);
//	origin.show();
//	target.show();
//}
// 
//
//class Rectangle {
//public:
//	int a;
//	int b;
//	Rectangle();
//	Rectangle(int x, int y);
//	bool isSquare() {
//		if (a == b) {
//			return true;
//		}
//		else{
//			return false;
//		}
//	}
//};
//Rectangle::Rectangle() {
//	a = 4;
//	b = 4;
//}
//Rectangle::Rectangle(int x, int y) {
//	a = x;
//	b = y;
//}
//int main() {
//	Rectangle rect1;
//	Rectangle rect2(3, 5);
//	//Rectangle rect 3(3);
//	if (rect1.isSquare()) {
//		cout << "rec1은 정사각형이다." << endl;
//	}
//	if (rect2.isSquare()) {
//		cout << "rec2은 정사각형이다." << endl;
//	}
//	//if (rect3.isSquare()) {
//	//	cout << "rec3은 정사각형이다." << endl;
//	//}
//}

//class pizza {
//public:
//	pizza(int s) :size(s) {}
//	int size;
//};
//pizza creatpizza() {
//	pizza p(10);
//	return p;
//}
//int main() {
//	pizza pizza = creatpizza();
//	cout << pizza.size << "인치 피자" << endl;
//} // 참조자 &를 사용하여야 변수를 변화시킬 수 있다.
//
//class Circle {
//public:
//	int x, y;
//	int radius;
//	Circle() :x{ 0 }, y{ 0 }, radius{ 0 }{}
//	Circle(int x,int y,int r) :x{ x }, y{ y }, radius{ r }{}
//	void print() {
//		cout << "반지름: " << radius << "@(" << x << "," << y << ")" << endl;
//	}
//};
//
//
//int main() {
//	Circle objArray[10];
//	for (Circle& c : objArray) {
//		c.x = rand() % 500;
//		c.y = rand() % 300;
//		c.radius = rand() % 100;
//	}
//	for (Circle& c : objArray) {
//		c.print();
//	}
//	return 0;
//}

//int main() {
//	vector<int> v1;
//	for (int i = 10; i < 100; i += 10) {
//		v1.push_back(i);
//	}
//	cout << "v1 =" << endl;;
//	for (int a : v1) {
//		cout << a << " " ;
//	}
//	//while (v1.empty() != true) {
//	//	cout << v1.back() << " ";
//	//	v1.pop_back();
//	//}
//	cout << endl;
//	for (auto p = v1.begin(); p != v1.end(); p++) {
//		cout << *p << " ";
//	}
//	return 0;
//}
//class Person {
//private:
//	string name;
//	int age;
//public:
//	Person(string n, int a) {
//		name = n;
//		age = a;
//	} 
//	string get_name() { return name; }
//	int get_age() { return age; }
//	void print() {
//		cout << name << " " << age << endl;
//	}
//};
//
//bool compare(Person p, Person q) {
//	return p.get_age() < q.get_age();
//}
//int main() {
//	vector<Person> list;
//	list.push_back(Person("Kim", 20));
//	list.push_back(Person("Park", 22));
//	list.push_back(Person("Ku", 21));
//	sort(list.begin(), list.end(), compare);
//	for (auto& a : list) {
//		a.print();
//	}
//	
//	return 0;
//
//}
//
//
//int main() {
//	vector<int> scores;
//	int sum = 0;
//	int count = 0;
//	while (true) {
//		int score;
//		cout << "성적을 입력하시오 (종료는 -1)" << endl;
//		cin >> score;
//		if (score == -1) { break; }
//		scores.push_back(score);
//	}
//	for (int& a : scores) {
//		sum += a;
//		count += 1;
//
//	}
//	cout << "평균은 " << sum / count << "입니다.";
//	return 0;
//}
//
//int main() {
//	array<int, 3>list{ 1,2,3 };
//	for (int i = 0; i < list.size(); ++i) {
//		cout << list[i] << endl;
//		++list[i];
//		cout << list[i] << endl;
//	}
//	for (auto& elem : list)
//		cout << elem << " ";
//	return 0;
//}
//
//class Student {
//private:
//	string name;
//	double marks;
//public:
//	Student(string s,double m):name{s},marks(m){}
//	void print() {
//		cout << "이름: " << name << "학점: " << marks << endl;
//	}
//	void set_name(string n) { name = n; }
//	void set_marks(double m) { marks = m; }
//	string get_name() { return name; }
//	double get_marks() { return marks; }
//};
//bool compare(Student& a,Student& b) {
//	return a.get_marks() > b.get_marks();
//}
//int main() {
//	vector<Student> list;
//	string name;
//	double marks;
//	for (int i = 0; i < 5; ++i) {
//		cout << "학생 이름을 입력하시오";
//		cin >> name;
//		cout << "성적을 입력하시오";
//		cin >> marks;
//		list.push_back(Student(name, marks));
//	}
//	sort(list.begin(), list.end(), compare);
//	for (auto& a : list) {
//		a.print();
//		cout << endl;
//	}
//	return 0;
//}