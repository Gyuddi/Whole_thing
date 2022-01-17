//#include <iostream>
//#include <string>
//#include <ctime>
//#include <cstdlib>
//#include <vector>
//#include <algorithm>
//#include <array>
//using namespace std;

//int main() {
//	int number = 10;
//	int* p;
//	p = &number;
//	cout << *p;
//}
//int main() {
//	int* ptr;
//	srand(time(NULL));
//	ptr = new int[10];
//}
//class Dog {
//private:
//	string name;
//	int age;
//public:
//	Dog() {
//		cout << "생성자 호출" << endl;
//		age = 1;
//		name = "바둑이";
//	}
//	~Dog() {
//		cout << "소멸자 호출";
//	}
//	int get_age() {
//		return age;
//	}
//	void set_age(int a) {
//		age = a;
//	}
//};
//int main() {
//	Dog* pDog = new Dog;
//	cout << pDog->get_age() << endl;
//	pDog->set_age(5);
//	cout << pDog->get_age() << endl;
//	delete pDog;
//	return 0;
//}
//
//class Dog {
//private:
//	int* pWeight;
//	int* pAge;
//public:
//	Dog() {
//		pAge = new int(1);
//		pWeight = new int(10);
//	}
//	~Dog() {
//		delete pAge;
//		delete pWeight;
//	}
//	int getAge() { return *pAge; }
//	void setAge(int age) { *pAge = age; }
//	int getWeight() { return *pWeight; }
//	void setWeight(int weight) { *pWeight = weight; }
//};
//
//int main() {
//	Dog *pDog = new Dog;
//	cout << "강아지의 나리: " << pDog->getAge() << endl;
//	pDog->setAge(5);
//	cout << "강아지의 나이: " << pDog->getAge() << endl;
//	delete pDog;
//	return 0;
//}
//
//class Circle {
//	int radius;
//public:
//	Circle() { radius = 1; }
//	Circle(int r) { radius = r; }
//	double getArea();
//};
//double Circle::getArea(){
//	return 3.14 * radius * radius;
//}
//int main() {
//	Circle donut;
//	Circle pizza(30);
//	cout << donut.getArea() << endl;
//	Circle* p;
//	p = &donut;
//	cout << p->getArea() << endl;
//	cout << (*p).getArea() << endl;
//	p = &pizza;
//	cout << p->getArea() << endl;
//	cout << (*p).getArea() << endl;
//	return 0;
//}
//int main() {
//	int num;
//	int value;
//	cout << "입력할 정수의 개수는?: ";
//	cin >> num;
//	int* p = new int[num];
//	for (int i = 0; i < num; i++) {
//		cout << i + 1 << "번쩨 정수: ";
//		cin >> p[i];
//	}
//	int sum = 0;
//	for (int i = 0; i < num; i++) {
//		sum += p[i];
//	}
//	cout << "평균은: " << sum / num;
//		
//	delete[] p;
//	return 0;
//}
//
//class Circle {
//	int radius;
//public:
//	Circle() {
//		radius = 1;
//		cout << "생상자 실행 radius = " << radius << endl;
//	}
//	Circle(int r) {
//		radius = r;
//		cout << "생상자 실행 radius = " << radius << endl;
//	}
//	~Circle() {
//		cout << "소멸자 실행 radius = " << radius << endl;
//	}
//	double getArea() {
//		return 3.14 * radius * radius;
//	}
//	void set_Radius(int a) {
//		radius = a;
//	}
//};

//int main() {
//	int radius;
//	while (true) {
//		cout << "정수 반지름 입력(음수이면 종료)>>";
//		cin >> radius;
//		if (radius < 0) break;
//		Circle* p = new Circle(radius);
//		cout << "원의 면적은: " << p->getArea() << endl;
//		delete [] p;
//	}
//}
////
//int main() {
//	Circle* pArray = new Circle[3];
//	pArray[0].set_Radius(10);
//	pArray[1].set_Radius(20);
//	pArray[2].set_Radius(30);
//	for (int i = 0; i < 3; i++) {
//		cout << "원의 면적은: " << pArray[i].getArea() << endl;
//	}
//	delete[] pArray;
//} - 동적으로 생성되었어도 일반 배열처럼 사용
//
//int main() {
//	Circle* pArray = new Circle[3];
//	pArray->set_Radius(10);
//	(pArray+1) ->set_Radius(20);
//	(pArray+2) ->set_Radius(30);
//	for (int i = 0; i < 3; i++) {
//		cout << "원의 면적은: " << (pArray+i)->getArea() << endl;
//}
//}
//class Circle {
//	int radius;
//public:
//	Circle() { radius = 1; }
//	Circle(int radius) { this->radius = radius; }
//	void setRadius(int radius) { this->radius = radius; }
//	int getRadius() { return radius; }
//};
//
//int main() {
//	Circle p(4);
//	cout << p.getRadius() << endl;
//	p.setRadius(6);
//	cout << p.getRadius() << endl;
//}
// - STRING

//int main() {
//	string str = "dkssud";
//	string address("서울시 성복구 삼선동");
//	cout << address;
//	cout << str;
//}

//int main() {
//	string s;
//	cout << "문자열을 입력하시오" << endl;
//	getline(cin, s, '\n');
//	int len = s.length(); 
//	for (int i = 0; i < len; i++) {
//		string first = s.substr(0, 1);
//		string sub = s.substr(1, len - 1);
//		s = sub + first;
//		cout << s << endl;
//	}
//}

//int main() {
//	string s;
//	cout << "여러 문자를 입력하세요. 입력의 끝은 & 문자입니다." << endl;
//	getline(cin, s, '&');
//	//cin.ignore();
//	string f, r;
//	cout << endl << "find: ";
//	getline(cin, f, '\n');
//	cout << "replace: ";
//	getline(cin, r, '\n');
//
//	int startindex = 0;
//	while (true) {
//		int findex = s.find(f, startindex);
//		if (findex == -1)
//			break;
//		s.replace(findex, f.length(), r);
//		startindex = findex + f.length();
//	}
//	cout << s << endl;
//}
//
//class Circle {
//	int radius;
//public:
//	Circle() { radius = 1; }
//	Circle(int r) { radius = r; }
//	void setRadius(int a) { radius = a; }
//	double getRadius() { return radius; }
//	double getArea() { return 3.14 * radius * radius; }
//};
//
//int main() {
//	srand(time(NULL));
//	int num;
//	int value;
//	cout << "생성할 원의 개수: ";
//	cin >> num;
//	Circle* pArray = new Circle[num];
//	for (int i = 0; i < num; i++) {
//		int value = rand() % 10;
//		pArray[i].setRadius(value);
//		cout << "생성된 원의 반지름은: " << pArray[i].getRadius() << "입니다" << endl;
//	}
//	int count = 0;
//	for (int i = 0; i < num; i++) {
//		if (pArray[i].getArea() > 100)
//			count += 1;
//	}
//	cout << "100 초과 원: " << count << "개 입니다.";
//	return 0;
//}