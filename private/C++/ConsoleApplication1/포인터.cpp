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
//		cout << "������ ȣ��" << endl;
//		age = 1;
//		name = "�ٵ���";
//	}
//	~Dog() {
//		cout << "�Ҹ��� ȣ��";
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
//	cout << "�������� ����: " << pDog->getAge() << endl;
//	pDog->setAge(5);
//	cout << "�������� ����: " << pDog->getAge() << endl;
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
//	cout << "�Է��� ������ ������?: ";
//	cin >> num;
//	int* p = new int[num];
//	for (int i = 0; i < num; i++) {
//		cout << i + 1 << "���� ����: ";
//		cin >> p[i];
//	}
//	int sum = 0;
//	for (int i = 0; i < num; i++) {
//		sum += p[i];
//	}
//	cout << "�����: " << sum / num;
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
//		cout << "������ ���� radius = " << radius << endl;
//	}
//	Circle(int r) {
//		radius = r;
//		cout << "������ ���� radius = " << radius << endl;
//	}
//	~Circle() {
//		cout << "�Ҹ��� ���� radius = " << radius << endl;
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
//		cout << "���� ������ �Է�(�����̸� ����)>>";
//		cin >> radius;
//		if (radius < 0) break;
//		Circle* p = new Circle(radius);
//		cout << "���� ������: " << p->getArea() << endl;
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
//		cout << "���� ������: " << pArray[i].getArea() << endl;
//	}
//	delete[] pArray;
//} - �������� �����Ǿ�� �Ϲ� �迭ó�� ���
//
//int main() {
//	Circle* pArray = new Circle[3];
//	pArray->set_Radius(10);
//	(pArray+1) ->set_Radius(20);
//	(pArray+2) ->set_Radius(30);
//	for (int i = 0; i < 3; i++) {
//		cout << "���� ������: " << (pArray+i)->getArea() << endl;
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
//	string address("����� ������ �Ｑ��");
//	cout << address;
//	cout << str;
//}

//int main() {
//	string s;
//	cout << "���ڿ��� �Է��Ͻÿ�" << endl;
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
//	cout << "���� ���ڸ� �Է��ϼ���. �Է��� ���� & �����Դϴ�." << endl;
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
//	cout << "������ ���� ����: ";
//	cin >> num;
//	Circle* pArray = new Circle[num];
//	for (int i = 0; i < num; i++) {
//		int value = rand() % 10;
//		pArray[i].setRadius(value);
//		cout << "������ ���� ��������: " << pArray[i].getRadius() << "�Դϴ�" << endl;
//	}
//	int count = 0;
//	for (int i = 0; i < num; i++) {
//		if (pArray[i].getArea() > 100)
//			count += 1;
//	}
//	cout << "100 �ʰ� ��: " << count << "�� �Դϴ�.";
//	return 0;
//}