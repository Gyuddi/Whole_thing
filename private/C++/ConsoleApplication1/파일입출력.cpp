#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <array>
#include<fstream>
using namespace std;
int main() {
	//ofstream os{ "numbers.txt" };
	//if (!os){
	//	cerr << "���� ���¿� �����Ͽ����ϴ�" << endl;
	//	exit(1);
	//}
	//for (int i = 0; i < 100; i++)
	//	os << i << " ";
	ofstream os("numbers.txt", ios::app);
	if (!os) {
		cerr << "����" << endl;
		exit(1);
	}
	os << "���� �߰�������" << endl;
	return 0;
}
