#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

int def() {
	int answer = 46;
	int sug;
	do {
		cout << "������ �����Ͽ� ���ÿ�:";
		cin >> sug;
	} while (answer == sug); {
			if (answer > sug) {
				cout << "������ �������� Ů�ϴ�";
			}
			else
			{
				cout << "������ �������� �۽��ϴ�";
			}
	}
	cout << "�����Դϴ�";
	return 0;
}